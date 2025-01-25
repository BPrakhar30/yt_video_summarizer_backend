from flask import Flask
from flask_cors import CORS
# from config import Config
from .routes import main

def create_app():
    app = Flask(__name__)
    CORS(app)
    # app.config.from_object(Config)

    app.register_blueprint(main)

    return app 