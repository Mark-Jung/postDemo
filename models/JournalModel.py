from db import db
from datetime import datetime
from models.basemodel import BaseModel

class JournalModel(db.Model, BaseModel):
    __tablename__ = "journal"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime)
    title = db.Column(db.String(50))
    text = db.Column(db.String(280))
    longitude = db.Column(db.String(255))
    latitude = db.Column(db.String(255))
    imageUrl = db.Column(db.String(100))

    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, title, text, longitude, latitude, imageUrl):
        self.title = title
        self.text = text
        self.longitude = str(longitude)
        self.latitude = str(latitude)
        self.imageUrl = imageUrl
        self.date_created = datetime.utcnow()
    

