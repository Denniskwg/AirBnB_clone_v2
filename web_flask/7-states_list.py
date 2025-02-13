#!/usr/bin/python3
"""7-states_list starts a Flask web application
application must be listening on 0.0.0.0, port 5000
Routes:
        /states_list: HTML page with a list of all State objects in DBStorage.
"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """lists all State objects in storage"""
    state_dict = storage.all(State)
    return render_template('7-states_list.html', states=state_dict)


@app.teardown_appcontext
def tear_down(exception):
    """close db session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
