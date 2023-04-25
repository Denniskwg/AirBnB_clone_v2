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


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_list(id=None):
    """lists all States in storage"""
    states = storage.all(State)
    if id is None:
        return render_template('9-states.html', states=states)
    else:
        state_id = escape(id)
        for state in states.values():
            if state.id == state_id:
                return render_template('9-states.html', states=state)
        return render_template('9-states.html')


@app.teardown_appcontext
def tear_down(exception):
    """close db session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
