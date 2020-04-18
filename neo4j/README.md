# Exercícios Neo4j

## Exercício 1- Retrieving Nodes
Coloque os comandos utilizado em cada item a seguir:

Exercise 1.1: Retrieve all nodes from the database.
![](1.1.png)
Exercise 1.2: Examine the data model for the graph.
![](1.2.png)
Exercise 1.3: Retrieve all Person nodes.
![](1.3.png)
Exercise 1.4: Retrieve all Movie nodes.
![](1.4.png)

## Exercício 2 – Filtering queries using property values
Coloque os comandos utilizado em cada item a seguir:
Exercise 2.1: Retrieve all movies that were released in a specific year.
![](2.1e2.png)
Exercise 2.2: View the retrieved results as a table.
![](2.1e2.png)
Exercise 2.3: Query the database for all property keys.
![](2.3.png)
Exercise 2.4: Retrieve all Movies released in a specific year, returning their titles.
![](2.4.png)
Exercise 2.5: Display title, released, and tagline values for every Movie node in the graph.
![](2.5.png)
Exercise 2.6: Display more user-friendly headers in the table
![](2.6.png)

## Exercício 3 - Filtering queries using relationships
Coloque os comandos utilizado em cada item a seguir:

Exercise 3.1: Display the schema of the database.
![](3.1.png)
Exercise 3.2: Retrieve all people who wrote the movie Speed Racer.
![](3.2.png)
Exercise 3.3: Retrieve all movies that are connected to the person, Tom Hanks.
![](3.3.png)
Exercise 3.4: Retrieve information about the relationships Tom Hanks had with the set of movies retrieved earlier.
![](3.4.png)
Exercise 3.5: Retrieve information about the roles that Tom Hanks acted in.
![](3.5.png)

## Exercício 4 – Filtering queries using WHERE clause

Coloque os comandos utilizado em cada item a seguir:

Exercise 4.1: Retrieve all movies that Tom Cruise acted in.
![](4.1.png)
Exercise 4.2: Retrieve all people that were born in the 70’s.
![](4.2.png)
Exercise 4.3: Retrieve the actors who acted in the movie The Matrix who were born after 1960.
![](4.3.png)
Exercise 4.4: Retrieve all movies by testing the node label and a property.
![](4.4.png)
Exercise 4.5: Retrieve all people that wrote movies by testing the relationship between two nodes.
![](4.5.png)
Exercise 4.6: Retrieve all people in the graph that do not have a property.
![](4.6.png)
Exercise 4.7: Retrieve all people related to movies where the relationship has a property.
![](4.7.png)
Exercise 4.8: Retrieve all actors whose name begins with James.
![](4.8.png)
Exercise 4.9: Retrieve all all REVIEW relationships from the graph with filtered results.
![](4.9.png)
Exercise 4.10: Retrieve all people who have produced a movie, but have not directed a movie.
![](4.10.png)
Exercise 4.11: Retrieve the movies and their actors where one of the actors also directed the movie.
![](4.11.png)
Exercise 4.12: Retrieve all movies that were released in a set of years.
![](4.12.png)
Exercise 4.13: Retrieve the movies that have an actor’s role that is the name of the movie.
![](4.13.png)

Exercício 5 – Controlling query processing

Coloque os comandos utilizado em cada item a seguir:

Exercise 5.1: Retrieve data using multiple MATCH patterns.
![](5.1.png)
Exercise 5.2: Retrieve particular nodes that have a relationship.
![](5.2.png)
Exercise 5.3: Modify the query to retrieve nodes that are exactly three hops away.
![](5.3.png)
Exercise 5.4: Modify the query to retrieve nodes that are one and two hops away.
![](5.4.png)
Exercise 5.5: Modify the query to retrieve particular nodes that are connected no matter how many hops are required.
![](5.5.png)
Exercise 5.6: Specify optional data to be retrieved during the query.
![](5.6.png)
Exercise 5.7: Retrieve nodes by collecting a list.
![](5.7.png)
Exercise 5.8: Retrieve all movies that Tom Cruise has acted in and the co-actors that acted in the same movie by collecting a list
![](5.7.png)
Exercise 5.9: Retrieve nodes as lists and return data associated with the corresponding lists.
![](5.9.png)
Exercise 5.10: Retrieve nodes and their relationships as lists.
![](5.10.png)
Exercise 5.11: Retrieve the actors who have acted in exactly five movies.
![](5.11.png)
Exercise 5.12: Retrieve the movies that have at least 2 directors with other optional data.
![](5.12.png)

