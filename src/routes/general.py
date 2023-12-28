# Flask features
from flask import Blueprint

# bp instance
general_bp = Blueprint("general", __name__)


# Root Endpoint
@general_bp.route("/")
def index():
    return "Hello World with Flask!!"
