# encoding: utf-8
from ._base import db
from datetime import datetime

class ExampleModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    age = db.Column(db.Integer, default=1)
    gender = db.Column(db.String(8), default='Male')
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now,
            onupdate=datetime.now)

    def __repr__(self):
        return "<ExampleModel: name=%s, age=%d, gender=%s>" %(self.name, self.age, self.gender)
