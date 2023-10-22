#!/usr/bin/python3
"""
1. Scripts starts a Flask web application
2. Listening on 0.0.0.0, port 5000
3. Routes: /: display "Hello HBNB!"
4. Routes: /hbnb: display "HBNB"
5. Routes: /c/<text>: display "C" followed by the value of the text variable
6. Routes: /python/(<text>): display "Python" followed by the value of the text
"""

from flask import Flask

app = Flask(__name__)


# Define the root route for the URL
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return the message"""
    return 'Hello HBNB!'


# Define the /hbnb route for the URL
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return the message"""
    return 'HBNB'


# Define the /c/<text> route for the URL
@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Return the message"""
    return 'C {}'.format(text.replace('_', ' '))


# Define the /python/(<text>) route for the URL
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """Return the message"""
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
