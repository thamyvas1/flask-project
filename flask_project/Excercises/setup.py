import os
from flask import Flask, app
import flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from flask_migrate import Migrate


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db) ##connect the database

class Puppy(db.Model):
    
    ##Manual override tablename##
    __tablename__ = 'puppies'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)
    #ONE TO MANY
    # Puppy to Many Toys
    toys = db.relationship('Toy', backref='puppy', lazy='dynamic')
    #ONE TO ONE
    #One puppy can only have one owner
    owner = db.relationship('Owner', backref='puppy', uselist = False)

    def __init__(self,name,age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __repr__(self):
        if self.owner:
            return f"Puppy {self.name} has a owner called {self.owner.name} and is {self.age} year's old"
        else:
            return f"Puppy {self.name} is {self.age} year's old and has no owner yet!!"
    
    def report_toys(self):
        print("Here are my toys: ")
        for toy in self.toys:
            print(toy.item_name)


class Toy(db.Model):
    
    __tablename__ = 'toys'

    id = db.Column(db.Integer,primary_key=True)
    item_name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self,item_name, puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id


class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self,name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id