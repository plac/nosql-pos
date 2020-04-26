## MongoDB

### Exercício 1 - Aquecendo com os pets

#### 1. Adicione outro Peixe e um Hamster com nome Frodo

```
> db.pets.insert({name: "Frodo", species: "Peixe"})
WriteResult({ "nInserted" : 1 })
> db.pets.insert({name: "Frodo", species: "Hamster"})
WriteResult({ "nInserted" : 1 })
``` 
#### 2. Faça uma contagem dos pets na coleção

```
> db.pets.count()
8
``` 

#### 3. Retorne apenas um elemento o método prático possível

```
> db.pets.findOne()
{
        "_id" : ObjectId("5ea08494d9eb40e8b2e729d9"),
        "name" : "Mike",
        "species" : "Hamster"
}

``` 

#### 4. Identifique o ID para o Gato Kilha.

```
> db.pets.find({name:"Kilha"}, {_id:1})
{ "_id" : ObjectId("5ea0858ad9eb40e8b2e729db") }
```

#### 5. Faça uma busca pelo ID e traga o Hamster Mike

```
> db.pets.find({_id : ObjectId("5ea08494d9eb40e8b2e729d9")})
{ "_id" : ObjectId("5ea08494d9eb40e8b2e729d9"), "name" : "Mike", "species" : "Hamster" }
```

#### 6. Use o find para trazer todos os Hamsters

```
> db.pets.find({species: "Hamster"})
{ "_id" : ObjectId("5ea08494d9eb40e8b2e729d9"), "name" : "Mike", "species" : "Hamster" }
{ "_id" : ObjectId("5ea0899c94476872ce6c4ae6"), "name" : "Frodo", "species" : "Hamster" }
``` 

#### 7. Use o find para listar todos os pets com nome Mike

```
> db.pets.find({name: "Mike"})
{ "_id" : ObjectId("5ea08494d9eb40e8b2e729d9"), "name" : "Mike", "species" : "Hamster" }
{ "_id" : ObjectId("5ea085a2d9eb40e8b2e729dc"), "name" : "Mike", "species" : "Cachorro" }
``` 

#### 8. Liste apenas o documento que é um Cachorro chamado Mike

```
> db.pets.find({name: "Mike", species: "Cachorro"})
{ "_id" : ObjectId("5ea085a2d9eb40e8b2e729dc"), "name" : "Mike", "species" : "Cachorro" }
```

### Exercício 2 – Mama mia!


#### 1. Liste/Conte todas as pessoas que tem exatamente 99 anos. Você pode usar um count para indicar a quantidade.

```
> db.italians.find({age: 99}).count()
0
```

#### 2. Identifique quantas pessoas são elegíveis atendimento prioritário (pessoas com mais de 65 anos)

```
> db.italians.find({age: {"$gt": 65}}).count()
1763
```

#### 3. Identifique todos os jovens (pessoas entre 12 a 18 anos).

```
> db.italians.find({age: {"$gte": 12, "$lte": 18}}).count()
923
```

#### 4. Identifique quantas pessoas tem gatos, quantas tem cachorro e quantas não tem nenhum dos dois

```
> db.italians.find({cat: {"$exists": true}}).count()
5926

> db.italians.find({dog: {"$exists": true}}).count()
4018

> db.italians.find(
    {"$and": [
        {dog: {"$exists": false}}, 
        {cat: {"$exists": false}}
    ]}).count()
2445

```

#### 5. Liste/Conte todas as pessoas acima de 60 anos que tenham gato

```
> db.italians.find({"$and": [{age: {"$gt": 60}}, {cat: {"$exists": true}}]}).count()
1431
```

#### 6. Liste/Conte todos os jovens com cachorro 

```
> db.italians.find({$and: [{age: {"$gte": 12, "$lte": 18}}, {dog: {"$exists": true}}]}).count()
376
```

#### 7. Utilizando o $where, liste todas as pessoas que tem gato e cachorro

```
> db.italians.find({$where: function() { return this.cat && this.dog }}).count()
2389
```

#### 8. Liste todas as pessoas mais novas que seus respectivos gatos.

