from flask_restx import fields
from app import api

user_model = api.model(
    'User', 
    {
        'id': fields.Integer(readOnly=True, description='The user ID'),
        'name': fields.String(required=True, description='The user name'),
        'email': fields.String(required=True, description='The user email')
    }
)

user_response_model = api.model(
    'UserResponse', 
    {
        'id': fields.Integer(description='The user ID'),
        'name': fields.String(description='The user name'),
        'email': fields.String(description='The user email')
    }
)
