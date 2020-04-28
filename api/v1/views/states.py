#!/usr/bin/python3
"""all default RestFul API actions"""
from api.v1.views import app_views
from models.state import State
from models import storage
from flask import jsonify, abort, request


@app_views.route("/states", methods=['GET'])
def get_states_all():
    """Retrieves the list of all State"""
    data = storage.all('State')
    states = [v.to_dict() for k, v in data.items()]
    return jsonify(states)


@app_views.route("/states/<state_id>", methods=['GET'])
def get_state(state_id):
    """Retrieves a State object specific or error 404"""
    data = storage.all('State')
    for v in data.values():
        if v.id == state_id:
            return jsonify(v.to_dict())
    abort(404)


@app_views.route("/states/<state_id>", methods=['DELETE'])
def delete_state(state_id):
    """Deletes a State object or error 404"""
    data = storage.all('State')
    for v in data.values():
        if v.id == state_id:
            storage.delete(v)
            storage.save()
            return jsonify({})
    abort(404)


@app_views.route("/states", methods=['POST'])
def create_state():
    """Add new object state to engine"""
    new_dict = request.get_json(silent=True)
    if new_dict == {}:
        return jsonify({"Error": "Not a JSON"}), 400
    elif 'name' not in new_dict:
        return jsonify({"Error": "Missing name"}), 400
    else:
        new_state = State(**new_dict)
        storage.new(new_state)
        storage.save()
        return jsonify(new_state.to_dict()), 201


@app_views.route("/states/<state_id>", methods=['PUT'])
def update_state(state_id):
    """Update instance of state"""
    update = request.get_json(silent=True)
    if update == {}:
        return jsonify({"Error": "Not a JSON"}), 400
    states = storage.all('State')
    new_state = None
    for item_state in states:
        if state_id in item_state:
            new_state = states[item_state]

    if not new_state:
        abort(404)
    ignore = ['id', 'created_at', 'updated_at']
    for k, v in update.items():
        if k not in ignore:
            setattr(new_state, k, v)
            storage.save()
    return jsonify(new_state.to_dict())

