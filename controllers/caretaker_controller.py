from flask import jsonify, request

from db import db
from models.caretakers import Caretakers, caretaker_schema, caretakers_schema
from util.reflection import populate_object
from lib.authenticate import authenticate, authenticate_return_auth


@authenticate
def create_caretaker():
    post_data = request.form if request.form else request.json

    new_caretaker = Caretakers()
    populate_object(new_caretaker, post_data)

    try:
        db.session.add(new_caretaker)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to add caretaker"}), 400

    return jsonify({
        "message": "caretaker created",
        "caretaker": caretaker_schema.dump(new_caretaker)
    }), 201


@authenticate
def get_all_caretakers():
    caretakers = db.session.query(Caretakers).all()
    return jsonify({"caretakers": caretakers_schema.dump(caretakers)}), 200


@authenticate_return_auth
def get_caretaker_by_id(caretaker_id, auth_info):
    caretaker = db.session.query(Caretakers).filter(Caretakers.caretaker_id == caretaker_id).first()

    if not caretaker:
        return jsonify({"message": "caretaker not found"}), 404

    return jsonify({"caretaker": caretaker_schema.dump(caretaker)}), 200


@authenticate_return_auth
def update_caretaker(caretaker_id, auth_info):
    post_data = request.form if request.form else request.json

    caretaker = db.session.query(Caretakers).filter(Caretakers.caretaker_id == caretaker_id).first()

    if not caretaker:
        return jsonify({"message": "caretaker not found"}), 404

    populate_object(caretaker, post_data)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to update caretaker"}), 400

    return jsonify({
        "message": "caretaker updated",
        "caretaker": caretaker_schema.dump(caretaker)
    }), 200


@authenticate_return_auth
def delete_caretaker(caretaker_id, auth_info):
    caretaker = db.session.query(Caretakers).filter(Caretakers.caretaker_id == caretaker_id).first()

    if not caretaker:
        return jsonify({"message": "caretaker not found"}), 404

    try:
        db.session.delete(caretaker)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete caretaker"}), 400

    return jsonify({"message": "caretaker deleted"}), 200
