#!/usr/bin/python3
"""
Script to start a Flask web application
"""

from flask import Flask
from urllib.parse import unquote

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route to display 'Hello HBNB!'
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    Route to display 'HBNB'
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """
    Route to display 'C ' followed by the value of the text variable
    """
    return 'C {}'.format(unquote(text).replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
