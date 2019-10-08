
from datetime import datetime, timedelta

from app import db

class Temperature(db.Model):
    """ Temperature table definition """

    _tablename_ = 'temperature'

    # fields of the Temperature table
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    temp_value = db.Column(db.Integer, nullable=False)
    
    def __init__(self, temp_value):
        """ initialize with name temp_value """
        self.temp_value = temp_value


    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()