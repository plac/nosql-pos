## HBase

### Exercício

#### Procedimentos

##### 1. Crie a tabela com 2 famílias de colunas:

```
hbase(main):004:0> create_namespace 'main'
Took 0.2283 seconds                                                                                                                                       
hbase(main):005:0> create 'main:italians', 'personal-data', 'professional-data'
Created table main:italians
Took 0.7488 seconds                                                                                                                                       
=> Hbase::Table - main:italians
```

##### 2. Importe o arquivo via linha de comando

```
root@f61c32261ec1:/# hbase shell /seed/italians.txt 
2020-04-26 22:12:17,754 WARN  [main] util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Took 0.3557 seconds                                                                                                                                       
Took 0.0034 seconds                                                                                                                                       
Took 0.0039 seconds                                                                                                                                       
Took 0.0039 seconds                                                                                                                                  
...
```

#### Operações

##### 1. Adicione mais 2 italianos mantendo adicionando informações como data de nascimento nas informações pessoais e um atributo de anos de experiência nas informações profissionais;

```
hbase(main):011:0> put 'italians', 11, 'personal-data:birth-date', '1990-10-01'
Took 0.0343 seconds                                                                                                                                       
hbase(main):012:0> put 'italians', 11, 'professional-data:experience', 6
Took 0.0056 seconds                                                                                                                                       
hbase(main):013:0> put 'italians', 11, 'personal-data:name', 'Vincenzo Palmieri'
Took 0.0028 seconds                                                                                                                                       
hbase(main):014:0> put 'italians', 11, 'personal-data:city', 'Palermo'
Took 0.0035 seconds                                                                                                                                       
hbase(main):015:0> put 'italians', 11, 'professional-data:role', 'Chef'
Took 0.0031 seconds                                                                                                                                       
hbase(main):016:0> put 'italians', 11, 'professional-data:salary', 80000
Took 0.0030 seconds   

hbase(main):018:0> put 'italians', 12, 'personal-data:name', 'Monalisa Totti'
Took 0.0037 seconds                                                                                                                          
hbase(main):021:0> put 'italians', 12, 'personal-data:city', 'Veneza'
Took 0.0045 seconds                                                                                                                                       
hbase(main):022:0> put 'italians', 12, 'personal-data:birth-date', '2000-12-8'
Took 0.0030 seconds                                                                                                                                       
hbase(main):023:0> put 'italians', 12, 'professional-data:role', 'Architect'
Took 0.0053 seconds                                                                                                                                       
hbase(main):024:0> put 'italians', 12, 'professional-data:salary', '85000'
Took 0.0036 seconds                                                                                                                                       
hbase(main):025:0> put 'italians', 12, 'professional-data:salary', 85000
Took 0.0032 seconds                                                                                                                                       
hbase(main):026:0> put 'italians', 12, 'professional-data:experience', 3
Took 0.0034 seconds                                                          
```

##### 2. Adicione o controle de 5 versões na tabela de dados pessoais.

```
hbase(main):028:0> alter 'italians', NAME => 'personal-data', VERSIONS => 5
Updating all regions with the new schema...
1/1 regions updated.
Done.
Took 1.7676 seconds   
```

##### 3. Faça 5 alterações em um dos italianos;

```
hbase(main):029:0> put 'italians', 11, 'personal-data:city', 'Roma'
Took 0.0061 seconds                                                                                                                                       
hbase(main):030:0> put 'italians', 11, 'personal-data:city', 'Monza'
Took 0.0037 seconds                                                                                                                                       
hbase(main):031:0> put 'italians', 11, 'personal-data:city', 'Florence'
Took 0.0031 seconds                                                                                                                                       
hbase(main):032:0> put 'italians', 11, 'personal-data:city', 'Napoli'
Took 0.0036 seconds                                                                                                                                       
hbase(main):033:0> put 'italians', 11, 'personal-data:city', 'Milano'
Took 0.0033 seconds    
```

##### 4. Com o operador get, verifique como o HBase armazenou o histórico.

```
hbase(main):035:0> get 'italians', '11', { COLUMN=>'personal-data:city', VERSIONS=>5 }
COLUMN                                  CELL                                                                                                              
 personal-data:city                     timestamp=1587941259397, value=Milano                                                                             
 personal-data:city                     timestamp=1587941246588, value=Napoli                                                                             
 personal-data:city                     timestamp=1587941235989, value=Florence                                                                           
 personal-data:city                     timestamp=1587941220514, value=Monza                                                                              
 personal-data:city                     timestamp=1587941209105, value=Roma                                                                               
1 row(s)
Took 0.0099 seconds 
```