```
> db.italians.find({$where: function() { return this.age && this.cat && this.cat.age > this.age }}, { _id: 0, "firstname": 1, "age":1, "cat.name": 1, "cat.age": 1 })
{ "firstname" : "Massimo", "age" : 1, "cat" : { "name" : "Chiara", "age" : 2 } }
{ "firstname" : "Stefano", "age" : 1, "cat" : { "name" : "Roberto", "age" : 14 } }
{ "firstname" : "Silvia", "age" : 4, "cat" : { "name" : "Giorgia", "age" : 12 } }
{ "firstname" : "Fabrizio", "age" : 6, "cat" : { "name" : "Federica", "age" : 12 } }
{ "firstname" : "Stefania", "age" : 2, "cat" : { "name" : "Gabiele", "age" : 17 } }
{ "firstname" : "Cristian", "age" : 9, "cat" : { "name" : "Cristian", "age" : 14 } }
{ "firstname" : "Giusy", "age" : 3, "cat" : { "name" : "Marta", "age" : 13 } }
{ "firstname" : "Alessio", "age" : 15, "cat" : { "name" : "Marta", "age" : 17 } }
{ "firstname" : "Giovanna", "age" : 2, "cat" : { "name" : "Alex", "age" : 15 } }
{ "firstname" : "Sara", "age" : 5, "cat" : { "name" : "Alessandra", "age" : 10 } }
{ "firstname" : "Andrea", "age" : 16, "cat" : { "name" : "Chiara", "age" : 17 } }
{ "firstname" : "Federico", "age" : 8, "cat" : { "name" : "Giuseppe", "age" : 17 } }
{ "firstname" : "Giacomo", "age" : 3, "cat" : { "name" : "Giovanni", "age" : 14 } }
{ "firstname" : "Elisa", "age" : 2, "cat" : { "name" : "Monica", "age" : 4 } }
{ "firstname" : "Angela", "age" : 13, "cat" : { "name" : "Domenico", "age" : 16 } }
{ "firstname" : "Barbara", "age" : 8, "cat" : { "name" : "Sergio", "age" : 9 } }
{ "firstname" : "Laura", "age" : 3, "cat" : { "name" : "Riccardo", "age" : 16 } }
{ "firstname" : "Manuela", "age" : 2, "cat" : { "name" : "Federico", "age" : 3 } }
{ "firstname" : "Veronica", "age" : 7, "cat" : { "name" : "Antonio", "age" : 9 } }
{ "firstname" : "Matteo", "age" : 12, "cat" : { "name" : "Sergio", "age" : 14 } }
```

#### 9. Liste as pessoas que tem o mesmo nome que seu bichano (gatou ou cachorro)

```
> db.italians.find({$where: function() { return this.surname && this.cat && this.cat.name == this.firstname }}, { _id: 0, "firstname": 1, "cat.name": 1 })
{ "firstname" : "Emanuele", "cat" : { "name" : "Emanuele" } }
{ "firstname" : "Cristian", "cat" : { "name" : "Cristian" } }
{ "firstname" : "Giusy", "cat" : { "name" : "Giusy" } }
{ "firstname" : "Teresa", "cat" : { "name" : "Teresa" } }
{ "firstname" : "Alessio", "cat" : { "name" : "Alessio" } }
{ "firstname" : "Salvatore", "cat" : { "name" : "Salvatore" } }
{ "firstname" : "Michele", "cat" : { "name" : "Michele" } }
{ "firstname" : "Roberta", "cat" : { "name" : "Roberta" } }
{ "firstname" : "Serena", "cat" : { "name" : "Serena" } }
{ "firstname" : "Davide", "cat" : { "name" : "Davide" } }
{ "firstname" : "Angela", "cat" : { "name" : "Angela" } }
{ "firstname" : "Paolo", "cat" : { "name" : "Paolo" } }
{ "firstname" : "Pasquale", "cat" : { "name" : "Pasquale" } }
{ "firstname" : "Fabrizio", "cat" : { "name" : "Fabrizio" } }
{ "firstname" : "Maurizio", "cat" : { "name" : "Maurizio" } }
{ "firstname" : "Filipo", "cat" : { "name" : "Filipo" } }
{ "firstname" : "Giovanna", "cat" : { "name" : "Giovanna" } }
{ "firstname" : "Pasquale", "cat" : { "name" : "Pasquale" } }
{ "firstname" : "Patrizia", "cat" : { "name" : "Patrizia" } }
{ "firstname" : "Pietro", "cat" : { "name" : "Pietro" } }
Type "it" for more
```

#### 10. Projete apenas o nome e sobrenome das pessoas com tipo de sangue de fator RH negativo

