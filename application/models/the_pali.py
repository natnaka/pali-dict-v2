# encoding: utf-8
from ._base import db
from datetime import datetime

class ThePali(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    word = db.Column(db.String(64), nullable=False, index=True)
    mean = db.Column(db.String(512))
    freq = db.Column(db.String(64))

    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now,
            onupdate=datetime.now)

    def __repr__(self):
        return "<%s: word=%s, freq=%s>" %(self.__class__, self.word, self.freq)

