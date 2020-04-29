#!/usr/bin/python3
"""New view for User object that handles all default RestFul API"""
from api.v1.views import app_views
from models.state import State
from models.city import City
from models.user import User
from models import storage
from flask import jsonify, abort, request
from datetime import datetime


@app_views.route('/users/', methods=['GET'], strict_slashes=False)
def list_all_user():
    """Retrives a list all User"""
    all_user = storage.all('User')
    users = [u.to_dict() for u in all_user.values()]
    return jsonify(users)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_users(user_id):
    """Retrives a especific instance of User otherwise 404 error"""
    user = storage.get('User', user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """Delete a specific instance of User otherwise error 404"""
    user = storage.get('User', user_id)
    if user is None:
        abort(404)
    storage.delete(user)
    storage.save()
    return jsonify({}), 200


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """Add another object into storage"""
    new_user_dict = request.get_json(silent=True)
    if new_user_dict is None:
        return jsonify("Not a JSON"), 400
    elif 'email' not in new_user_dict:
        return ("Missing email"), 400
    elif 'password' not in new_user_dict:
        return ("Missing password"), 400
    else:
        new_user = User(**new_user_dict)
        storage.new(new_user)
        storage.save()
        return jsonify(new_user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """Update an instance of User"""
    update_user_json = request.get_json(silent=True)
    if update_user_json is None:
        return jsonify("Not a JSON"), 400
    user = storage.get('User', user_id)
    if user is None:
        abort(404)
    ignore = ['id', 'email', 'created_at', 'updated_at']
    user.save()
    for k, v in update_user_json.items():
        if k not in ignore:
            setattr(user, k, v)
            storage.save()
    return jsonify(user.to_dict())