```
> db.italians.find({"bloodType": {$regex: "-$"}}, { _id: 0, "firstname": 1, "surname": 1 })
{ "firstname" : "Emanuele", "surname" : "Basile" }
{ "firstname" : "Alessio", "surname" : "Carbone" }
{ "firstname" : "Elena", "surname" : "De Luca" }
{ "firstname" : "Giorgia", "surname" : "Fontana" }
{ "firstname" : "Luca", "surname" : "Conte" }
{ "firstname" : "Alessia", "surname" : "Palumbo" }
{ "firstname" : "Valeira", "surname" : "Grassi" }
{ "firstname" : "Massimo", "surname" : "Orlando" }
{ "firstname" : "Gianni", "surname" : "Fontana" }
{ "firstname" : "Elisa", "surname" : "Coppola" }
{ "firstname" : "Valeira", "surname" : "Ferretti" }
{ "firstname" : "Rita", "surname" : "Greco" }
{ "firstname" : "Barbara", "surname" : "Ruggiero" }
{ "firstname" : "Silvia", "surname" : "Sorrentino" }
{ "firstname" : "Claudia", "surname" : "Mancini" }
{ "firstname" : "Giuseppe", "surname" : "Gentile" }
{ "firstname" : "Mirko", "surname" : "Fabbri" }
{ "firstname" : "Massimiliano", "surname" : "Silvestri" }
{ "firstname" : "Rita", "surname" : "Bernardi" }
{ "firstname" : "Mirko", "surname" : "Fontana" }
Type "it" for more

```

#### 11. Projete apenas os animais dos italianos. Devem ser listados os animais com nome e idade. Não mostre o identificado do mongo (ObjectId)

```
> db.italians.find({"$or": [{cat: {$exists: true}}, {dog: {$exists: true}}]},{_id: 0, "cat": 1, "dog": 1})
{ "cat" : { "name" : "Emanuele", "age" : 13 } }
{ "cat" : { "name" : "Mirko", "age" : 11 } }
{ "dog" : { "name" : "Chiara", "age" : 5 } }
{ "cat" : { "name" : "Giusy", "age" : 5 } }
{ "cat" : { "name" : "Tiziana", "age" : 4 }, "dog" : { "name" : "Enzo ", "age" : 3 } }
{ "dog" : { "name" : "Paola", "age" : 15 } }
{ "cat" : { "name" : "Filipo", "age" : 8 } }
{ "cat" : { "name" : "Pietro", "age" : 2 }, "dog" : { "name" : "Claudia", "age" : 16 } }
{ "cat" : { "name" : "Antonio", "age" : 2 }, "dog" : { "name" : "Patrizia", "age" : 10 } }
{ "cat" : { "name" : "Filipo", "age" : 5 }, "dog" : { "name" : "Valentina", "age" : 9 } }
{ "dog" : { "name" : "Sergio", "age" : 7 } }
{ "cat" : { "name" : "Silvia", "age" : 11 } }
{ "dog" : { "name" : "Martina", "age" : 7 } }
{ "dog" : { "name" : "Pasquale", "age" : 7 } }
{ "cat" : { "name" : "Dario", "age" : 9 } }
{ "cat" : { "name" : "Serena", "age" : 14 }, "dog" : { "name" : "Gianni", "age" : 12 } }
{ "cat" : { "name" : "Chiara", "age" : 4 }, "dog" : { "name" : "Pasquale", "age" : 1 } }
{ "cat" : { "name" : "Gianluca", "age" : 12 }, "dog" : { "name" : "Daniele", "age" : 8 } }
{ "dog" : { "name" : "Emanuela", "age" : 15 } }
{ "dog" : { "name" : "Michela", "age" : 1 } }
Type "it" for more
```

#### 12. Quais são as 5 pessoas mais velhas com sobrenome Rossi?

```
> db.italians.find({"surname": "Rossi"}, {_id: 0, firstname:1, lastname: 1, age:1}).sort({age: -1}).limit(5)
{ "firstname" : "Mauro", "age" : 79 }
{ "firstname" : "Claudio", "age" : 78 }
{ "firstname" : "Serena", "age" : 78 }
{ "firstname" : "Filipo", "age" : 77 }
{ "firstname" : "Sara", "age" : 77 }
```

#### 13. Crie um italiano que tenha um leão como animal de estimação. Associe um nome e idade ao bichano

```
> db.italians.insert({
...         "firstname" : "Francesco",
...         "surname" : "Totti",
...         "username" : "totti",
...         "age" : 21,
...         "email" : "Roberto.Rossi@uol.com.br",
...         "bloodType" : "AB+",
...         "ticketNumber" : 3796,
...         "jobs" : [
...                 "Jogador de Futebol"
...         ],
...         "favFruits" : [
...                 "Uva"
...         ],
...         "movies" : [
...                 {
...                         "title" : "Matrix (1999)",
...                         "rating" : 2
...                 },
...                 {
...                         "title" : "Filme do Pelé",
...                         "rating" : 10
...                 },
...                 {
...                         "title" : "Cidade de Deus (2002)",
...                         "rating" : 4.52
...                 }
...         ],
...         "lion" : {
...                 "name" : "Simba",
...                 "age" : 2
...         }
... }
... )
WriteResult({ "nInserted" : 1 })

```

