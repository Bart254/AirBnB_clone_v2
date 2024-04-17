#!/usr/bin/python3
"""Starts a Flask application that fetches data from storage engine
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def close_connection(exception=None):
    storage.close()


@app.route('/states', strict_slashes=False)
def get_states():
    """Function returns an html page with a list of all states
    """
    from models.state import State
    state_dict = {}
    states = []
    for state in storage.all(State).values():
        state_dict.update({state.name: state})
    state_dict = dict(sorted(state_dict.items()))
    for state in state_dict.values():
        states.append(state)
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def get_cities_by_states(id):
    """Displays a html page depending on whether state is found or not
    """
    from models.state import State
    my_state = None
    for state in storage.all(State).values():
        if state.id == id:
            my_state = state
            break
    if my_state:
        cities = {}
        for city in my_state.cities:
            cities.update({city.name: city})
        cities = dict(sorted(cities.items()))
        my_state.cities = list(cities.values())
    return render_template('9-states.html', state=my_state)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
