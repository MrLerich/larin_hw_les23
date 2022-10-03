import os
from flask import Flask

from views import app_bp

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


def create_application():
    """Создает приложение и регистрирует blueprint"""
    app = Flask(__name__)
    app.register_blueprint(app_bp)

    return app





