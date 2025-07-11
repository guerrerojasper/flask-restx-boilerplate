from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mongoengine import MongoEngine


db = SQLAlchemy()
api = Api(
    version='1.0',
    title='My API',
    description='My Simple API',
    doc='/swagger'
)

def create_app(config_class=None):
    app = Flask(__name__)
    app.config.from_object('app.config.Config') # Load default config.Config

    if config_class: # Override config (eg. test, prod, dev)
        app.config.from_object(config_class)

    db.init_app(app)
    mongo_db = MongoEngine(app)
    api.init_app(app)

    from app.register import register_routes
    register_routes()

    migrate = Migrate(app, db)

    return app

