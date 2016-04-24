# -*- coding: utf-8 -*-

from bookhouse.core import db


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    name = db.Column(db.String(32), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    intro = db.Column(db.Text)

    user = db.relationship(
        'User',
        foreign_keys=[user_id], primaryjoin='Book.user_id == User.id',
        backref=db.backref('books', cascade='all, delete-orphan'))
