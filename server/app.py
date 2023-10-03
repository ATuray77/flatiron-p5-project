#!/usr/bin/env python3

# Standard library imports
from sqlalchemy.exc import IntegrityError
# Remote library imports
from flask import request, session, make_response, jsonify
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import Artist, Song, User


# Views go here!

class ClearSession(Resource):

    def delete(self):
    
        session['page_views'] = None
        session['user_id'] = None

        return {}, 204


class Signup(Resource):

    def post(self):
        
        username = request.get_json()['username']
        password = request.get_json()['password']

        if username and password:
            
            new_user = User(username=username)
            new_user.password_hash = password
            db.session.add(new_user)
            db.session.commit()

            session['user_id'] = new_user.id
            
            return new_user.to_dict(), 201

        return {'error': '422 Unprocessable Entity'}, 422


class CheckSession(Resource):

    def get(self):

        if session.get('user_id'):
            
            user = User.query.filter(User.id == session['user_id']).first()
            
            return user.to_dict(), 200

        return {}, 204

class Login(Resource):

    def post(self):

        username = request.get_json()['username']
        password = request.get_json()['password']

        user = User.query.filter(User.username == username).first()

        if user.authenticate(password):

            session['user_id'] = user.id
            return user.to_dict(), 200

        return {'error': '401 Unauthorized'}, 401

class Logout(Resource):
    def delete(self):
    
        session['user_id'] = None
        
        return {}, 204


# CRUD ROUTES
class SongsIndex(Resource):
    def get(self):
        if not session.get('user_id'):
            return ({"error":"unauthorized"}, 401)
        else:
            user_id = session['user_id']
            songs = [song.to_dict() for song in Song.query.filter(Song.user_id == user_id).all()]
            return songs, 200
    
    def post(self):
        json = request.get_json()
        if not session.get('user_id'):
            return ({"error":"unauthorized"}, 401)
        else:
            try:
                new_song = Song(
                    title = json['title'],
                    style = json['style'],
                    lyrics = json['lyrics'],
                    user_id = session['user_id'],
                    )
            
                db.session.add(new_song)
                db.session.commit()
                return new_song.to_dict(), 201
            except IntegrityError:
                db.session.rollback()
                return ({"error":"unprocessable entity"}, 422)


@app.route('/')
def index():
    return '<h1>Project Server</h1>'

@app.route('/songs', methods=['GET'])
def songs():
    if request.method == 'GET':
        songs = Song.query.all()

        return make_response(
            jsonify([movie.to_dict() for movie in songs]),
            200,
        )

    return make_response(
        jsonify({"text": "Method Not Allowed"}),
        405,
    ) 


# CREATING USER CLASS THIS MAY BE MOVED LATER
class User(Resource):
    def post(self):
        data = request.get_json()
        user = User(
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            username=data["username"]

        )
# END OF CREATING USER CLASS THIS MAY BE MOVED LATER


api.add_resource(ClearSession, '/clear', endpoint='clear')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')
api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')

if __name__ == '__main__':
    app.run(port=5555, debug=True)

