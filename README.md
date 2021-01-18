# CastingAgency


Introduction and Motivation
---------------------------
The App constitutes the capstone project of the Udacity course "Full Stack Web Developer". The Casting Agency app is the tool for a company which creates movies and 
assigns actors to these movies.



url
---
The api is located at Heroku at:
https://ud-agency.herokuapp.com/ 


API behavior
------------
/actors
methods = ['GET']: list all entries
methods = ['POST']: insert a new entry
/actors/<int:id>
methods = ['DEL']: delete an entry with specific id
methods = ['PATCH']: update an enry with specific id

/movies
methods = ['GET']: list all entries
methods = ['POST']: insert a new entry
/movies/<int:id>
methods = ['DEL']: delete an entry with specific id
methods = ['PATCH']: update an enry with specific id



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



Testing
--------
API tests are conducted by two ways:
1) via Postman (see exported requests)
2) via unittest in test_app.py

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

/backend/starter
python test_app.py

Roles: Tests are executed as Executive Producer
```

authentication
---------------
Login is at:
https://py1150.eu.auth0.com/authorize?audience=agency&response_type=token&client_id=EeYJIGaf3frKfj1nRwclF8nA9N88wYpz&redirect_uri=http://localhost:3000/user

Auth0 Domain name: py1150.eu.auth0.com
JWT secret: LU0wdilfit94XeL8KYeAnUN-312Xf-NBzA5AY8G5ep1ZYxoMDWCnEJAdCm5l9Rgm
Auth0 ClientID: EeYJIGaf3frKfj1nRwclF8nA9N88wYpz


Roles:
------
Casting Assistant:
Can view actors and movies

Casting Director:
All permissions a Casting Assistant has and…
Add or delete an actor from the database
Modify actors or movies

Executive Producer:
All permissions a Casting Director has and…
Add or delete a movie from the database

