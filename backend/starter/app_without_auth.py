import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from database.models import db_drop_and_create_all, setup_db, Movie, Actor
from auth.auth import AuthError, requires_auth

import json
import pdb


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  return app

APP = create_app()


# added for CORS
@APP.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers','Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Headers','GET, POST, PATCH, DELETE, OPTIONS')
    return response


'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''
#db_drop_and_create_all()


## ROUTES
'''
@TODO implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''

"""
GET
"""

@APP.route('/actors', methods= ['GET'])
def display_all_actors():
    query = Actor.query.all()

    if query==None:
        abort(404)
    else:
        #define output
        output = {}
        output['success']=True
        output['actors']=[actor.long() for actor in query]

        return jsonify(output), 200

@APP.route('/movies', methods= ['GET'])
def display_all_movies():

    query = Movie.query.all()

    if query==None:
        abort(404)
    else:
        #define output
        output = {}
        output['success']=True
        output['movies']=[movie.long() for movie in query]

        return jsonify(output), 200

'''
@TODO implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''

"""
@app.route('/drinks-detail', methods= ['GET'])
#@requires_auth('get:drinks-detail')
def display_all_drinks_detail(payload):
    drink_query = Drink.query.all()

    if drink_query==None:
        abort(404)
    else:
        #define output
        output = {}
        output['success']=True
        output['drinks']=[drink.long() for drink in drink_query]

        return jsonify(output), 200
"""
"""
INSERT
"""

@APP.route('/movies', methods = ['POST'])
#@requires_auth('post:movies')
#def insert_movie(payload):
def insert_movie():  

    # content of post request  
    result_dict = request.get_json()
    title = result_dict['title']
    release_date = result_dict['release_date']
    description = result_dict['description']
    actor_id = result_dict['actor_id']

    # instantiate new movie object
    movie = Movie(title=title,\
                  description=description,\
                  release_date=release_date,\
                  actor_id=actor_id)    

    # insert to database 
    try:
        movie.insert()
        return jsonify({'sucess':True,'movie':movie.long()}),201
    except:
        abort(422)


@APP.route('/actors', methods = ['POST'])
#@requires_auth('post:actors')
#def insert_movie(payload):
def insert_actor():

    # content of post request  
    result_dict = request.get_json()
    name = result_dict['name']
    date_birth = result_dict['date_birth']
    gender = result_dict['gender']

    # instantiate new actor object
    actor = Actor(name=name,\
                  date_birth=date_birth,\
                  gender=gender)  

    # insert to database  
    try:
        actor.insert()
        return jsonify({'sucess':True,'actor':actor.long()}),201
    except:
        abort(422)

"""
'''
@TODO implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks', methods = ['POST'])
#@requires_auth('post:drinks')
def insert_drink(payload):
    result_dict = request.get_json()
    title = result_dict['title']
    recipe = json.dumps(result_dict['recipe'])
    drink = Drink(title=title, recipe=recipe)    
    try:
        drink.insert()
        return jsonify({'sucess':True,'drink':drink.long()}),201
    except:
        #db.rollback()
        abort(422)
"""

"""
PATCH
"""    
@APP.route('/movies/<int:id>', methods=['PATCH'])
#@requires_auth('patch:movies')
#def update_drink(payload, id):
def update_movie(id):
    result_dict = request.get_json()
    movie = Movie.query.filter(Movie.id == id).first()

    if movie==None:
        abort(404)
    try:
        title = result_dict.get('title')
        release_date = result_dict.get('release_date')
        description = result_dict.get('description')
        actor_id = result_dict.get('actor_id')
        if title!=None:
            movie.title = title
        if release_date!=None:
            movie.release_date = json.dumps(release_date)
        if description!=None:
            movie.description = json.dumps(description)
        if actor_id!=None:
            movie.actor_id = json.dumps(actor_id)

        movie.update()
        return jsonify({'success': True, 'movies': [movie.long()]}), 200
    except:
        abort(400)


