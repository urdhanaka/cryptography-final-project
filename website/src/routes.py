from flask import Blueprint

api = Blueprint("api", __name__)
api.register_blueprint()