#### 14. Infelizmente o Leão comeu o italiano. Remova essa pessoa usando o Id.

```
> db.italians.findOne({username: "totti"})
{
        "_id" : ObjectId("5ea1e5d483c68d117461e58d"),
        "firstname" : "Francesco",
        "surname" : "Totti",
        "username" : "totti",
        "age" : 21,
        "email" : "Roberto.Rossi@uol.com.br",
        "bloodType" : "AB+",
        "ticketNumber" : 3796,
        "jobs" : [
                "Jogador de Futebol"
        ],
        "favFruits" : [
                "Uva"
        ],
        "movies" : [
                {
                        "title" : "Matrix (1999)",
                        "rating" : 2
                },
                {
                        "title" : "Filme do Pelé",
                        "rating" : 10
                },
                {
                        "title" : "Cidade de Deus (2002)",
                        "rating" : 4.52
                }
        ],
        "lion" : {
                "name" : "Simba",
                "age" : 2
        }
}


> db.italians.remove({_id: ObjectId("5ea1e5d483c68d117461e58d")})
WriteResult({ "nRemoved" : 1 })
```

#### 15. Passou um ano. Atualize a idade de todos os italianos e dos bichanos em 1.

```
> db.italians.update({age: {$exists:true}}, {$inc: {age: 1}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })

> db.italians.update({"dog": {$exists:true}}, {$inc: {"dog.age": 1}})       
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })

> db.italians.update({"cat": {$exists:true}}, {$inc: {"cat.age": 1}})       
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })     
```

#### 16. O Corona Vírus chegou na Itália e misteriosamente atingiu pessoas somente com gatos e de 66 anos. Remova esses italianos.

```
> db.italians.remove({$and: [{age: 66}, { cat: {$exists:true}}]})
WriteResult({ "nRemoved" : 76 })
```

#### 17. Utilizando o framework agregate, liste apenas as pessoas com nomes iguais a sua respectiva mãe e que tenha gato ou cachorro.

```
> db.italians.aggregate([ {'$match': { mother: { $exists: 1} }}, {'$project': { "firstname": 1, "mother": 1, "dog": 1, "cat": 1, "isEqual": { "$cmp": ["$firstname","$mother.firstname"]} }}, {'$match': {"isEqual": 0}}, {$match: {$or:[{dog: {$exists: true} }, {cat: {$exists: true}} ]}} ])
{ "_id" : ObjectId("5ea08f046f9629ee7f2707af"), "firstname" : "Massimiliano", "mother" : { "firstname" : "Massimiliano", "surname" : "Riva", "age" : 53 }, "dog" : { "name" : "Stefano", "age" : 1 }, "isEqual" : 0 }
{ "_id" : ObjectId("5ea08f056f9629ee7f270b26"), "firstname" : "Nicola", "mother" : { "firstname" : "Nicola", "surname" : "Grasso", "age" : 62 }, "dog" : { "name" : "Laura", "age" : 16 }, "isEqual" : 0 }
{ "_id" : ObjectId("5ea08f076f9629ee7f271676"), "firstname" : "Alessandro", "mother" : { "firstname" : "Alessandro", "surname" : "D’Amico", "age" : 38 }, "cat" : { "name" : "Teresa", "age" : 6 }, "dog" : { "name" : "Sabrina", "age" : 17 }, "isEqual" : 0 }
{ "_id" : ObjectId("5ea08f0a6f9629ee7f272298"), "firstname" : "Alessandro", "mother" : { "firstname" : "Alessandro", "surname" : "Ferretti", "age" : 105 }, "dog" : { "name" : "Fabio", "age" : 6 }, "isEqual" : 0 }
{ "_id" : ObjectId("5ea08f0a6f9629ee7f272599"), "firstname" : "Andrea", "mother" : { "firstname" : "Andrea", "surname" : "Giordano", "age" : 68 }, "cat" : { "name" : "Eleonora", "age" : 4 }, "isEqual" : 0 }
{ "_id" : ObjectId("5ea08f0b6f9629ee7f27260c"), "firstname" : "Alessandra", "mother" : { "firstname" : "Alessandra", "surname" : "Farina", "age" : 55 }, "cat" : { "name" : "Pietro", "age" : 12 }, "isEqual" : 0 }
```

#### 18. Utilizando aggregate framework, faça uma lista de nomes única de nomes. Faça isso usando apenas o primeiro nome

