from flask import Blueprint

import controllers.preserve_artifact_xref_controller as controllers


preserve_artifacts_xref = Blueprint("preserve_artifacts_xref", __name__)


@preserve_artifacts_xref.route("/preserve_artifact_xref", methods=["POST"])
def create_preserve_artifact_xref_route():
    return controllers.create_preserve_artifact_xref()

@preserve_artifacts_xref.route("/preserve_artifacts_xref", methods=["GET"])
def get_all_preserve_artifacts_xref_route():
    return controllers.get_all_preserve_artifacts_xref()

@preserve_artifacts_xref.route("/preserve_artifact_xref/<preserve_artifact_xref_id>", methods=["GET"])
def get_preserve_artifact_xref_by_id_route(preserve_artifact_xref_id):
    return controllers.get_preserve_artifact_xref_by_id(preserve_artifact_xref_id)

@preserve_artifacts_xref.route("/preserve_artifact_xref/<preserve_artifact_xref_id>", methods=["PUT"])
def update_preserve_artifact_xref_route(preserve_artifact_xref_id):
    return controllers.update_preserve_artifact_xref(preserve_artifact_xref_id)

@preserve_artifacts_xref.route("/preserve_artifact_xref/delete/<preserve_artifact_xref_id>", methods=["DELETE"])
def delete_preserve_artifact_xref_route(preserve_artifact_xref_id):
    return controllers.delete_preserve_artifact_xref(preserve_artifact_xref_id)