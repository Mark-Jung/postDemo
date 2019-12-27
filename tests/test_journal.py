import os, sys
import unittest
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
basedir = os.path.abspath(os.path.dirname(__file__))

from app import app
from db import db

from helper import Helper

TEST_DB = 'test.db'
class JournalTests(unittest.TestCase):
    sample_journal = {
        "title": "test",
        "text": "body",
        "date": None,
        "longitude": 23.3,
        "latitude": 23.12,
        "files": [str(open("/home/mark/postDemo/tests/cutecat.jpg", 'rb').read())]
    }

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.init_app(app)
        #db.create_all(app=app)

    # executed after each test
    def tearDown(self):
        db.drop_all(app=app)
        pass

    def test_when_journal_posted_then_writes_to_db(self):
        response = self.app.post('/journal', data=json.dumps(self.sample_journal))
        self.assertEqual(response.status_code, 201)
        with app.app_context():
            # check if request's body is consistent with the database
            pass
