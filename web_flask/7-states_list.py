#!/usr/bin/python3
"""
1. Scripts starts a Flask web application
2. Listening on 0.0.0.0, port 5000
3. Routes: /states_list: display a HTML page
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Return the message"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda k: k.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the current SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