```
> db.italians.aggregate([{$group: {_id: "firstname", uniqueNames: {$addToSet: "$firstname"} }}])
{ "_id" : "firstname", "uniqueNames" : [ "Luigi", "Barbara", "Michela", "Marta", "Cristian", "Luca", "Stefano", "Valentina", "Elisabetta", "Ilaria", "Massimiliano", "Fabio", "Gianni", "Roberto", "Rosa", "Chiara", "Alessio", "Gianluca", "Emanuele", "Sara", "Paola", "Laura", "Pietro", "Alessia", "Claudia", "Lorenzo", "Enrico", "Teresa", "Giovanna", "Simona", "Alessandra", "Alex", "Giuseppe", "Lucia", "Mauro", "Paolo", "Giorgio", "Patrizia", "Vincenzo", "Giacomo", "Angelo", "Federico", "Federica", "Alessandro", "Raffaele", "Pasquale", "Michele", "Massimo", "Giulia", "Daniele", "Angela", "Martina", "Fabrizio", "Alberto", "Anna", "Giusy", "Daniela", "Claudio", "Veronica", "Elena", "Salvatore", "Elisa", "Eleonora", "Davide", "Stefania", "Cristina", "Andrea", "Antonella", "Cinzia", "Simone", "Domenico", "Sabrina", "Valeira", "Mirko", "Antonio", "Nicola", "Sonia", "Emanuela", "Manuela", "Maurizio", "Serena", "Rita", "Gabiele", "Giovanni", "Mattia", "Riccardo", "Mario", "Dario", "Tiziana", "Roberta", "Filipo", "Sergio", "Enzo ", "Maria", "Monica", "Carlo", "Matteo", "Marco", "Giorgia", "Silvia" ] }
```

#### 19. Agora faça a mesma lista do item acima, considerando nome completo.

```
> db.italians.aggregate([{ $project: { name: { $concat: [ "$firstname", " ", "$surname" ] } } }, {$group: {_id: "$name", uniqueNames: {$addToSet: "$name"} }}])
{ "_id" : "Maurizio Giuliani", "uniqueNames" : [ "Maurizio Giuliani" ] }
{ "_id" : "Marco Milani", "uniqueNames" : [ "Marco Milani" ] }
{ "_id" : "Michele Villa", "uniqueNames" : [ "Michele Villa" ] }
{ "_id" : "Valentina Pellegrini", "uniqueNames" : [ "Valentina Pellegrini" ] }
{ "_id" : "Serena Parisi", "uniqueNames" : [ "Serena Parisi" ] }
{ "_id" : "Luca Romano", "uniqueNames" : [ "Luca Romano" ] }
{ "_id" : "Alberto Caputo", "uniqueNames" : [ "Alberto Caputo" ] }
{ "_id" : "Sara Fabbri", "uniqueNames" : [ "Sara Fabbri" ] }
{ "_id" : "Manuela Negri", "uniqueNames" : [ "Manuela Negri" ] }
{ "_id" : "Davide Piras", "uniqueNames" : [ "Davide Piras" ] }
{ "_id" : "Alessandro Marchetti", "uniqueNames" : [ "Alessandro Marchetti" ] }
{ "_id" : "Valeira Parisi", "uniqueNames" : [ "Valeira Parisi" ] }
{ "_id" : "Claudio Gentile", "uniqueNames" : [ "Claudio Gentile" ] }
{ "_id" : "Manuela Riva", "uniqueNames" : [ "Manuela Riva" ] }
{ "_id" : "Pietro Barbieri", "uniqueNames" : [ "Pietro Barbieri" ] }
{ "_id" : "Gianni Lombardi", "uniqueNames" : [ "Gianni Lombardi" ] }
{ "_id" : "Alessia Montanari", "uniqueNames" : [ "Alessia Montanari" ] }
{ "_id" : "Stefano Serra", "uniqueNames" : [ "Stefano Serra" ] }
{ "_id" : "Mauro Mancini", "uniqueNames" : [ "Mauro Mancini" ] }
{ "_id" : "Emanuela Gallo", "uniqueNames" : [ "Emanuela Gallo" ] }

> db.italians.aggregate([{ $project: { name: { $concat: [ "$firstname", " ", "$surname" ] } } }, {$group: {_id: "$name", uniqueNames: {$addToSet: "$name"} }}, {$count: "distinct fullname"}])
{ "distinct fullname" : 6302 }

```

#### 20. Procure pessoas que gosta de Banana ou Maçã, tenham cachorro ou gato, mais de 20 e menos de 60 anos.

