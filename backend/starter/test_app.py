import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
import time

# import the api application
from app import APP
from database.models import setup_db, db_drop_and_create_all, Actor, Movie

import pdb


# ----------------------------------------------------------------------------#
# Utility functions
# ----------------------------------------------------------------------------#

def str_to_date(time_str, format='%a, %d %b %Y %H:%M:%S'):
    """
    converts a string containing a datetime to a date
    """
    # delete locale 'GMT'
    time_str = time_str[0:len(time_str) - 4]
    # convert to date
    date = datetime.strptime(time_str, format).date()

    return date


# ----------------------------------------------------------------------------#
# Tests
# ----------------------------------------------------------------------------#


class AgencyTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = APP  # create_app()
        self.client = self.app.test_client
        self.database_name = "agency_test"
        self.database_path = "postgres://{}/{}".format(
            'localhost:5432', self.database_name)
        setup_db(self.app)

        self.token_in = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCI\
            sImtpZCI6IkRVQlM1TEhLVGFITmF1dWt0N3VZUiJ9.eyJpc3M\
            iOiJodHRwczovL3B5MTE1MC5ldS5hdXRoMC5jb20vIiwic3Vi\
            IjoiYXV0aDB8NWZlOWQ4MWM3OWFjNzkwMDZmYTc5NDJiIiwiY\
            XVkIjoiYWdlbmN5IiwiaWF0IjoxNjEwODE5NzIyLCJleHAiOj\
            E2MTA4MjY5MjIsImF6cCI6IkVlWUpJR2FmM2ZyS2ZqMW5Sd2N\
            sRjhuQTlOODh3WXB6Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9u\
            cyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsI\
            nBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YW\
            N0b3JzIiwicG9zdDptb3ZpZXMiXX0.kQKrIgLkVMXFs1Oc-gU\
            Yv5lF6Af7ESe8MEarb1Twj6SdzgF-edUp-geRN3lWmiooFd5e\
            SxJuIoc5LbxH9AejA9QZH_wlA6TVMo8QCpTRbQuL2LXQrQtxh\
            942OsQDdGwvE5yu7LeLmqlLIjoDVlH7oBh5yt4nkFZW2s1KfU\
            n0FoHtGZEBaWTvzro3k-sz7RceSahW1VwyzlCg8hoCzD3fHLl\
            NwL-FFg5YyLY1xi4n4j-ci7UrYCNWCtuFMPpZ-rjSp_kFbaWI\
            VQoIjeZSDJ7fOVbOewg5c_CWP1FmU4OHS-DWevJV_nxsXyJZL\
            1KLOxUz2WnyLiR6bf68d8Nti-BWRA'

        self.new_actor = {
            "name": "Al Pacino",
            "date_birth": "1940-04-25",
            "gender": "male"
        }

        self.new_movie = {
            "actor_id": 1,
            "description": "Crime movie",
            "id": 9,
            "release_date": "Fri, 24 Mar 1972 00:00:00 GMT",
            "title": "The Godfather"
        }

        self.updatedName = "Robert De Niro"
        self.updatedDate = "1943-08-17"
        self.update_actor = {
            "name": self.updatedName,
            "date_birth": self.updatedDate
        }

        self.updatedMName = "Goodfellas"
        self.updatedMDate = "1990-09-21"
        self.update_movie = {
            "title": self.updatedMName,
            "release_date": self.updatedMDate
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.drop_all()
            self.db.create_all()
            # self.db_drop_and_create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    Authentication
    """
    # def test_create_new_actor(self):

    def test_auth_error_actor(self):
        res = self.client().post('/actors', json=self.new_actor)
        self.assertEqual(res.status_code, 401)

    """
    Create
    """

    def test_create_new_actor(self):
        headers = {
            'Authorization': 'Bearer ' + self.token_in,
            'Content-Type': 'application/json'
        }
        res = self.client().post('/actors', headers=headers,
                                 json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['sucess'], True)
        self.assertTrue(len(data['actor']['name']))

    def test_create_new_movie(self):
        headers = {
            'Authorization': 'Bearer ' + self.token_in,
            'Content-Type': 'application/json'
        }
        res = self.client().post('/movies', headers=headers,
                                 json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['sucess'], True)
        self.assertTrue(len(data['movie']['title']))

    """
    Get
    """

    def test_get_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    """
    Patch
    """

    def test_update_actor(self):
        headers = {
            'Authorization': 'Bearer ' + self.token_in,
            'Content-Type': 'application/json'
        }
        # select record with highest id
        query = Actor.query.all()
        max_id = query[len(query) - 1].id
        res = self.client().patch(
            '/actors/' + str(max_id),
            headers=headers,
            json=self.update_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors'][0]['name']))
        self.assertEqual(data['actors'][0]['name'], self.updatedName)
        time_str = data['actors'][0]['date_birth']
        out_date = str_to_date(
            time_str=time_str,
            format='%a, %d %b %Y %H:%M:%S')
        in_date = datetime.strptime(self.updatedDate, '%Y-%m-%d').date()
        self.assertEqual(out_date, in_date)
        print('Actor updated')

    def test_update_actor_404(self):
        headers = {
            'Authorization': 'Bearer ' + self.token_in,
            'Content-Type': 'application/json'
        }
        res = self.client().patch('/actors/9999', headers=headers,
                                  json=self.update_actor)
        self.assertEqual(res.status_code, 404)

    def test_update_movie(self):
        headers = {
            'Authorization': 'Bearer ' + self.token_in,
            'Content-Type': 'application/json'
        }
        # select record with highest id
        query = Movie.query.all()
        max_id = query[len(query) - 1].id
        res = self.client().patch(
            '/movies/' + str(max_id),
            headers=headers,
            json=self.update_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies'][0]['title']))
        self.assertEqual(data['movies'][0]['title'], self.updatedMName)
        time_str = data['movies'][0]['release_date']
        out_date = str_to_date(
            time_str=time_str,
            format='%a, %d %b %Y %H:%M:%S')
        in_date = datetime.strptime(self.updatedMDate, '%Y-%m-%d').date()
        self.assertEqual(out_date, in_date)
        print('Movie updated')

    def test_update_movie_404(self):
        headers = {
            'Authorization': 'Bearer ' + self.token_in,
            'Content-Type': 'application/json'
        }
        res = self.client().patch('/movies/9999', headers=headers,
                                  json=self.update_movie)
        self.assertEqual(res.status_code, 404)

    """
    Delete
    """

    def test_delete_actor(self):
        headers = {
            'Authorization': 'Bearer ' + self.token_in,
            'Content-Type': 'application/json'
        }
        # select record with highest id
        query = Actor.query.all()
        max_id = query[len(query) - 1].id
        res = self.client().delete(
            '/actors/' + str(max_id),
            headers=headers,
            json=self.update_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors'][0]['name']))
        print('Actor deleted')

    def test_delete_actor_404(self):
        headers = {
            'Authorization': 'Bearer ' + self.token_in,
            'Content-Type': 'application/json'
        }
        # select record with highest id
        res = self.client().delete(
            '/actors/9999',
            headers=headers,
            json=self.update_actor)
        self.assertEqual(res.status_code, 404)

    def test_delete_movie(self):
        headers = {
            'Authorization': 'Bearer ' + self.token_in,
            'Content-Type': 'application/json'
        }
        # select record with highest id
        query = Movie.query.all()
        max_id = query[len(query) - 1].id
        res = self.client().delete(
            '/movies/' + str(max_id),
            headers=headers,
            json=self.update_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies'][0]['title']))
        print('Movie deleted')

    def test_delete_movie_404(self):
        headers = {
            'Authorization': 'Bearer ' + self.token_in,
            'Content-Type': 'application/json'
        }
        res = self.client().delete(
            '/movies/9999',
            headers=headers,
            json=self.update_actor)
        self.assertEqual(res.status_code, 404)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
