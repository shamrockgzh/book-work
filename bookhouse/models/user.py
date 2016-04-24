# -*- coding: utf-8 -*-

from bookhouse.core import db


GENDER_OPTIONS = {
    'MALE': 1,
    'FEMALE': 2,
}


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(32))
    gender = db.Column(db.Integer, nullable=False)
