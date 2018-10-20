from flask_sqlalchemy import SQLAlchemy as sa
from flask import Flask as fl
from sqlalchemy import exc

class Parent(db.Model):

    id = db.Column('parent_id', db.Integer, primary_key=True)
    parent_col = db.Column('parent_col', db.VARCHAR(45))

    child = db.relationship('Child', backref='parent', lazy=True)


    def __init__(self, symbol_col):
        self.parent_col = parent_col

    def __repr__(self):
        return '<Parent %r>' % self.id


class Child(db.Model):
    id = db.Column('child_id', db.Integer, primary_key=True)
    col1 = db.Column('col1', db.Text(20))
    col2 = db.Column('col2', db.VARCHAR(45))
    col3 = db.Column('col3', db.VARCHAR(45))
    parent_id = db.Column(db.Integer, db.ForeignKey('Parent.parent_id'))
    parents = db.relationship('parent')

    def __int__(self, col1, col2,col3):
        self.col1 = col1
        self.col2 = col2
        self.col3 = col3

    def __repr__(self):
        return '<Child %r>' % self.id


