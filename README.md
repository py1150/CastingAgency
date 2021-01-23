# CastingAgency


Introduction and Motivation
---------------------------
The App constitutes the capstone project of the Udacity course "Full Stack Web Developer". The Casting Agency app is the tool for a company which creates movies and assigns actors to these movies.

I developed this project to create a base application which integrates fundamental web development building blocks which were taught in this course. They include:
- set-up of a database
- development of an API which is able to provide data and process received data by the use of different request methods
- deployment to a production system
- creation of an accompanying readme


url
---
The api is located at Heroku at:
https://ud-agency.herokuapp.com/ 



ENDPOINT DOCUMENTATION
----------------------
```

Endpoints
GET '/actors'
GET '/movies'
POST '/actors'
POST '/movies'
PATCH '/actors/<id>'
PATCH '/movies/<id>'
DELETE '/actors/<id>'
DELETE '/movies/<id>'


GET '/actors'
- Fetches a nested dictionary of with request status and actors data 
- within the data value there is a list of dictionaries with data for each actor in which the keys are the data category and the value is the corresponding value of the information
- Request Arguments: None
- Returns: An object of information category: content key:value pairs. 
{"actors":[
    {"date_birth":"Thu, 25 Apr 1940 00:00:00 GMT",           "gender":"male",
    "id":2,
    "name":"Al Pacino"}],
"success":true}

GET '/movies'
- Fetches a nested dictionary of with request status and movies data 
- within the data value there is a list of dictionaries with data for each movie in which the keys are the data category and the value is the corresponding value of the information
- Request Arguments: None
- Returns: An object of information category: content key:value pairs. 
{"movies":[
    {"actor_id":1,
    "description":"Crime movie",
    "id":2,"release_date":
    "Fri, 24 Mar 1972 00:00:00 GMT","title":"The Godfather"}]    
"success":true}


POST '/actors'
- Inserts a new actor by providing a dictionary. The structure
follows the description above (see GET 'actors')
{
    "name":"Al Pacino",
    "date_birth":"1940-04-25",
    "gender":"male"
}
- Request Arguments: None
- Returns: upon success a 201 status and the inserted dictionary or  upon error a 422 status


POST '/movies'
- Inserts a new movie by providing a dictionary. The structure
follows the description above (see GET 'movies')
{
    "title":"The Godfather",
    "release_date":"1972-03-24",
    "description":"Crime movie",
    "actor_id":1
}
- Request Arguments: None
- Returns: upon success a 201 status and the inserted dictionary or  upon error a 422 status


PATCH '/actors/<id>'
- Updates the data of a specific actor by providing a dictionary with data to be updated. The structure
follows the description above (see GET 'actors')
{
    "name":"Al Pacino",
    "date_birth":"1940-04-25",
    "gender":"male"
}
- Request Arguments: <id> id of the actor 
- Returns: upon success a 200 status and the deleted dictionary or  upon error a 400 status if values could not be inserted into the database, a 404 status if the actor does not exist


PATCH '/movies/<id>'
- Updates the data of a specific movie by providing a dictionary with data to be updated. The structure
follows the description above (see GET 'actors')
{
    "title":"The Godfather",
    "release_date":"1972-03-24",
    "description":"Crime movie",
    "actor_id":1
}
- Request Arguments: <id> id of the movie 
- Returns: upon success a 200 status and the deleted dictionary or  upon error a 400 status if values could not be inserted into the database, a 404 status if the movie does not exist


DELETE '/actors/<id>'
- Deletes the data of a specific actor 
- Request Arguments: <id> id of the actor 
- Returns: upon success a 200 status and the deleted dictionary or  upon error a 400 status if values could not be inserted into the database, a 404 status if the actor does not exist


DELETE '/movies/<id>'
- Deletes the data of a specific actor 
- Request Arguments: <id> id of the actor 
- Returns: upon success a 200 status and the deleted dictionary or  upon error a 400 status if values could not be inserted into the database, a 404 status if the movie does not exist

```



dependencies
------------
pip install -r requirements.txt


Database
-------

Database local:
/datatabse
createdb agency
psql agency < agency.psql

Database deployed:
models.py --> database_path
/database
heroku pg:psql --app ud-agency<agency.psql


RBAC:
------
Casting Assistant:<br/>
Can view actors and movies

Casting Director:<br/>
All permissions a Casting Assistant has and…<br/>
Add or delete an actor from the database<br/>
Modify actors or movies

Executive Producer:<br/>
All permissions a Casting Director has and…<br/>
Add or delete a movie from the database




Testing
--------
API tests are conducted by two ways:
1: via Postman (see exported requests)
2: via unittest in test_app.py

1)
backend/starter
gency.postman_collection_local.json
gency.postman_collection_deployed.json

2)
To run the tests, run
```
/backend/starter/database
dropdb agency_test
createdb trivia_test
psql agency_test < agency.psql
```

```
/backend/starter
python test_app.py
```



authentication
---------------
Login is at:
https://py1150.eu.auth0.com/authorize?audience=agency&response_type=token&client_id=EeYJIGaf3frKfj1nRwclF8nA9N88wYpz&redirect_uri=http://localhost:3000/user

Auth0 Domain name: py1150.eu.auth0.com
JWT secret: LU0wdilfit94XeL8KYeAnUN-312Xf-NBzA5AY8G5ep1ZYxoMDWCnEJAdCm5l9Rgm
Auth0 ClientID: EeYJIGaf3frKfj1nRwclF8nA9N88wYpz


