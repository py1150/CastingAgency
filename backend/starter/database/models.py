import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "agency"
# local database_path = "postgres://{}/{}".format('localhost:5432',
# database_name)
database_path = ("postgres://rbgblbcllsormd:cf49d999f6a4acbf22eb09"
                 "d5a0dbe963a51e1ce235bb2de1c89e5f00f3b468cf@ec2-5"
                 "2-213-173-172.eu-west-1.compute.amazonaws.com:54"
                 "32/d9fuhp8j095eoj")

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


def db_drop_and_create_all():
    print('db_drop_and_create_all called')
    print('db_drop_all called')
    db.drop_all()
    print('db_create_all called')
    db.create_all()
    print('db_drop_all complete')


class Actor(db.Model):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date_birth = Column(db.Date)
    gender = Column(String)

    def short(self):
        # print(json.loads(self.name))
        print(self.name)
        return {
            'id': self.id,
            'name': self.name,
        }

    def long(self):
        return {
            'id': self.id,
            'name': self.name,
            'date_birth': self.date_birth,
            'gender': self.gender
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()
        print('Inserted to db')

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.short())


class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(db.Date)
    description = Column(String(180))
    actor_id = Column(db.Integer, db.ForeignKey('actors.id'), nullable=False)

    def short(self):
        # print(json.loads(self.title))
        print(self.title)
        return {
            'id': self.id,
            'title': self.title,
        }

    def long(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            # 'description': json.loads(self.description)
            'description': self.description,
            'actor_id': self.actor_id
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()
        print('Inserted to db')

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.short())
