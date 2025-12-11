from flask import Blueprint

import controllers.dark_creature_controller as controllers


dark_creatures = Blueprint("dark_creatures", __name__)


@dark_creatures.route("/dark_creature", methods=["POST"])
def create_dark_creature_route():
    return controllers.create_dark_creature()

@dark_creatures.route("/dark_creatures", methods=["GET"])
def get_all_dark_creatures_route():
    return controllers.get_all_dark_creatures()

@dark_creatures.route("/dark_creature/<dark_creature_id>", methods=["GET"])
def get_dark_creature_by_id_route(dark_creature_id):
    return controllers.get_dark_creature_by_id(dark_creature_id)

@dark_creatures.route("/dark_creature/<dark_creature_id>", methods=["PUT"])
def update_dark_creature_route(dark_creature_id):
    return controllers.update_dark_creature(dark_creature_id)

@dark_creatures.route("/dark_creature/delete/<dark_creature_id>", methods=["DELETE"])
def delete_dark_creature_route(dark_creature_id):
    return controllers.delete_dark_creature(dark_creature_id)
