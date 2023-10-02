#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Artist, Song, User

if __name__ == '__main__':
    fake = Faker()


    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
    Artist.query.delete()
    Song.query.delete()
    User.query.delete()


print("Creating Users...")


    # title = db.Column(db.String)
    # style = db.Column(db.String)
    # lyrics = db.Column(db.String)
print ("Creating songs...")
