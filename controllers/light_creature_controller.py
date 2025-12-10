from flask import jsonify, request

from db import db
from models.light_creatures import LightCreatures, light_creature_schema, light_creatures_schema
from util.reflection import populate_object
from lib.authenticate import authenticate, authenticate_return_auth


@authenticate
def create_light_creature():
    post_data = request.form if request.form else request.json

    new_creature = LightCreatures()
    populate_object(new_creature, post_data)

    try:
        db.session.add(new_creature)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to add light creature"}), 400

    return jsonify({
        "message": "light creature created",
        "light_creature": light_creature_schema.dump(new_creature)
    }), 201


@authenticate
def get_all_light_creatures():
    creatures = db.session.query(LightCreatures).all()
    return jsonify({"light_creatures": light_creatures_schema.dump(creatures)}), 200


@authenticate_return_auth
def get_light_creature_by_id(light_creature_id, auth_info):
    creature = db.session.query(LightCreatures).filter(LightCreatures.light_creature_id == light_creature_id).first()

    if not creature:
        return jsonify({"message": "light creature not found"}), 404

    return jsonify({"light_creature": light_creature_schema.dump(creature)}), 200


@authenticate_return_auth
def update_light_creature(light_creature_id, auth_info):
    post_data = request.form if request.form else request.json
    creature = db.session.query(LightCreatures).filter(LightCreatures.light_creature_id == light_creature_id).first()

    if not creature:
        return jsonify({"message": "light creature not found"}), 404

    populate_object(creature, post_data)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to update light creature"}), 400

    return jsonify({
        "message": "light creature updated",
        "light_creature": light_creature_schema.dump(creature)
    }), 200


@authenticate_return_auth
def delete_light_creature(light_creature_id, auth_info):
    creature = db.session.query(LightCreatures).filter(LightCreatures.light_creature_id == light_creature_id).first()

    if not creature:
        return jsonify({"message": "light creature not found"}), 404

    try:
        db.session.delete(creature)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete light creature"}), 400

    return jsonify({"message": "light creature deleted"}), 200
