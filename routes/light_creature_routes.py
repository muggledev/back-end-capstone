from flask import Blueprint

import controllers.light_creature_controller as controllers


light_creatures = Blueprint("light_creatures", __name__)


@light_creatures.route("/light_creature", methods=["POST"])
def create_light_creature_route():
    return controllers.create_light_creature()

@light_creatures.route("/light_creatures", methods=["GET"])
def get_all_light_creatures_route():
    return controllers.get_all_light_creatures()

@light_creatures.route("/light_creature/<light_creature_id>", methods=["GET"])
def get_light_creature_by_id_route(light_creature_id):
    return controllers.get_light_creature_by_id(light_creature_id)

@light_creatures.route("/light_creature/<light_creature_id>", methods=["PUT"])
def update_light_creature_route(light_creature_id):
    return controllers.update_light_creature(light_creature_id)

@light_creatures.route("/light_creature/delete/<light_creature_id>", methods=["DELETE"])
def delete_light_creature_route(light_creature_id):
    return controllers.delete_light_creature(light_creature_id)
