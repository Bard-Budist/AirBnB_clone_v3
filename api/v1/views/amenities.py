#!/usr/bin/python3
"""all default RestFul API actions"""
from api.v1.views import app_views
from models.amenity import Amenity
from models import storage
from flask import jsonify, abort, request


@app_views.route("/amenities", methods=['GET'])
def get_amenities():
    all_amenities = storage.all('Amenity').values()
    dict_amenities = [obj.to_dict() for obj in all_amenities]
    return jsonify(dict_amenities)


@app_views.route(
        "/amenities/<amenity_id>",
        methods=['GET'])
def get_amenitie(amenity_id):
    obj_ameni = storage.get(Amenity, amenity_id)
    if obj_ameni is None:
        abort(404)
    else:
        return jsonify(obj_ameni.to_dict())


@app_views.route(
        "/amenities/<amenity_id>",
        methods=['DELETE'])
def delete_ameniti(amenity_id):
    obj_ameni = storage.get(Amenity, amenity_id)
    if obj_ameni is None:
        abort(404)
    else:
        storage.delete(obj_ameni)
        storage.save()
        return jsonify({})


@app_views.route(
        "/amenities",
        methods=['POST'])
def create_amenity():
    dict_request = request.get_json(silent=True)
    if dict_request is None:
        return "Not JSON", 400
    elif 'name' not in dict_request:
        return "Missing name", 400
    else:
        new_amenity = Amenity(**dict_request)
        storage.new(new_amenity)
        storage.save()
        return jsonify(new_amenity.to_dict()), 201


@app_views.route(
        "/amenities/<amenity_id>",
        methods=['PUT'])
def update_amenity(amenity_id):
    dict_request = request.get_json(silent=True)
    if dict_request is None:
        return "Not JSON", 400
    obj_ameni = storage.get('Amenity', amenity_id)
    if obj_ameni is None:
        abort(404)
    ignore = ['id', 'created_at', 'updated_at']
    obj_ameni.save()
    for k, v in dict_request.items():
        if k not in ignore:
            setattr(obj_ameni, k, v)
            storage.save()
    return jsonify(obj_ameni.to_dict())
