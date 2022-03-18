
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

# http://127.0.0.1:5000/
@app.route('/')
def hello_world():
    return 'Hello, World!'

# http://127.0.0.1:5000/bye
@app.route('/bye')
def say_bye():
    return 'Bye!'

if __name__ == "__main__":
    app.run()
