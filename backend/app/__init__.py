from flask import Flask
from flask_cors import CORS
from .routes import main

def create_app():
    app = Flask(__name__)
    
    # More permissive CORS configuration
    CORS(app, resources={
        r"/*": {  # Changed from /api/* to /* to cover all routes
            "origins": [
                "https://ytvideosummarizerfrontend.vercel.app",  # Removed trailing slash
                "http://localhost:3000",
                "https://ytvideosummarizerfrontend.vercel.app"  # Added without www
            ],
            "methods": ["GET", "POST", "OPTIONS"],  # Added GET
            "allow_headers": ["Content-Type", "Authorization", "Accept", "Origin"],  # Added more headers
            "expose_headers": ["Content-Type"],
            "supports_credentials": False  # Changed to False since we're not using cookies
        }
    })

    app.register_blueprint(main)
    return app