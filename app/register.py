from app import api

from app.routes.user_routes import user
from app.routes.user_mongo_routes import user_mongo_ns
from app.routes.post_mongo_routes import post_mongo_ns

def register_routes():
    
    api.add_namespace(user)
    api.add_namespace(user_mongo_ns)
    api.add_namespace(post_mongo_ns)