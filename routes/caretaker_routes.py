from flask import Blueprint

import controllers.caretaker_controller as controllers


caretakers = Blueprint("caretakers", __name__)


@caretakers.route("/caretaker", methods=["POST"])
def create_caretaker_route():
    return controllers.create_caretaker()

@caretakers.route("/caretakers", methods=["GET"])
def get_all_caretakers_route():
    return controllers.get_all_caretakers()

@caretakers.route("/caretaker/<caretaker_id>", methods=["GET"])
def get_caretaker_by_id_route(caretaker_id):
    return controllers.get_caretaker_by_id(caretaker_id)

@caretakers.route("/caretaker/<caretaker_id>", methods=["PUT"])
def update_caretaker_route(caretaker_id):
    return controllers.update_caretaker(caretaker_id)

@caretakers.route("/caretaker/<caretaker_id>/delete", methods=["DELETE"])
def delete_caretaker_route(caretaker_id):
    return controllers.delete_caretaker(caretaker_id)
