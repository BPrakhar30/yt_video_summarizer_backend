from flask import Flask
from flask_cors import CORS
# from config import Config
from .routes import main

def create_app():
    app = Flask(__name__)
    
    CORS(app, resources={
        r"/api/*": {
            "origins": [
                "https://ytvideosummarizerfrontend.vercel.app/",
                "http://localhost:3000"
            ],
            "methods": ["OPTIONS", "POST"],
            "allow_headers": ["Content-Type"],
            "expose_headers": ["Content-Type"],
            "supports_credentials": True
        }
    })

    # app.config.from_object(Config)

    app.register_blueprint(main)

    return app 