```
db.italians.find({
$and: [
        {$or: [{ favFruits: "Maçã" },{ favFruits: "Banana"}]},
        {$or: [{dog : {$exists: true} },{ cat: {$exists: true}}]},
        {$and: [{age : {$gt: 20} },{ age: {$lt: 60}}]},
]})
1284
```

## Exercício 3 - Stockbrokers

#### 1. Liste as ações com profit acima de 0.5 (limite a 10 o resultado)

```
> db.stocks.find({"Profit Margin": { $gte: 0.5}}, {_id: 0, Ticker: 1, Company: 1, "Profit Margin": 1}).limit(10)
{ "Ticker" : "AB", "Profit Margin" : 0.896, "Company" : "AllianceBernstein Holding L.P." }
{ "Ticker" : "AGNC", "Profit Margin" : 0.972, "Company" : "American Capital Agency Corp." }
{ "Ticker" : "ARCC", "Profit Margin" : 0.654, "Company" : "Ares Capital Corporation" }
{ "Ticker" : "ARI", "Profit Margin" : 0.576, "Company" : "Apollo Commercial Real Estate Finance, Inc." }
{ "Ticker" : "ARR", "Profit Margin" : 0.848, "Company" : "ARMOUR Residential REIT, Inc." }
{ "Ticker" : "ATHL", "Profit Margin" : 0.732, "Company" : "Athlon Energy Inc." }
{ "Ticker" : "AYR", "Profit Margin" : 0.548, "Company" : "Aircastle LTD" }
{ "Ticker" : "BK", "Profit Margin" : 0.63, "Company" : "The Bank of New York Mellon Corporation" }
{ "Ticker" : "BLX", "Profit Margin" : 0.588, "Company" : "Banco Latinoamericano de Comercio Exterior, S.A" }
{ "Ticker" : "BPO", "Profit Margin" : 0.503, "Company" : "Brookfield Properties Corporation" }
}
```

#### 2. Liste as ações com perdas (limite a 10 novamente)

```
> db.stocks.find({"Profit Margin": { $lt: 0}}, {_id: 0, Ticker: 1, Company: 1, "Profit Margin": 1}).limit(10)
{ "Ticker" : "AAOI", "Profit Margin" : -0.023, "Company" : "Applied Optoelectronics, Inc." }
{ "Ticker" : "AAV", "Profit Margin" : -0.232, "Company" : "Advantage Oil & Gas Ltd." }
{ "Ticker" : "ABCD", "Profit Margin" : -0.645, "Company" : "Cambium Learning Group, Inc." }
{ "Ticker" : "ABFS", "Profit Margin" : -0.005, "Company" : "Arkansas Best Corporation" }
{ "Ticker" : "ABMC", "Profit Margin" : -0.0966, "Company" : "American Bio Medica Corp." }
{ "Ticker" : "ABX", "Profit Margin" : -0.769, "Company" : "Barrick Gold Corporation" }
{ "Ticker" : "ACCL", "Profit Margin" : -0.014, "Company" : "Accelrys Inc." }
{ "Ticker" : "ACFC", "Profit Margin" : -0.18, "Company" : "Atlantic Coast Financial Corporation" }
{ "Ticker" : "ACH", "Profit Margin" : -0.051, "Company" : "Aluminum Corporation Of China Limited" }
{ "Ticker" : "ACI", "Profit Margin" : -0.173, "Company" : "Arch Coal Inc." }
```

#### 3. Liste as 10 ações mais rentáveis

```
> db.stocks.find({}, {_id: 0, Ticker: 1, Company: 1, "Profit Margin": 1}).sort({"Profit Margin": -1}).limit(10)
{ "Ticker" : "BPT", "Profit Margin" : 0.994, "Company" : "BP Prudhoe Bay Royalty Trust" }
{ "Ticker" : "CACB", "Profit Margin" : 0.994, "Company" : "Cascade Bancorp" }
{ "Ticker" : "ROYT", "Profit Margin" : 0.99, "Company" : "Pacific Coast Oil Trust" }
{ "Ticker" : "NDRO", "Profit Margin" : 0.986, "Company" : "Enduro Royalty Trust" }
{ "Ticker" : "WHZ", "Profit Margin" : 0.982, "Company" : "Whiting USA Trust II" }
{ "Ticker" : "MVO", "Profit Margin" : 0.976, "Company" : "MV Oil Trust" }
{ "Ticker" : "AGNC", "Profit Margin" : 0.972, "Company" : "American Capital Agency Corp." }
{ "Ticker" : "VOC", "Profit Margin" : 0.971, "Company" : "VOC Energy Trust" }
{ "Ticker" : "MTR", "Profit Margin" : 0.97, "Company" : "Mesa Royalty Trust" }
{ "Ticker" : "OLP", "Profit Margin" : 0.97, "Company" : "One Liberty Properties Inc." }
```

