import os
import jwt

from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta

from db import db
from models.basemodel import BaseModel

class UserModel(db.Model, BaseModel):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    loginID = db.Column(db.String(20))
    password = db.Column(db.String(30))
    
    def __init__(self, loginID, password):
        self.loginID = loginID
        self.password = Bcrypt().generate_password_hash(password).decode()
    
    def validate_password(self, password):
        """
        Checks the password against it's hash to validates the user's password
        """
        return Bcrypt().check_password_hash(self.password, password)
    
    def generate_token(self):
        """ Generates the access token"""
        try:
            # set up a payload with an expiration time
            payload = {
                'exp': datetime.utcnow() + timedelta(days=100),
                'iat': datetime.utcnow(),
                'sub': self.id
            }
            # create the byte string token using the payload and the SECRET key
            jwt_bytes = jwt.encode(
                payload,
                os.environ.get('SECRET', 'test'),
                algorithm='HS256'
            )
            return jwt_bytes.decode('utf-8')
        except Exception as e:
            # return an error in string format if an exception occurs
            raise Exception(str(e))

    @staticmethod
    def update_token(token):
        """
        Decodes the access token and give them a 100 day extension
        """
        try:
            payload = jwt.decode(token, os.environ.get('SECRET', 'test'))
            payload['exp'] = datetime.utcnow() + timedelta(days=100)
            jwt_bytes = jwt.encode(
                    payload,
                    os.environ.get('SECRET', 'test'),
                    algorithm='HS256'
                    )
            return jwt_bytes.decode('utf-8')
        except Exception as e:
            raise Exception(str(e))

    @staticmethod
    def decode_token(token):
        """Decodes the access token from the Authorization header."""
        try:
            # try to decode the token using our SECRET variable
            payload = jwt.decode(token, os.environ.get('SECRET', 'test'))
            return "", payload['sub']
        except jwt.ExpiredSignatureError:
            # the token is expired, return an error string
            return "Expired token. Please login to get a new token", None
        except jwt.InvalidTokenError:
            # the token is invalid, return an error string
            return "Invalid token. Please register or login", None
