from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['CUSTOM_VAR'] = 5  # Just an example of app config :)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))



#
# ROUTING
#

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
    users = [
        {'id':1, 'name': 'First User'},
        {'id':2, 'name': 'Second User'},
        {'id':3, 'name': 'Third User'},
    ]
    return jsonify(users)

@app.route('/users/create', methods=['POST'])
def create_user():
    print('CREATING A NEW USER...')
    print('FORM DATA:', dict(request.form))
    # todo: create a new user
    return jsonify({'message': 'CREATED OKAY (TODO)'})

if __name__ == '__main__':
    app.run()
