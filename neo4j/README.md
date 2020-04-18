# Exercícios Neo4j

## Exercício 1- Retrieving Nodes
Coloque os comandos utilizado em cada item a seguir:

Exercise 1.1: Retrieve all nodes from the database.
![](imgs/1.1.png)
Exercise 1.2: Examine the data model for the graph.
![](imgs/1.2.png)
Exercise 1.3: Retrieve all Person nodes.
![](imgs/1.3.png)
Exercise 1.4: Retrieve all Movie nodes.
![](imgs/1.4.png)

## Exercício 2 – Filtering queries using property values
Coloque os comandos utilizado em cada item a seguir:
Exercise 2.1: Retrieve all movies that were released in a specific year.
![](imgs/2.1e2.png)
Exercise 2.2: View the retrieved results as a table.
![](imgs/2.1e2.png)
Exercise 2.3: Query the database for all property keys.
![](imgs/2.3.png)
Exercise 2.4: Retrieve all Movies released in a specific year, returning their titles.
![](imgs/2.4.png)
Exercise 2.5: Display title, released, and tagline values for every Movie node in the graph.
![](imgs/2.5.png)
Exercise 2.6: Display more user-friendly headers in the table
![](imgs/2.6.png)

## Exercício 3 - Filtering queries using relationships
Coloque os comandos utilizado em cada item a seguir:

Exercise 3.1: Display the schema of the database.
![](imgs/3.1.png)
Exercise 3.2: Retrieve all people who wrote the movie Speed Racer.
![](imgs/3.2.png)
Exercise 3.3: Retrieve all movies that are connected to the person, Tom Hanks.
![](imgs/3.3.png)
Exercise 3.4: Retrieve information about the relationships Tom Hanks had with the set of movies retrieved earlier.
![](imgs/3.4.png)
Exercise 3.5: Retrieve information about the roles that Tom Hanks acted in.
![](imgs/3.5.png)

## Exercício 4 – Filtering queries using WHERE clause

Coloque os comandos utilizado em cada item a seguir:

Exercise 4.1: Retrieve all movies that Tom Cruise acted in.
![](imgs/4.1.png)
Exercise 4.2: Retrieve all people that were born in the 70’s.
![](imgs/4.2.png)
Exercise 4.3: Retrieve the actors who acted in the movie The Matrix who were born after 1960.
![](imgs/4.3.png)
Exercise 4.4: Retrieve all movies by testing the node label and a property.
![](imgs/4.4.png)
Exercise 4.5: Retrieve all people that wrote movies by testing the relationship between two nodes.
![](imgs/4.5.png)
Exercise 4.6: Retrieve all people in the graph that do not have a property.
![](imgs/4.6.png)
Exercise 4.7: Retrieve all people related to movies where the relationship has a property.
![](imgs/4.7.png)
Exercise 4.8: Retrieve all actors whose name begins with James.
![](imgs/4.8.png)
Exercise 4.9: Retrieve all all REVIEW relationships from the graph with filtered results.
![](imgs/4.9.png)
Exercise 4.10: Retrieve all people who have produced a movie, but have not directed a movie.
![](imgs/4.10.png)
Exercise 4.11: Retrieve the movies and their actors where one of the actors also directed the movie.
![](imgs/4.11.png)
Exercise 4.12: Retrieve all movies that were released in a set of years.
![](imgs/4.12.png)
Exercise 4.13: Retrieve the movies that have an actor’s role that is the name of the movie.
![](imgs/4.13.png)

Exercício 5 – Controlling query processing

Coloque os comandos utilizado em cada item a seguir:

Exercise 5.1: Retrieve data using multiple MATCH patterns.
![](imgs/5.1.png)
Exercise 5.2: Retrieve particular nodes that have a relationship.
![](imgs/5.2.png)
Exercise 5.3: Modify the query to retrieve nodes that are exactly three hops away.
![](imgs/5.3.png)
Exercise 5.4: Modify the query to retrieve nodes that are one and two hops away.
![](imgs/5.4.png)
Exercise 5.5: Modify the query to retrieve particular nodes that are connected no matter how many hops are required.
![](imgs/5.5.png)
Exercise 5.6: Specify optional data to be retrieved during the query.
![](imgs/5.6.png)
Exercise 5.7: Retrieve nodes by collecting a list.
![](imgs/5.7.png)
Exercise 5.8: Retrieve all movies that Tom Cruise has acted in and the co-actors that acted in the same movie by collecting a list
![](imgs/5.7.png)
Exercise 5.9: Retrieve nodes as lists and return data associated with the corresponding lists.
![](imgs/5.9.png)
Exercise 5.10: Retrieve nodes and their relationships as lists.
![](imgs/5.10.png)
Exercise 5.11: Retrieve the actors who have acted in exactly five movies.
![](imgs/5.11.png)
Exercise 5.12: Retrieve the movies that have at least 2 directors with other optional data.
![](imgs/5.12.png)