#### 4. Qual foi o setor mais rentável?

```
> db.stocks.aggregate([{$group: {_id: "$Sector", profitTotal: {$sum: "$Profit Margin"}}}, {$sort: {profitTotal:-1}}])
{ "_id" : "Financial", "profitTotal" : 162.5356 }
{ "_id" : "Services", "profitTotal" : 20.5515 }
{ "_id" : "Consumer Goods", "profitTotal" : 13.23 }
{ "_id" : "Industrial Goods", "profitTotal" : 11.0327 }
{ "_id" : "Utilities", "profitTotal" : 7.423 }
{ "_id" : "Conglomerates", "profitTotal" : 0.3835 }
{ "_id" : "Basic Materials", "profitTotal" : -9.190900000000001 }
{ "_id" : "Technology", "profitTotal" : -18.8968 }
{ "_id" : "Healthcare", "profitTotal" : -316.68649999999997 }
```

#### 5. Ordene as ações pelo profit e usando um cursor, liste as ações.

```
> var cursor = db.stocks.find({}, {_id: 0, Ticker: 1, Company: 1, "Profit Margin": 1}).sort({"Profit Margin": -1})
> cursor.next()
{
        "Ticker" : "BPT",
        "Profit Margin" : 0.994,
        "Company" : "BP Prudhoe Bay Royalty Trust"
}
> cursor.next()
{
        "Ticker" : "CACB",
        "Profit Margin" : 0.994,
        "Company" : "Cascade Bancorp"
}
> cursor.next()
{
        "Ticker" : "ROYT",
        "Profit Margin" : 0.99,
        "Company" : "Pacific Coast Oil Trust"
}
> cursor.count()
6756
```

#### 6. Renomeie o campo “Profit Margin” para apenas “profit”.

```
> db.stocks.updateMany({}, {$rename: {"Profit Margin": "profit"}})
{ "acknowledged" : true, "matchedCount" : 6756, "modifiedCount" : 4302 }
> db.stocks.find({"profit": {$exists: true}}).count()
4302
> db.stocks.find({"Profit Margin": {$exists: true}}).count()
0
```

#### 7. Agora liste apenas a empresa e seu respectivo resultado

```
> db.stocks.find({}, {Company: 1, profit: 1})
{ "_id" : ObjectId("52853800bb1177ca391c1802"), "Company" : "iShares MSCI AC Asia Information Tech" }
{ "_id" : ObjectId("52853800bb1177ca391c1801"), "Company" : "WCM/BNY Mellon Focused Growth ADR ETF" }
{ "_id" : ObjectId("52853800bb1177ca391c1803"), "Company" : "Altisource Asset Management Corporation" }
{ "_id" : ObjectId("52853800bb1177ca391c1800"), "Company" : "Alcoa, Inc.", "profit" : 0.013 }
{ "_id" : ObjectId("52853800bb1177ca391c17ff"), "Company" : "Agilent Technologies Inc.", "profit" : 0.137 }
{ "_id" : ObjectId("52853800bb1177ca391c1804"), "Company" : "Atlantic American Corp.", "profit" : 0.056 }
{ "_id" : ObjectId("52853800bb1177ca391c1806"), "Company" : "Applied Optoelectronics, Inc.", "profit" : -0.023 }
{ "_id" : ObjectId("52853800bb1177ca391c1805"), "Company" : "Aaron's, Inc.", "profit" : 0.06 }
{ "_id" : ObjectId("52853800bb1177ca391c1807"), "Company" : "AAON Inc.", "profit" : 0.105 }
{ "_id" : ObjectId("52853800bb1177ca391c1809"), "Company" : "Apple Inc.", "profit" : 0.217 }
{ "_id" : ObjectId("52853800bb1177ca391c180a"), "Company" : "American Assets Trust, Inc.", "profit" : 0.155 }
{ "_id" : ObjectId("52853800bb1177ca391c180b"), "Company" : "Almaden Minerals Ltd." }
{ "_id" : ObjectId("52853800bb1177ca391c1808"), "Company" : "Advance Auto Parts Inc.", "profit" : 0.063 }
{ "_id" : ObjectId("52853800bb1177ca391c180e"), "Company" : "iShares MSCI All Country Asia ex Jpn Idx" }
{ "_id" : ObjectId("52853800bb1177ca391c180c"), "Company" : "Advantage Oil & Gas Ltd.", "profit" : -0.232 }
{ "_id" : ObjectId("52853800bb1177ca391c180d"), "Company" : "Atlas Air Worldwide Holdings Inc.", "profit" : 0.071 }
{ "_id" : ObjectId("52853800bb1177ca391c180f"), "Company" : "AllianceBernstein Holding L.P.", "profit" : 0.896 }
{ "_id" : ObjectId("52853800bb1177ca391c1810"), "Company" : "Abaxis Inc.", "profit" : 0.1 }
{ "_id" : ObjectId("52853800bb1177ca391c1813"), "Company" : "AmerisourceBergen Corporation", "profit" : 0.005 }
{ "_id" : ObjectId("52853800bb1177ca391c1811"), "Company" : "ABB Ltd.", "profit" : 0.069 }
Type "it" for more

```

