from flask import Flask
from flask_cors import CORS
from .config import Config
from .routes import main as main_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    # Registro de rutas
    app.register_blueprint(main_blueprint)

    return app