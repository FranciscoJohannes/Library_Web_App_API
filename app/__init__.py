from flask import Flask, jsonify
from config import Config
from app.extension import db, migrate, bcrypt
from app.models import user_model
from app.models import book_model
from app.models import category_model
from app.models import progress_model

from flask_smorest import Api
from app.blueprint.user_blueprint import user_blp
from app.blueprint.book_blueprint import book_blp
from app.blueprint.category_blueprint import category_blp
from app.blueprint.progress_blueprint import progress_blp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    api = Api(app)
    api.register_blueprint(user_blp)
    api.register_blueprint(book_blp)
    api.register_blueprint(category_blp)
    api.register_blueprint(progress_blp)

    @app.route('/')
    def home():
        return jsonify({"message": "Hello World"})

    return app