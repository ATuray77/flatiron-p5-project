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
        data = request.get_json()

        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')
        

        if not username or not password:
            return ({'message': 'Missing username or password'}), 422

        existing_user = User.query.filter(User.username==username).first()
        if existing_user:
            return ({'message': 'User already exists'}), 422

        user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
           
        )
        user.password_hash = password

        db.session.add(user)
        db.session.commit()

        session['user_id'] = user.id

        return user.to_dict(), 201



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
class Users(Resource):
    def post(self):
        data = request.get_json()
        user = User(
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            username=data["username"]
        )
        db.session.add(user)  # adding new user to db
        db.session.commit()

        session["user_id"] = user.id  # create session

        return user.to_dict(), 201
# END OF CREATING USER CLASS THIS MAY BE MOVED LATER

api.add_resource(Users, '/signup')
api.add_resource(ClearSession, '/clear', endpoint='clear')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')
api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')

if __name__ == '__main__':
    app.run(port=5555, debug=True)

