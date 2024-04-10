#!/usr/bin/python3
"""
Script to start a Flask web application
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/hbnb_filters')
def hbnb_filters():
    states = storage.all("State").values()
    states.sort(key=lambda x: x.name)
    amenities = storage.all("Amenity").values()
    amenities.sort(key=lambda x: x.name)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)

@app.teardown_appcontext
def teardown_db(exception=None):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)