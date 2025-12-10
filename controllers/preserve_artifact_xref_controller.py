from flask import jsonify, request

from db import db
from models.preserve_artifacts_xref import PreserveArtifactsXref, preserve_artifacts_xref_schema, preserve_artifacts_xref_schemas
from util.reflection import populate_object
from lib.authenticate import authenticate, authenticate_return_auth


@authenticate
def create_preserve_artifact():
    post_data = request.form if request.form else request.json

    new_xref = PreserveArtifactsXref()
    populate_object(new_xref, post_data)

    try:
        db.session.add(new_xref)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to add preserve-artifact relation"}), 400

    return jsonify({
        "message": "preserve-artifact relation created",
        "preserve_artifact": preserve_artifacts_xref_schema.dump(new_xref)
    }), 201


@authenticate
def get_all_preserve_artifacts():
    xrefs = db.session.query(PreserveArtifactsXref).all()
    return jsonify({"preserve_artifacts": preserve_artifacts_xref_schemas.dump(xrefs)}), 200


@authenticate_return_auth
def get_preserve_artifact_by_id(preserve_id, artifact_id, auth_info):
    xref = db.session.query(PreserveArtifactsXref).filter(
        PreserveArtifactsXref.preserve_id == preserve_id,
        PreserveArtifactsXref.artifact_id == artifact_id
    ).first()

    if not xref:
        return jsonify({"message": "preserve-artifact relation not found"}), 404

    return jsonify({"preserve_artifact": preserve_artifacts_xref_schema.dump(xref)}), 200


@authenticate_return_auth
def update_preserve_artifact(preserve_id, artifact_id, auth_info):
    post_data = request.form if request.form else request.json

    xref = db.session.query(PreserveArtifactsXref).filter(
        PreserveArtifactsXref.preserve_id == preserve_id,
        PreserveArtifactsXref.artifact_id == artifact_id
    ).first()

    if not xref:
        return jsonify({"message": "preserve-artifact relation not found"}), 404

    populate_object(xref, post_data)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to update preserve-artifact relation"}), 400

    return jsonify({
        "message": "preserve-artifact relation updated",
        "preserve_artifact": preserve_artifacts_xref_schema.dump(xref)
    }), 200


@authenticate_return_auth
def delete_preserve_artifact(preserve_id, artifact_id, auth_info):
    xref = db.session.query(PreserveArtifactsXref).filter(
        PreserveArtifactsXref.preserve_id == preserve_id,
        PreserveArtifactsXref.artifact_id == artifact_id
    ).first()

    if not xref:
        return jsonify({"message": "preserve-artifact relation not found"}), 404

    try:
        db.session.delete(xref)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete preserve-artifact relation"}), 400

    return jsonify({"message": "preserve-artifact relation deleted"}), 200
