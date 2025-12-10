from flask import Blueprint

import controllers.magical_preserve_controller as controllers


magical_preserves = Blueprint("magical_preserves", __name__)


@magical_preserves.route("/preserve", methods=["POST"])
def create_preserve_route():
    return controllers.create_preserve()

@magical_preserves.route("/preserves", methods=["GET"])
def get_preserves_route():
    return controllers.get_preserves()

@magical_preserves.route("/preserve/<preserve_id>", methods=["GET"])
def get_preserve_by_id_route(preserve_id):
    return controllers.get_preserve_by_id(preserve_id)

@magical_preserves.route("/preserve/<preserve_id>", methods=["PUT"])
def update_preserve_route(preserve_id):
    return controllers.update_preserve(preserve_id)

@magical_preserves.route("/preserve/delete/<preserve_id>", methods=["DELETE"])
def delete_preserve_route(preserve_id):
    return controllers.delete_preserve(preserve_id)
