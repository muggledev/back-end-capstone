from flask import Blueprint

import controllers.artifact_controller as controllers


artifacts = Blueprint("artifacts", __name__)


@artifacts.route("/artifact", methods=["POST"])
def create_artifact_route():
    return controllers.create_artifact()

@artifacts.route("/artifacts", methods=["GET"])
def get_all_artifacts_route():
    return controllers.get_all_artifacts()

@artifacts.route("/artifact/<artifact_id>", methods=["GET"])
def get_artifact_by_id_route(artifact_id):
    return controllers.get_artifact_by_id(artifact_id)

@artifacts.route("/artifact/<artifact_id>", methods=["PUT"])
def update_artifact_route(artifact_id):
    return controllers.update_artifact(artifact_id)

@artifacts.route("/artifact/delete/<artifact_id>", methods=["DELETE"])
def delete_artifact_route(artifact_id):
    return controllers.delete_artifact(artifact_id)
