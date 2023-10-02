#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Artist, Song, User
import random

if __name__ == '__main__':
    fake = Faker()


    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
    Artist.query.delete()
    Song.query.delete()
    User.query.delete()


print("Creating Artists...")
    # name
for i in range(10):
    artist_name = fake.name()
    name = Artist(artist_name)

db.session.add(name)
db.commit()


    
print ("Creating songs...")
    # title = db.Column(db.String)
    # style = db.Column(db.String)
    # lyrics = db.Column(db.String)
song_style = ["praise", "worship"]

for n in range(20):
    song = Song(
        title = fake.sentence(nb_words=5, variable_nb_words=True),
        style = random.choice(song_style),
        lyrics = fake.paragraph(nb_sentences=10, variable_nb_sentences=True)
    )
