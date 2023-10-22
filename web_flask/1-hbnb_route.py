#!/usr/bin/python3
"""
1. Scripts starts a Flask web application
2. Listening on 0.0.0.0, port 5000
3. Routes: /: display "Hello HBNB!"
4. Routes: /hbnb: display "HBNB"
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
