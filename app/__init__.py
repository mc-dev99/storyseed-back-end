from flask import Flask, jsonify
from dotenv import load_dotenv
import os
from flask_cors import CORS

load_dotenv()

def create_app():
    app = Flask(__name__)

    # Register Blueprints here
    # from .routes import example_bp
    # app.register_blueprint(example_bp)
    from app.routes import decks_bp
    app.register_blueprint(decks_bp)

    CORS(app)
    return app
