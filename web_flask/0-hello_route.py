#!/usr/bin/python3
'''Script that start Flask app'''
from flask import Flask
app = Flask(__name__)

@app.route('/frontPage/', strict_slashes=False)
def open_hbnb():
    """print Hello HBNB!"""
    return "Hello HBNB!"


if __name__ == '__main__':
    """runs the app"""
    app.run(host='0.0.0.0', port=5000)
