#!/usr/bin/python3
"""
Starts a Flask web application to display filters for states, cities, and amenities.
"""

from flask import Flask, render_template # type: ignore
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Display a HTML page with filters for states, cities, and amenities."""
    states = sorted(list(storage.all("State").values()), key=lambda state: state.name)
    cities = sorted(list(storage.all("City").values()), key=lambda city: city.name)
    amenities = sorted(list(storage.all("Amenity").values()), key=lambda amenity: amenity.name)
    return render_template('10-hbnb_filters.html', states=states, cities=cities, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
