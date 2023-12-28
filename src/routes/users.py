# Flask features
from typing import List
from flask import Blueprint, json, jsonify

# Types
from utils.interfaces.datatypes import Users_Types

# bp instance
users_bp = Blueprint("products", __name__)
FILE_DATA: str = "src/examples/data.json"


# Read example products data
with open(FILE_DATA, "r") as archivo:
    datos: List[Users_Types] = json.load(archivo)


# Get products Endpoint
@users_bp.route("/users")
def get_productos():
    return jsonify({"confirm": True, "data": datos})
