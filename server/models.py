from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!
class Artist(db.Model, SerializerMixin):
    __tablename__ = 'artists'
    serialize_rules = ("-songs.artist",)  # added to deal with serialization

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    songs = db.relationship('Song', backref='artist')

class Song(db.Model, SerializerMixin):
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    style = db.Column(db.String)
    lyrics = db.Column(db.String)
    artist_id = db.Column(db.Integer, db.Foreignkey('artists.id'))

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Integer)
    last_name = db.Column(db.Integer)
    email = db.Column(db.String, unique = True, nullable = False)
    username = db.Column(db.String)
    _password_hash = db.Column(db.String)

   