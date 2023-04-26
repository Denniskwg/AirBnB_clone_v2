#!/usr/bin/python3
"""9-states starts a Flask web application
application must be listening on 0.0.0.0, port 5000
Routes:
        /states_list: HTML page with a list of all State objects in DBStorage.
"""
from models import storage
from models.state import State
from flask import Flask, render_template, escape

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """lists all States in storage"""
    states = storage.all(State)
    return render_template('10-hbnb_filters.html', states=states)


@app.teardown_appcontext
def tear_down(exception):
    """close db session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
