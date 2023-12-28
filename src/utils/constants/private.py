import os

# port to init App
PORT: int = os.environ.get("APP_PORT")

# debug app active
DEBUG: bool = os.environ.get("APP_DEBUG")