@APP.route('/actors/<int:id>', methods=['PATCH'])
#@requires_auth('patch:actors')
#def update_drink(payload, id):
def update_actor(id):
    result_dict = request.get_json()
    actor = Actor.query.filter(Actor.id == id).first()

    if actor==None:
        abort(404)
    try:
        name = result_dict.get('name')
        date_birth = result_dict.get('date_birth')
        gender = result_dict.get('gender')

        #pdb.set_trace()
        if name!=None:
            actor.name = name
        if date_birth!=None:
            actor.date_birth = json.dumps(date_birth)
        if gender!=None:
            actor.gender = json.dumps(gender)

        actor.update()
        return jsonify({'success': True, 'actors': [actor.long()]}), 200
    except:
        abort(400)


"""
'''
@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks/<int:id>', methods=['PATCH'])
#@requires_auth('patch:drinks')
def update_drink(payload, id):
    result_dict = request.get_json()
    drink = Drink.query.filter(Drink.id == id).first()

    if drink==None:
        abort(404)
    try:
        title = result_dict.get('title')
        recipe = result_dict.get('recipe')
        if title!=None:
            drink.title = title
        if recipe!=None:
            drink.recipe = json.dumps(recipe)

        drink.update()
        return jsonify({'success': True, 'drinks': [drink.long()]}), 200
    except:
        abort(400)
"""

"""
DELETE
"""    
@APP.route('/movies/<int:id>', methods=['DELETE'])
#@requires_auth('delete:movies')
#def delete_movie(payload, id):
def delete_movie(id):
    movie = Movie.query.filter(Movie.id == id).first()

    if movie==None:
        abort(404)
    try:
        movie.delete()
        return jsonify({'success': True, 'movies': [movie.long()]}), 200
    except:
        abort(400)

@APP.route('/actors/<int:id>', methods=['DELETE'])
#@requires_auth('delete:actors')
#def delete_actor(payload, id):
def delete_actor(id):
    actor = Actor.query.filter(Actor.id == id).first()

    if actor==None:
        abort(404)
    try:
        actor.delete()
        return jsonify({'success': True, 'actors': [actor.long()]}), 200
    except:
        abort(400)


"""
'''
@TODO implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks/<int:id>', methods=['DELETE'])
#@requires_auth('delete:drinks')
def delete_drink(payload, id):
    drink = Drink.query.filter(Drink.id == id).first()

    if drink==None:
        abort(404)
    try:
        drink.delete()
        return jsonify({'success': True, 'drinks': [drink.long()]}), 200
    except:
        abort(400)
"""

## Error Handling
'''
Example error handling for unprocessable entity
'''
@APP.errorhandler(422)
def unprocessable(error):
    return jsonify({
                    "success": False, 
                    "error": 422,
                    "message": "unprocessable"
                    }), 422

'''
@TODO implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False, 
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''
@APP.errorhandler(400)
def bad_request(error):
    return jsonify({
                    "success": False, 
                    "error": 400,
                    "message": "bad request"
                    }), 400

@APP.errorhandler(405)
def not_allowed(error):
    return jsonify({
                    "success": False, 
                    "error": 405,
                    "message": "method not allowed"
                    }), 405



@APP.errorhandler(500)
def server_error(error):
    return jsonify({
                    "success": False, 
                    "error": 500,
                    "message": "server error"
                    }), 500


@APP.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
                    "success": False, 
                    "error": 405,
                    "message": "method not allowed"
                    }), 405

'''
@TODO implement error handler for 404
    error handler should conform to general task above 
'''
@APP.errorhandler(404)
def not_found(error):
    return jsonify({
                    "success": False, 
                    "error": 404,
                    "message": "not found"
                    }), 404

'''
@TODO implement error handler for AuthError
    error handler should conform to general task above 
'''
@APP.errorhandler(AuthError)
def auth_error(error):
    return jsonify({
                    "success": False,
                    "error": 401,
                    "message": "authentication error"
                    }), 401


if __name__ == '__main__':
    #APP.run(host='0.0.0.0', port=8080, debug=True)
    APP.run(debug=True)