from flask import jsonify, request

from db import db
from models.dark_creatures import DarkCreatures, dark_creature_schema, dark_creatures_schema
from util.reflection import populate_object
from lib.authenticate import authenticate, authenticate_return_auth


@authenticate
def create_dark_creature():
    post_data = request.form if request.form else request.json

    new_creature = DarkCreatures()
    populate_object(new_creature, post_data)

    try:
        db.session.add(new_creature)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to add dark creature"}), 400

    return jsonify({
        "message": "dark creature created",
        "dark_creature": dark_creature_schema.dump(new_creature)
    }), 201


@authenticate
def get_all_dark_creatures():
    creatures = db.session.query(DarkCreatures).all()
    return jsonify({"dark_creatures": dark_creatures_schema.dump(creatures)}), 200


@authenticate_return_auth
def get_dark_creature_by_id(dark_creature_id, auth_info):
    creature = db.session.query(DarkCreatures).filter(DarkCreatures.dark_creature_id == dark_creature_id).first()

    if not creature:
        return jsonify({"message": "dark creature not found"}), 404

    return jsonify({"dark_creature": dark_creature_schema.dump(creature)}), 200


@authenticate_return_auth
def update_dark_creature(dark_creature_id, auth_info):
    post_data = request.form if request.form else request.json
    creature = db.session.query(DarkCreatures).filter(DarkCreatures.dark_creature_id == dark_creature_id).first()

    if not creature:
        return jsonify({"message": "dark creature not found"}), 404

    populate_object(creature, post_data)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to update dark creature"}), 400

    return jsonify({
        "message": "dark creature updated",
        "dark_creature": dark_creature_schema.dump(creature)
    }), 200


@authenticate_return_auth
def delete_dark_creature(dark_creature_id, auth_info):
    creature = db.session.query(DarkCreatures).filter(DarkCreatures.dark_creature_id == dark_creature_id).first()

    if not creature:
        return jsonify({"message": "dark creature not found"}), 404

    try:
        db.session.delete(creature)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete dark creature"}), 400

    return jsonify({"message": "dark creature deleted"}), 200
