# Flask features
from flask import Flask

# general routes
from routes.general import general_bp
from routes.products import products_bp


# config App for Api
def config_app(app: Flask):
    app.register_blueprint(general_bp)
    app.register_blueprint(products_bp)
    return app
