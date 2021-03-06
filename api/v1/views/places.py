#!/usr/bin/python3
"""all default RestFul API actions"""
from api.v1.views import app_views
from models.place import Place
from models.city import City
from models import storage
from flask import jsonify, request, abort


@app_views.route(
        "/cities/<city_id>/places",
        methods=['GET'],
        strict_slashes=False)
def get_all_places(city_id):
    """Retrieves the list of all Place objects of a City"""
    city = storage.get('City', city_id)
    if city is None:
        abort(404)
    all_es = storage.all('Place').values()
    places = [obj.to_dict() for obj in all_es if obj.city_id == city_id]
    return jsonify(places)


@app_views.route(
        "/places/<place_id>",
        methods=['GET'],
        strict_slashes=False)
def get_specific_place(place_id):
    """Retrieves a Place objec"""
    place = storage.get('Place', place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route(
        "/places/<place_id>",
        methods=['DELETE'],
        strict_slashes=False)
def delete_place(place_id):
    """Deletes a Place object"""
    place = storage.get('Place', place_id)
    if place is None:
        abort(404)
    storage.delete(place)
    storage.save()
    return jsonify({})


@app_views.route(
        "/cities/<city_id>/places",
        methods=['POST'],
        strict_slashes=False)
def create_place(city_id):
    """Creates a Place"""
    city = storage.get('City', city_id)
    if city is None:
        abort(404)
    dict_request = request.get_json(silent=True)
    if dict_request is None:
        return "Not a JSON", 400
    elif 'name' not in dict_request:
        return "Missing name", 400
    elif 'user_id' not in dict_request:
        return "Missing user_id", 400
    user_id = dict_request['user_id']
    user = storage.get('User', user_id)
    if user is None:
        abort(404)
    dict_request['city_id'] = city_id
    place = Place(**dict_request)
    storage.new(place)
    storage.save()
    return jsonify(place.to_dict()), 201


@app_views.route(
        "/places/<place_id>",
        methods=['PUT'],
        strict_slashes=False)
def update_place(place_id):
    """Updates a Place object"""
    dict_request = request.get_json(silent=True)
    if dict_request is None:
        return "Not a JSON", 400
    place = storage.get('Place', place_id)
    if place is None:
        abort(404)
    ignore = ['id', 'user_id', 'city_id', 'created_at', 'updated_at']
    place.save()
    for k, v in dict_request.items():
        if k not in ignore:
            setattr(place, k, v)
    storage.save()
    return jsonify(place.to_dict())