##### 5. Utilize o scan para mostrar apenas o nome e profissão dos italianos.

```
hbase(main):036:0> scan 'italians', { COLUMNS => ['personal-data:name', 'professional-data:role']}
ROW                                     COLUMN+CELL                                                                                                       
 1                                      column=personal-data:name, timestamp=1587939138569, value=Paolo Sorrentino                                        
 1                                      column=professional-data:role, timestamp=1587939138614, value=Gestao Comercial                                    
 10                                     column=personal-data:name, timestamp=1587939138861, value=Giovanna Caputo                                         
 10                                     column=professional-data:role, timestamp=1587939138879, value=Comunicacao Institucional                           
 11                                     column=personal-data:name, timestamp=1587939600614, value=Vincenzo Palmieri                                       
 11                                     column=professional-data:role, timestamp=1587939637488, value=Chef                                                
 12                                     column=personal-data:name, timestamp=1587939714873, value=Monalisa Totti                                          
 12                                     column=professional-data:role, timestamp=1587939822332, value=Architect                                           
 2                                      column=personal-data:name, timestamp=1587939138624, value=Domenico Barbieri                                       
 2                                      column=professional-data:role, timestamp=1587939138650, value=Psicopedagogia                                      
 3                                      column=personal-data:name, timestamp=1587939138659, value=Maria Parisi                                            
 3                                      column=professional-data:role, timestamp=1587939138668, value=Optometria                                          
 4                                      column=personal-data:name, timestamp=1587939138689, value=Silvia Gallo                                            
 4                                      column=professional-data:role, timestamp=1587939138698, value=Engenharia Industrial Madeireira                    
 5                                      column=personal-data:name, timestamp=1587939138718, value=Rosa Donati                                             
 5                                      column=professional-data:role, timestamp=1587939138729, value=Mecatronica Industrial                              
 6                                      column=personal-data:name, timestamp=1587939138752, value=Simone Lombardo                                         
 6                                      column=professional-data:role, timestamp=1587939138764, value=Biotecnologia e Bioquimica                          
 7                                      column=personal-data:name, timestamp=1587939138781, value=Barbara Ferretti                                        
 7                                      column=professional-data:role, timestamp=1587939138797, value=Libras                                              
 8                                      column=personal-data:name, timestamp=1587939138808, value=Simone Ferrara                                          
 8                                      column=professional-data:role, timestamp=1587939138822, value=Engenharia de Minas                                 
 9                                      column=personal-data:name, timestamp=1587939138833, value=Vincenzo Giordano                                       
 9                                      column=professional-data:role, timestamp=1587939138848, value=Marketing                                           
12 row(s)
Took 0.0458 seconds  
```

##### 6. Apague os italianos com row id ímpar

```
hbase(main):038:0> deleteall 'italians', 1
Took 0.0035 seconds                                                                                                                                       
hbase(main):039:0> deleteall 'italians', 3
Took 0.0031 seconds                                                                                                                                       
hbase(main):040:0> deleteall 'italians', 5
Took 0.0033 seconds                                                                                                                                       
hbase(main):041:0> deleteall 'italians', 7
Took 0.0029 seconds 

hbase(main):042:0> deleteall 'italians', 9
Took 0.0033 seconds 

hbase(main):043:0> deleteall 'italians', 11
Took 0.0024 seconds 
```

##### 7. Crie um contador de idade 55 para o italiano de row id 5

```
hbase(main):017:0> incr 'italians', 5, 'personal-data:age', 55
COUNTER VALUE = 55
Took 0.0051 seconds    
```

##### 8. Incremente a idade do italiano em 1

```
hbase(main):018:0> incr 'italians', 5, 'personal-data:age', 1
COUNTER VALUE = 56
Took 0.0070 seconds    
```

### Exercício MapReduce:

Foi criado o arquivo `gen-italians.js` baseado no `italians.js` do mongodb, executando ele é criado o arquivo `generated-italians.txt` que serve de entrada para o hbase. Importando no container:

> docker-compose exec hbase bash

```
hbase shell seed/generated-italians.txt
...

```

#### 1. Quantidade de gatos e cachorros na amostra

```

```

#### 2. Média de gatos e cachorros na população
#### 3. Quantidade de pais e mães
#### 4. Média de pais e mães
#### 5. Média de frutas e filmes por italiano
#### 6. Salário médio dos italianos