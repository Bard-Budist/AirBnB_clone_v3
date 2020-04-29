#!/usr/bin/python3
"""New view for Review object that handles all default RestFul API"""
from api.v1.views import app_views
from models.state import State
from models.city import City
from models.user import User
from models.review import Review
from models import storage
from flask import jsonify, abort, request
from datetime import datetime


@app_views.route('/places/<place_id>/reviews',
                 methods=['GET'],
                 strict_slashes=False)
def list_all_(place_id):
    """Retrives a list all Reviews of a places otherwise error 404"""
    place = storage.get('Place', place_id)
    if place is None:
        abort(404)
    all_reviews = storage.all("Review").values()
    reviews = [r.to_dict() for r in all_reviews if r.place_id == place_id]
    return jsonify(reviews)


@app_views.route('reviews/<review_id>', methods=['GET'], strict_slashes=False)
def get_reviews(review_id):
    """Retrives a especific instance of Review otherwise 404 error"""
    review = storage.get('Review', review_id)
    if review is None:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('/reviews/<review_id>',
                 methods=['DELETE'],
                 strict_slashes=False)
def delete_review(review_id):
    """Delete a specific instance of Review otherwise error 404"""
    review = storage.get('Review', review_id)
    if review is None:
        abort(404)
    storage.delete(review)
    storage.save()
    return jsonify({}), 200


@app_views.route('/places/<place_id>/reviews',
                 methods=['POST'],
                 strict_slashes=False)
def create_review(place_id):
    """Add another object into storage"""
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    new_review_dict = request.get_json(silent=True)
    if new_review_dict is None:
        return jsonify("Not a JSON"), 400
    elif 'user_id' not in new_review_dict:
        return ("Missing user_id"), 400
    elif 'text' not in new_review_dict:
        return ("Missing text"), 400
    user = storage.get("User", request.json["user_id"])
    if user is None:
        abort(404)
    new_review_dict['place_id'] = place_id
    new_review = Review(**new_review_dict)
    storage.new(new_review)
    storage.save()
    return jsonify(new_review.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def update_review(review_id):
    """Update an instance of Review"""
    update_review_json = request.get_json(silent=True)
    if update_review_json is None:
        return jsonify("Not a JSON"), 400
    review = storage.get('Review', review_id)
    if review is None:
        abort(404)
    ignore = ['id', 'created_at', 'updated_at', 'user_id', 'place_id']
    review.save()
    for k, v in update_review_json.items():
        if k not in ignore:
            setattr(review, k, v)
            storage.save()
    return jsonify(review.to_dict())
