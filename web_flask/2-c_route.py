#!/usr/bin/python3
"""Script in which starts a Flask app"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def open_hbnb():
    """print Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """prints Hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cfun(text):
    """C input text"""
    c_input = 'C {}'.format(text)
    c_input = c_input.replace('_', ' ')
    return c_input


if __name__ == "__main__":
    """runs the app"""
    app.run(host='0.0.0.0', port=5000)
