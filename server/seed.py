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
        artist_list = []
        for i in range(10):
            artist = Artist(name=fake.name())
            artist_list.append(artist)
        db.session.add_all(artist_list)
        db.session.commit()
        # artist_list.append(artist)


        
        print ("Creating songs...")
    
        song_style = ["praise", "worship"]
        songs_list = []
        for n in range(15):
            song = Song(
                title = fake.sentence(nb_words=5, variable_nb_words=True),
                style = random.choice(song_style),
                lyrics = fake.paragraph(nb_sentences=10, variable_nb_sentences=True)
            )


            artist = random.choice(artist_list)
            artist.songs.append(song)
            songs_list.append(song)

        db.session.add_all(songs_list)
        db.session.commit()