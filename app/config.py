import os

class Config(object):
    # Base conf
    SECRET_KEY = os.environ.get('SECRET_KEY', 'a_very_secret_key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
    # Test conf
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Use an in-memory database for testing

    MONGODB_SETTINGS = {
        'db': os.environ.get('MONGODB_DB', ''),
        'host': os.environ.get('MONGODB_HOST', '')
    }

class DevelopmentConfig(Config):
    # Dev conf
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'

    MONGODB_SETTINGS = {
        'db': os.environ.get('MONGODB_DB', 'mydatabase'),
        'host': os.environ.get('MONGODB_HOST', 'mongodb://localhost:27017/mydatabase')
    }

class ProductionConfig(Config):
    # Prod conf
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/production_db'

    MONGODB_SETTINGS = {
        'db': os.environ.get('MONGODB_DB', ''),
        'host': os.environ.get('MONGODB_HOST', '')
    }
    