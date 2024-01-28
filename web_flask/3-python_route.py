#!/usr/bin/python3
""" Uses Flask to create a hello page
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays hello page of web application
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB message
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_message(text):
    """ Displays default C message
    """
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_message(text="is cool"):
    """ Displays default python message
    """
    text = text.replace('_', ' ')
    return f'Python {text}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
