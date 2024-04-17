#!/usr/bin/python3
"""Module creates a hbnb url in my wep application
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


def sort_states():
    """Function returns a list of sorted states
    """
    from models.state import State
    state_dict = {}
    states = []
    for state in storage.all(State).values():
        state_dict.update({state.name: state})
    state_dict = dict(sorted(state_dict.items()))
    for state in state_dict.values():
        states.append(state)
    return states


@app.teardown_appcontext
def close_connection(exception=None):
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def get_hbnb():
    """Renders an html file
    """
    from models.amenity import Amenity
    states = sort_states()
    for state in states:
        cities = {}
        for city in state.cities:
            cities.update({city.name: city})
        cities = dict(sorted(cities.items()))
        state.cities = list(cities.values())

    amenities = []
    for amenity in storage.all(Amenity).values():
        amenities.append(amenity.name)
    amenities = sorted(amenities)

    place_dict = {}
    places = []
    for place in storage.all('Place').values():
        place_dict.update({place.name: place})
    place_dict = dict(sorted(place_dict.items()))
    for place in place_dict.values():
        places.append(place)
    return render_template('100-hbnb.html',
                           states=states,
                           amenities=amenities,
                           places=places)


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0', debug=True)
