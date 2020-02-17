from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

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
