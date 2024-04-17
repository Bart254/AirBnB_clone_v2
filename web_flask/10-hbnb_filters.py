#!/usr/bin/python3
"""Starts a Flask application that fetches data from storage engine
and displays a webpage
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def close_connection(exception=None):
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def get_states():
    """Function returns an html page with a list of all states
    """
    from models.amenity import Amenity
    from models.state import State
    from models import storage
    state_dict = {}
    amenities = []
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
    for amenity in storage.all(Amenity).values():
        amenities.append(amenity.name)
    amenities = sorted(amenities)
    return render_template('10-hbnb_filters.html',
                           states=states,
                           amenities=amenities
                           )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