## Exercício 6 – Controlling results returned

Coloque os comandos utilizado em cada item a seguir:

Exercise 6.1: Execute a query that returns duplicate records.
![](imgs/6.1.png)
Exercise 6.2: Modify the query to eliminate duplication.
![](imgs/6.2.png)
Exercise 6.3: Modify the query to eliminate more duplication.
![](imgs/6.3.png)
Exercise 6.4: Sort results returned.
![](imgs/6.4.png)
Exercise 6.5: Retrieve the top 5 ratings and their associated movies.
![](imgs/6.5.png)
Exercise 6.6: Retrieve all actors that have not appeared in more than 3 movies.
![](imgs/6.6.png)

## Exercício 7 – Working with cypher data

Coloque os comandos utilizado em cada item a seguir:

Exercise 7.1: Collect and use lists.
![](imgs/7.1.png)
Exercise 7.2: Collect a list.
![](imgs/7.2.png)
Exercise 7.3: Unwind a list.
![](imgs/7.3.png)
Exercise 7.4: Perform a calculation with the date type.
![](imgs/7.4.png)

## Exercício 8 – Creating nodes

Coloque os comandos utilizado em cada item a seguir:

Exercise 8.1: Create a Movie node.
![](imgs/8.1.png)
Exercise 8.2: Retrieve the newly-created node.
![](imgs/8.2.png)
Exercise 8.3: Create a Person node.
![](imgs/8.3.png)
Exercise 8.4: Retrieve the newly-created node.
![](imgs/8.4.png)
Exercise 8.5: Add a label to a node.
![](imgs/8.5.png)
Exercise 8.6: Retrieve the node using the new label.
![](imgs/8.6.png)
Exercise 8.7: Add the Female label to selected nodes.
![](imgs/8.7.png)
Exercise 8.8: Retrieve all Female nodes.
![](imgs/8.8.png)
Exercise 8.9: Remove the Female label from the nodes that have this label.
![](imgs/8.9.png)
Exercise 8.10: View the current schema of the graph.
![](imgs/8.10.png)
Exercise 8.11: Add properties to a movie.
![](imgs/8.11.png)
Exercise 8.12: Retrieve an OlderMovie node to confirm the label and properties.
![](imgs/8.12.png)
Exercise 8.13: Add properties to the person, Robin Wright.
![](imgs/8.13.png)
Exercise 8.14: Retrieve an updated Person node.
![](imgs/8.14.png)
Exercise 8.15: Remove a property from a Movie node.
![](imgs/8.15.png)
Exercise 8.16: Retrieve the node to confirm that the property has been removed.
![](imgs/8.16.png)
Exercise 8.17: Remove a property from a Person node.
![](imgs/8.17.png)
Exercise 8.18: Retrieve the node to confirm that the property has been removed.
![](imgs/8.18.png)

## Exercício 9 – Creating relationships

Coloque os comandos utilizado em cada item a seguir:

Exercise 9.1: Create ACTED_IN relationships.
![](imgs/9.1.png)
Exercise 9.2: Create DIRECTED relationships.
![](imgs/9.2.png)
Exercise 9.3: Create a HELPED relationship.
![](imgs/9.3.png)
Exercise 9.4: Query nodes and new relationships.
![](imgs/9.4.png)
Exercise 9.5: Add properties to relationships.
![](imgs/9.5.png)
Exercise 9.6: Add a property to the HELPED relationship.
![](imgs/9.6.png)
Exercise 9.7: View the current list of property keys in the graph.
![](imgs/9.7.png)
Exercise 9.8: View the current schema of the graph.
![](imgs/9.8.png)
Exercise 9.9: Retrieve the names and roles for actors.
![](imgs/9.9.png)
Exercise 9.10: Retrieve information about any specific relationships.
![](imgs/9.10.png)
Exercise 9.11: Modify a property of a relationship.
![](imgs/9.11.png)
Exercise 9.12: Remove a property from a relationship.
![](imgs/9.12.png)
Exercise 9.13: Confirm that your modifications were made to the graph.
![](imgs/9.13.png)

## Exercício 10 – Deleting nodes and relationships

Coloque os comandos utilizado em cada item a seguir:

Exercise 10.1: Delete a relationship.
![](imgs/10.1.png)
Exercise 10.2: Confirm that the relationship has been deleted.
![](imgs/10.2.png)
Exercise 10.3: Retrieve a movie and all of its relationships.
![](imgs/10.3.png)
Exercise 10.4: Try deleting a node without detaching its relationships.
![](imgs/10.4.png)
Exercise 10.5: Delete a Movie node, along with its relationships.
![](imgs/10.5.png)
Exercise 10.6: Confirm that the Movie node has been deleted.
![](imgs/10.6.png)

> Pedro Lacerda :coffee: