# CastingAgency


Introduction and Motivation
---------------------------
The App constitutes the capstone project of the Udacity course "Full Stack Web Developer". The Casting Agency app is the tool for a company which creates movies and 
assigns actors to these movies.


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


url
---
The api is located at Heroku at:
https://ud-agency.herokuapp.com/ 


dependencies
------------
pip install -r requirements.txt


backend
-------

/datatabse
createdb agency
psql agency < agency.psql



#Testing
#--------
API tests are conducted by two ways:
1) via Postman (see exported requests)
2) via unittest in test_app.py

1)

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
Login is at ....
Sign up to receive token

Auth0 Domain name: py1150.eu.auth0.com
JWT secret: LU0wdilfit94XeL8KYeAnUN-312Xf-NBzA5AY8G5ep1ZYxoMDWCnEJAdCm5l9Rgm
Auth0 ClientID: EeYJIGaf3frKfj1nRwclF8nA9N88wYpz


development server
------------------


frontend
--------

image
source:
<span>Photo by <a href="https://unsplash.com/@felixmooneeram?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Felix Mooneeram</a> on <a href="https://unsplash.com/s/photos/movie?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>



