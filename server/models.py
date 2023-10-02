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

    def __repr__(self):
        return f"\n<Artist id={self.id} name={self.name}>"

class Song(db.Model, SerializerMixin):
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    style = db.Column(db.String)
    lyrics = db.Column(db.Text)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))

    def __repr__(self):
        return f"\n<Song id={self.id} title={self.title} style={self.style} lyrics={self.lyrics}>"

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Integer)
    last_name = db.Column(db.Integer)
    email = db.Column(db.String, unique = True, nullable = False)
    username = db.Column(db.String)
    _password_hash = db.Column(db.String)

    def __repr__(self):
        return f"\n<User id={self.id} first_name={self.first_namename} last_name={self.last_name}email={self.email} username={self.username}>"

   