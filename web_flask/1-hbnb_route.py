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


if __name__ == "__main__":
    """runs the app"""
    app.run(host='0.0.0.0', port=5000)