#### 8. Analise as ações. É uma bola de cristal na sua mão... Quais as três ações você investiria?

Considerei lucro e performance anual.

```
> db.stocks.find({}, {_id: 0, Ticker: 1, Company: 1, "Performance (Year)": 1, "profit": 1}).sort({profit:-1, "Performance (Year)": 1}).limit(3)
{ "Ticker" : "CACB", "Company" : "Cascade Bancorp", "Performance (Year)" : 0.0241, "profit" : 0.994 }
{ "Ticker" : "BPT", "Company" : "BP Prudhoe Bay Royalty Trust", "Performance (Year)" : 0.1837, "profit" : 0.994 }
{ "Ticker" : "ROYT", "Company" : "Pacific Coast Oil Trust", "Performance (Year)" : -0.1141, "profit" : 0.99 }
```

#### 9. Liste as ações agrupadas por setor

```
> db.stocks.aggregate([{$group: {_id: "$Sector", tickers: {$addToSet: "$Ticker"}, size: {$sum: 1}}},{$sort:{size: 1}}, {$limit: 2}])
{ "_id" : "Conglomerates", "tickers" : [ "QPAC", "PME", "MITSY", "HMTV", "HRG", "MWRX", "IEP", "LDL", "PBSK", "SAEX", "CACG", "ANDA", "AQU", "SPLP", "NC", "MMM", "EAGL", "ENT", "GDEF", "HTWO", "JACQ" ], "size" : 21 }
{ "_id" : "Utilities", "tickers" : [ "CZZ", "OTTR", "BKH", "ADGE", "NU", "ENI", "CWCO", "POR", "POM", "NGG", "UNS", "CWT", "AEE", "TAC", "OGE", "AMID", "UTL", "XEL", "TE", "EDE", "CPK", "HNP", "NVE", "EE", "DGAS", "CPN", "MSEX", "ARTNA", "WEC", "ELLO", "GAS", "ED", "SMLP", "NJR", "D", "AWK", "SRE", "BEP", "STR", "CNP", "SXE", "PNW", "KEP", "UGI", "PCG", "EBR", "PEG", "PNG", "SO", "SWX", "EQT", "PPL", "FCEL", "CLNE", "DTE", "NWE", "CDZI", "EGAS", "ITC", "PEGI", "LNT", "HTM", "AES", "MDU", "FE", "TRP", "PCYO", "NI", "OPTT", "SPH", "CORR", "TEG", "ATLS", "CHC", "SJI", "TGS", "PNY", "CIG", "WR", "SBS", "IDA", "LG", "ATO", "VVC", "ALE", "SCG", "BIP", "HE", "MGEE", "UIL", "DYN", "ELP", "NRG", "WTR", "CTWS", "APU", "AVA", "NYLD", "ORA", "YORW", "EXC", "CMS", "EDN", "GXP", "DUK", "AEP", "RGCO", "EOC", "NKA", "AWR", "JE", "OKE", "ETR", "AT", "SJW", "PAM", "EIX", "NEE", "WGL", "PNM", "FNRG", "CNL", "CPL", "NWN" ], "size" : 124 }
```

### Exercício 3 – Fraude na Enron!

#### 1. Liste as pessoas que enviaram e-mails (de forma distinta, ou seja, sem repetir). Quantas pessoas são?

```
> db.enron.aggregate([{$group: {_id: "$sender", sent: {$sum : 1}}}, {$group: {_id: "result", count: {$sum: "$sent"}}}])
{ "_id" : "result", "count" : 5929 }
```

#### 2. Contabilize quantos e-mails tem a palavra “fraud”

```
> db.enron.aggregate([{$match:{text: {$regex: ".*fraud.*"}}}, {$group: {_id: "frauds", count: {$sum: 1}}} ])
{ "_id" : "frauds", "count" : 23 }

ou

> db.enron.find({text: {$regex: ".*fraud.*"}}, {_id: 0, text: 1}).count()
23
```
