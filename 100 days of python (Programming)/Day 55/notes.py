from flask import Flask
import random

app = Flask(__name__)

print(random.__name__)
print(__name__)

# https://flask.palletsprojects.com/en/1.1.x/quickstart/
# ~ set FLASK_APP=hello.py
# ~ flask run
# http://127.0.0.1:5000/
# ctrl + c to quit

'''
@ means when the user hits this '/' you want to see the home page hello_world
@ is a decorater* decorator function gives additional functionality
'''

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper

# http://127.0.0.1:5000/
@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
    '<p>This is a paragraph</p>' \
    '<img src="https://media.giphy.com/media/hvS1eKlR75hMr0l7VJ/giphy.gif">'

# http://127.0.0.1:5000/bye
@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return 'Bye!'

'''https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules'''
# http://127.0.0.1:5000/Tim
@app.route('/<name>')
def greet(name):
    return f'<h1 style="text-align: center"> Hello there {name}! </h1>'

'''keeps everything after username'''
@app.route('/username/<path:name>')
def greet_path(name):
    return f"Hello there {name}!"

'''Multiple inputs'''
@app.route('/username/<name>/<int:number>')
def multiple_inputs(name, number):
    return f"Hello there {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)