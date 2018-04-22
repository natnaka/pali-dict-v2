# encoding: utf-8
from ._base import db
from datetime import datetime

class TwarePaliWord(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    word = db.Column(db.String(64), nullable=False)
    mean = db.Column(db.String(256))
    word_type = db.Column(db.String(64))
    gender = db.Column(db.String(64))
    vachana = db.Column(db.String(64))
    viphat = db.Column(db.String(64))
    category = db.Column(db.String(64))
    read = db.Column(db.String(128))
    note = db.Column(db.String(128))

    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now,
            onupdate=datetime.now)

    def __repr__(self):
        return "<%s: word=%s>" %(self.__class__, self.word)

