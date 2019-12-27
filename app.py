import os

from flask import Flask, request, redirect, Response
from flask_cors import CORS
from flask_migrate import Migrate

from db import db

from views.JournalView import JournalView

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///localdata.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE'] = 'filesystem'

migrate = Migrate(app, db)

@app.route('/', methods=['GET'])
def sup():
    return "sup" 

@app.route('/journal', methods=['POST'])
def new_journal():
    return JournalView.new_journal()

if __name__ == '__main__':
    CORS(app)
    db.init_app(app)
    @app.before_first_request
    def create_tables():
        db.create_all()
    app.run()


