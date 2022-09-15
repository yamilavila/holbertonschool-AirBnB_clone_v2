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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_is_cool(text='is cool'):
    """prints python and after is the input"""
    py_input = 'Python {}'.format(text)
    py_input = py_input.replace('_', ' ')
    return py_input


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """prints a number only if n is a int"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """displays a HTML page only if n is a int"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
