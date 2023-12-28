# Flask features
from flask import Flask

# Constants
from utils.constants.private import PORT, DEBUG

# Routes
from config import config_app

# flask instance
app_flask = Flask(__name__)

# config_app instance
app = config_app(app_flask)

# Start App
if __name__ == "__main__":
    app.run(debug=DEBUG, port=PORT)
