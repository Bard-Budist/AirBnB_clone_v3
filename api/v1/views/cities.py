#!/usr/bin/python3
"""
New view for City objects that handles all default RestFul API
"""
from api.v1.views import app_views
from models.state import State
from models.city import City
from models import storage
from flask import jsonify, abort, request
from datetime import datetime


@app_views.route(
    '/states/<state_id>/cities',
    methods=['GET'],
    strict_slashes=False)
def list_all_cities(state_id):
    """Retrieves the list of all City objects of a State"""
    state = storage.get('State', state_id)
    if state is None:
        abort(404)
    all_cities = storage.all("City").values()
    s_cities = [c.to_dict() for c in all_cities if c.state_id == state_id]
    return jsonify(s_cities)


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city(city_id):
    """Retrieves a City object. otherwise error 404"""
    city = storage.get('City', city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route(
    '/cities/<city_id>',
    methods=['DELETE'],
    strict_slashes=False)
def delete_city(city_id):
    """Deletes a City object otherwise error 404"""
    city = storage.get('City', city_id)
    if city is None:
        abort(404)
    storage.delete(city)
    storage.save()
    return jsonify({}), 200


@app_views.route(
    '/states/<state_id>/cities',
    methods=['POST'],
    strict_slashes=False)
def create_city(state_id):
    """Creates a City into the storage"""
    state = storage.get('State', state_id)
    if state is None:
        abort(404)
    new_dict_city = request.get_json(silent=True)
    if new_dict_city is None:
        return jsonify("Not a JSON"), 400
    elif 'name' not in new_dict_city:
        return ("Missing name"), 400
    else:
        new_dict_city['state_id'] = state_id
        new_city = City(**new_dict_city)
        storage.new(new_city)
        storage.save()
        return jsonify(new_city.to_dict()), 201


@app_views.route(
    '/cities/<city_id>',
    methods=['PUT'],
    strict_slashes=False)
def update_city(city_id):
    """Update an instance of City"""
    update_city_json = request.get_json(silent=True)
    if update_city_json is None:
        return jsonify("Not a JSON"), 400
    city = storage.get('City', city_id)
    if city is None:
        abort(404)
    ignore = ['id', 'created_at', 'updated_at']
    city.save()
    for k, v in update_city_json.items():
        if k not in ignore:
            setattr(city, k, v)
            storage.save()
    return jsonify(city.to_dict())
