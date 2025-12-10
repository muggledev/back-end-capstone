from flask import jsonify, request
from datetime import datetime, timedelta

from db import db
from models.auth_tokens import AuthTokens, auth_token_schema, auth_tokens_schema
from models.users import Users
from lib.authenticate import authenticate



def create_auth_token():
    post_data = request.form if request.form else request.json

    user_id = post_data.get("user_id")

    if not user_id:
        return jsonify({"message": "user_id is required"}), 400

    user = db.session.query(Users).filter(Users.user_id == user_id).first()

    if not user:
        return jsonify({"message": "user not found"}), 404

    expiration = datetime.now() + timedelta(hours=24)

    new_token = AuthTokens(user_id=user_id, expiration=expiration)

    try:
        db.session.add(new_token)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create token"}), 400

    return jsonify({
        "message": "token created",
        "token": auth_token_schema.dump(new_token)
    }), 201


@authenticate
def get_all_tokens():
    tokens = db.session.query(AuthTokens).all()
    return jsonify({"tokens": auth_tokens_schema.dump(tokens)}), 200


@authenticate
def get_token_by_id(auth_token):
    token = db.session.query(AuthTokens).filter(AuthTokens.auth_token == auth_token).first()

    if not token:
        return jsonify({"message": "token not found"}), 404

    return jsonify({"token": auth_token_schema.dump(token)}), 200


@authenticate
def delete_token(auth_token):
    token = db.session.query(AuthTokens).filter(AuthTokens.auth_token == auth_token).first()

    if not token:
        return jsonify({"message": "token not found"}), 404

    try:
        db.session.delete(token)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete token"}), 400

    return jsonify({"message": "token deleted"}), 200
