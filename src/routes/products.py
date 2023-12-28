# Flask features
from flask import Blueprint, json, jsonify

# Types
from utils.interfaces.datatypes import Products_Types

# bp instance
products_bp = Blueprint("products", __name__)
FILE_DATA: str = "src/examples/products.json"


# Read example products data
with open(FILE_DATA, "r") as archivo:
    datos: Products_Types = json.load(archivo)


# Get products Endpoint
@products_bp.route("/products")
def get_productos():
    return jsonify({"confirm": True, "data": datos})
