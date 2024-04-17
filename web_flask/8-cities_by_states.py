#!/usr/bin/python3
"""Starts a Flask application that fetches data from storage engine
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def close_connection(exception=None):
    storage.close()


@app.route('/states_list', strict_slashes=False)
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


@app.route('/cities_by_states', strict_slashes=False)
def get_cities_by_states():
    """Returns a html page containing cities of states
    """
    from models.state import State
    state_dict = {}
    states = []
    for state in storage.all(State).values():
        state_dict.update({state.name: state})
    state_dict = dict(sorted(state_dict.items()))
    for state in state_dict.values():
        states.append(state)
    for state in states:
        cities = {}
        for city in state.cities:
            cities.update({city.name: city})
        cities = dict(sorted(cities.items()))
        state.cities = list(cities.values())
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
