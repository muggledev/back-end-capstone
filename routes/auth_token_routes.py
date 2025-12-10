from flask import Blueprint
import controllers.auth_token_controller as controllers

auth_tokens = Blueprint("auth_tokens", __name__)


@auth_tokens.route("/auth/token", methods=["POST"])
def create_token_route():
    return controllers.create_auth_token()


@auth_tokens.route("/auth/tokens", methods=["GET"])
def get_tokens_route():
    return controllers.get_all_tokens()


@auth_tokens.route("/auth/token/<auth_token>", methods=["GET"])
def get_token_by_id_route(auth_token):
    return controllers.get_token_by_id(auth_token)


@auth_tokens.route("/auth/token/<auth_token>/delete", methods=["DELETE"])
def delete_token_route(auth_token):
    return controllers.delete_token(auth_token)
