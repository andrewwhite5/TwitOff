import os
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from twitoff.models import db, User, Tweet, migrate

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL', default='Oops')

def create_app():
    pass
    app = Flask(__name__)
    app.config['CUSTOM_VAR'] = 5  # Just an example of app config :)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    '''ROUTING'''
    # Homepage
    @app.route('/')
    def root():
        return render_template('home.html')

    # Webpage that says 'Hello [name]' when user inserts name after final '/'
    @app.route('/<name>')
    def hello_name(name):
        return render_template('name.html', name=name)

    # Webpage that describes Thanos when user inserts score after final '/'
    @app.route('/<int:score>')
    def check_score(score):
        return render_template('score.html', score=score)

    # Users route with dummy data
    @app.route('/users')
    @app.route('/users.json')
    def users():
        users = User.query.all()  # Returns a list of <class 'app.User'>
        print(type(users))
        print(type(users[0]))
        print(len(users))

        # Create simplified dict for users
        users_response = []
        for u in users:
            user_dict = u.__dict__
            del user_dict['_sa_instance_state']
            users_response.append(user_dict)
        return jsonify(users_response)

    # Create new users
    @app.route('/users/create', methods=['POST'])
    def create_user():
        print('CREATING A NEW USER...')
        print('FORM DATA:', dict(request.form))
        if 'name' in request.form:
            name = request.form['name']
            print(name)
            db.session.add(User(name=name))
            db.session.commit()
            return jsonify({'message': 'CREATED OKAY', 'name': name})
        else:
            return jsonify({'message': 'OOPS! PLEASE SPECIFY A NAME!'})

    # if __name__ == '__main__':
    #     app.run()

    return app
