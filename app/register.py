from app import api

from app.routes.user_routes import user

def register_routes():
    
    api.add_namespace(user)