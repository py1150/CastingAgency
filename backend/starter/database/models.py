import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "agency"
#local database_path = "postgres://{}/{}".format('localhost:5432', database_name)
database_path = "postgres://rbgblbcllsormd:cf49d999f6a4acbf22eb09d5a0dbe963a51e1ce235bb2de1c89e5f00f3b468cf@ec2-52-213-173-172.eu-west-1.compute.amazonaws.com:5432/d9fuhp8j095eoj"

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to have multiple verisons of a database
'''
def db_drop_and_create_all():
    print('db_drop_and_create_all called')
    print('db_drop_all called')
    db.drop_all()
    print('db_create_all called')
    db.create_all()
    print('db_drop_all complete')

'''
Drink
a persistent drink entity, extends the base SQLAlchemy Model
'''
class Actor(db.Model):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date_birth = Column(db.Date)
    gender = Column(String)
    #movie_id = Column(db.Integer, db.ForeignKey('movies.id'), nullable=False) 
   
    '''
    short()
        short form representation of the Drink model
    '''
    def short(self):
        #print(json.loads(self.name))
        print(self.name)
        #short_recipe = [{'color': r['color'], 'parts': r['parts']} for r in json.loads(self.recipe)]
        return {
            'id': self.id,
            'name': self.name,
        }

    '''
    long()
        long form representation of the Drink model
    '''
    def long(self):
        return {
            'id': self.id,
            'name': self.name,
            #'dateOfbirth': json.loads(self.dateOfbirth)
            'date_birth': self.date_birth,
            'gender': self.gender
        }

    '''
    insert()
        inserts a new model into a database
        the model must have a unique name
        the model must have a unique id or null id
        EXAMPLE
            drink = Drink(title=req_title, recipe=req_recipe)
            drink.insert()
    '''
    def insert(self):
        db.session.add(self)
        db.session.commit()
        print('Inserted to db')

    '''
    delete()
        deletes a new model into a database
        the model must exist in the database
        EXAMPLE
            drink = Drink(title=req_title, recipe=req_recipe)
            drink.delete()
    '''
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database
        EXAMPLE
            drink = Drink.query.filter(Drink.id == id).one_or_none()
            drink.title = 'Black Coffee'
            drink.update()
    '''
    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.short())




class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(db.Date)
    description =  Column(String(180))
    actor_id = Column(db.Integer, db.ForeignKey('actors.id'), nullable=False)
    
    """
    # Autoincrementing, unique primary key
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    # String Title
    title = Column(String(80), unique=True)
    # the ingredients blob - this stores a lazy json blob
    # the required datatype is [{'color': string, 'name':string, 'parts':number}]
    recipe =  Column(String(180), nullable=False)
    """

    '''
    short()
        short form representation of the Drink model
    '''
    def short(self):
        #print(json.loads(self.title))
        print(self.title)
        #short_recipe = [{'color': r['color'], 'parts': r['parts']} for r in json.loads(self.recipe)]
        return {
            'id': self.id,
            'title': self.title,
        }

    '''
    long()
        long form representation of the Drink model
    '''
    def long(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            #'description': json.loads(self.description)
            'description': self.description,
            'actor_id': self.actor_id
        }

    '''
    insert()
        inserts a new model into a database
        the model must have a unique name
        the model must have a unique id or null id
        EXAMPLE
            drink = Drink(title=req_title, recipe=req_recipe)
            drink.insert()
    '''
    def insert(self):
        db.session.add(self)
        db.session.commit()
        print('Inserted to db')

    '''
    delete()
        deletes a new model into a database
        the model must exist in the database
        EXAMPLE
            drink = Drink(title=req_title, recipe=req_recipe)
            drink.delete()
    '''
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database
        EXAMPLE
            drink = Drink.query.filter(Drink.id == id).one_or_none()
            drink.title = 'Black Coffee'
            drink.update()
    '''
    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.short())
