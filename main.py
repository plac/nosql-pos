import redis

r = redis.Redis(host='localhost', port=6379, db=0)

cartela = 'cartela'
scores = 'scores'
game = 'jogo'
max_score = 15

class User:
    def __init__(self, idx):
        self.name = 'user:{}'.format(idx)
        self.bcartela = 'cartela:{}'.format(idx)
        self.bscore = 'score:{}'.format(idx)
    
    def pretty(self):
        return '\nUser:\nname: {}\ncartela: {}\nscore: {}'.format(self.name, self.bcartela, self.bscore)
    
    def __repr__(self):
        return str(self.__dict__)

def printScore():
    print(r.zrange(scores, 0, -1, desc=True, withscores=True))

def printWinners(rounds):

    print('Sorteados:', rounds)

    s = r.zrange(scores, 0, -1, desc=True, withscores=True)
    print("\nBINGOOO!\n\n\nGanhadores:\n")
    print([ (name, score) for name, score in s if score == max_score ])

def someone_won():
    s = r.zrange(scores, 0, -1, desc=True, withscores=True)
    return s[0][1] >= max_score

def round_number():
    number = r.srandmember(game)
    r.srem(game, number)
    return number

def main():
    # setup/seed
    cartela_original = [ x for x in range(0, 100) ]
    r.sadd(cartela, *cartela_original)
    r.sadd(game, *cartela_original)

    users = [ User(x) for x in range(1, 51)]

    for user in users:
        r.hmset(user.name, user.__dict__)
        numbers = r.srandmember(cartela, 15)
        r.delete(user.bcartela)
        r.sadd(user.bcartela, *numbers)
        r.zadd(scores, { user.name: 0 })

    # game

    rounds = []
    while not someone_won():
        n = round_number()        

        rounds.append(n)

        for user in users:
            if r.sismember(user.bcartela, n):
                r.zincrby(scores, 1, user.name)
            

    printWinners(rounds)

if __name__ == "__main__":
    main()