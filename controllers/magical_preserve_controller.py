from flask import jsonify, request

from db import db
from models.magical_preserves import MagicalPreserves, magical_preserve_schema, magical_preserve_schema
from util.reflection import populate_object
from lib.authenticate import authenticate, authenticate_return_auth
from uuid import UUID


@authenticate
def create_preserve():
    data = request.json if request.json else request.form
    preserve = MagicalPreserves(
        preserve_name=data.get("preserve_name"),
        location=data.get("location"),
        status=data.get("status"),
        founded_date=data.get("founded_date")
    )
    try:
        db.session.add(preserve)
        db.session.commit()
        return jsonify({"message": "preserve created", "preserve": magical_preserve_schema.dump(preserve)}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 400


@authenticate
def get_preserves():
    preserves = MagicalPreserves.query.all()
    return jsonify({"preserves": magical_preserve_schema.dump(preserves, many=True)}), 200


@authenticate_return_auth
def get_preserve_by_id(preserve_id, auth_info):
    preserve = MagicalPreserves.query.get(preserve_id)
    if not preserve:
        return jsonify({"message": "preserve not found"}), 404
    return jsonify({"preserve": magical_preserve_schema.dump(preserve)}), 200


@authenticate_return_auth
def update_preserve(preserve_id, auth_info):
    preserve = MagicalPreserves.query.get(preserve_id)
    if not preserve:
        return jsonify({"message": "preserve not found"}), 404

    data = request.json if request.json else request.form
    try:
        populate_object(preserve, data)
        db.session.commit()
        return jsonify({"message": "preserve updated", "preserve": magical_preserve_schema.dump(preserve)}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 400


@authenticate_return_auth
def delete_preserve(preserve_id, auth_info):
    preserve = MagicalPreserves.query.get(preserve_id)
    if not preserve:
        return jsonify({"message": "preserve not found"}), 404
    try:
        db.session.delete(preserve)
        db.session.commit()
        return jsonify({"message": "preserve deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 400
