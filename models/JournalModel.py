from db import db
from datetime import datetime
from models.basemodel import BaseModel

class JournalModel(db.Model, BaseModel):
    __tablename__ = "journal"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime)
    title = db.Column(db.String(50))
    text = db.Column(db.String(280))
    longitude = db.Column(db.Numeric(precision=6))
    latitude = db.Column(db.Numeric(precision=6))
    imageUrl = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, title, text, longitude, latitude, imageUrl):
        self.title = title
        self.text = text
        self.longitude = longitude
        self.latitude = latitude
        self.imageUrl = imageUrl
        self.date_created = datetime.utcnow()
    

