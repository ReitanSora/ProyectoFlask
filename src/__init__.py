from flask import Flask
from src.routes import HomeRoutes

app = Flask(__name__)

def init_app(config):

    app.config.from_object(config)

    # Blueprints
    app.register_blueprint(HomeRoutes.main, url_prefix = '/')
    
    return app