from flask import Flask, render_template, jsonify

# def create_app():
#     '''Create and configure an instance of the Flask application.'''
#     app = Flask(__name__)
#
#     @app.route('/')
#     def root():
#         return render_template('home.html')
#
#     return app
#
# if __name__ == '__main__':
#     create_app()

app = Flask(__name__)

# Webpage that says 'Hello World!'
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

if __name__ == '__main__':
    app.run()