## Exercício 6 – Controlling results returned

Coloque os comandos utilizado em cada item a seguir:

Exercise 6.1: Execute a query that returns duplicate records.
![](6.1.png)
Exercise 6.2: Modify the query to eliminate duplication.
![](6.2.png)
Exercise 6.3: Modify the query to eliminate more duplication.
![](6.3.png)
Exercise 6.4: Sort results returned.
![](6.4.png)
Exercise 6.5: Retrieve the top 5 ratings and their associated movies.
![](6.5.png)
Exercise 6.6: Retrieve all actors that have not appeared in more than 3 movies.
![](6.6.png)

## Exercício 7 – Working with cypher data

Coloque os comandos utilizado em cada item a seguir:

Exercise 7.1: Collect and use lists.
![](7.1.png)
Exercise 7.2: Collect a list.
![](7.2.png)
Exercise 7.3: Unwind a list.
![](7.3.png)
Exercise 7.4: Perform a calculation with the date type.
![](7.4.png)

## Exercício 8 – Creating nodes

Coloque os comandos utilizado em cada item a seguir:

Exercise 8.1: Create a Movie node.
![](8.1.png)
Exercise 8.2: Retrieve the newly-created node.
![](8.2.png)
Exercise 8.3: Create a Person node.
![](8.3.png)
Exercise 8.4: Retrieve the newly-created node.
![](8.4.png)
Exercise 8.5: Add a label to a node.
![](8.5.png)
Exercise 8.6: Retrieve the node using the new label.
![](8.6.png)
Exercise 8.7: Add the Female label to selected nodes.
![](8.7.png)
Exercise 8.8: Retrieve all Female nodes.
![](8.8.png)
Exercise 8.9: Remove the Female label from the nodes that have this label.
![](8.9.png)
Exercise 8.10: View the current schema of the graph.
![](8.10.png)
Exercise 8.11: Add properties to a movie.
![](8.11.png)
Exercise 8.12: Retrieve an OlderMovie node to confirm the label and properties.
![](8.12.png)
Exercise 8.13: Add properties to the person, Robin Wright.
![](8.13.png)
Exercise 8.14: Retrieve an updated Person node.
![](8.14.png)
Exercise 8.15: Remove a property from a Movie node.
![](8.15.png)
Exercise 8.16: Retrieve the node to confirm that the property has been removed.
![](8.16.png)
Exercise 8.17: Remove a property from a Person node.
![](8.17.png)
Exercise 8.18: Retrieve the node to confirm that the property has been removed.
![](8.18.png)

## Exercício 9 – Creating relationships

Coloque os comandos utilizado em cada item a seguir:

Exercise 9.1: Create ACTED_IN relationships.
![](9.1.png)
Exercise 9.2: Create DIRECTED relationships.
![](9.2.png)
Exercise 9.3: Create a HELPED relationship.
![](9.3.png)
Exercise 9.4: Query nodes and new relationships.
![](9.4.png)
Exercise 9.5: Add properties to relationships.
![](9.5.png)
Exercise 9.6: Add a property to the HELPED relationship.
![](9.6.png)
Exercise 9.7: View the current list of property keys in the graph.
![](9.7.png)
Exercise 9.8: View the current schema of the graph.
![](9.8.png)
Exercise 9.9: Retrieve the names and roles for actors.
![](9.9.png)
Exercise 9.10: Retrieve information about any specific relationships.
![](9.10.png)
Exercise 9.11: Modify a property of a relationship.
![](9.11.png)
Exercise 9.12: Remove a property from a relationship.
![](9.12.png)
Exercise 9.13: Confirm that your modifications were made to the graph.
![](9.13.png)

## Exercício 10 – Deleting nodes and relationships

Coloque os comandos utilizado em cada item a seguir:

Exercise 10.1: Delete a relationship.
![](10.1.png)
Exercise 10.2: Confirm that the relationship has been deleted.
![](10.2.png)
Exercise 10.3: Retrieve a movie and all of its relationships.
![](10.3.png)
Exercise 10.4: Try deleting a node without detaching its relationships.
![](10.4.png)
Exercise 10.5: Delete a Movie node, along with its relationships.
![](10.5.png)
Exercise 10.6: Confirm that the Movie node has been deleted.
![](10.6.png)

> Pedro Lacerda :coffee: