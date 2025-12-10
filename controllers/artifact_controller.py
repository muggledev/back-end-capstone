from flask import jsonify, request

from db import db
from models.artifacts import Artifacts, artifact_schema, artifacts_schema
from util.reflection import populate_object
from lib.authenticate import authenticate, authenticate_return_auth


@authenticate
def create_artifact():
    post_data = request.form if request.form else request.json

    new_artifact = Artifacts()
    populate_object(new_artifact, post_data)

    try:
        db.session.add(new_artifact)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to add artifact"}), 400

    return jsonify({
        "message": "artifact created",
        "artifact": artifact_schema.dump(new_artifact)
    }), 201


@authenticate
def get_all_artifacts():
    artifacts = db.session.query(Artifacts).all()
    return jsonify({"artifacts": artifacts_schema.dump(artifacts)}), 200


@authenticate_return_auth
def get_artifact_by_id(artifact_id, auth_info):
    artifact = db.session.query(Artifacts).filter(Artifacts.artifact_id == artifact_id).first()

    if not artifact:
        return jsonify({"message": "artifact not found"}), 404

    return jsonify({"artifact": artifact_schema.dump(artifact)}), 200


@authenticate_return_auth
def update_artifact(artifact_id, auth_info):
    post_data = request.form if request.form else request.json
    artifact = db.session.query(Artifacts).filter(Artifacts.artifact_id == artifact_id).first()

    if not artifact:
        return jsonify({"message": "artifact not found"}), 404

    populate_object(artifact, post_data)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to update artifact"}), 400

    return jsonify({
        "message": "artifact updated",
        "artifact": artifact_schema.dump(artifact)
    }), 200


@authenticate_return_auth
def delete_artifact(artifact_id, auth_info):
    artifact = db.session.query(Artifacts).filter(Artifacts.artifact_id == artifact_id).first()

    if not artifact:
        return jsonify({"message": "artifact not found"}), 404

    try:
        db.session.delete(artifact)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete artifact"}), 400

    return jsonify({"message": "artifact deleted"}), 200
