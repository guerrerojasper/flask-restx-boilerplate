from flask_restx import fields
from app import api

user_model = api.model(
    'UserDocument',
    {
        'name': fields.String(required=True, description='The user name.'),
        'age': fields.Integer(required=True, description='The user age.'),
        'email': fields.String(required=True, description='The user email address.'),
        'address': fields.Raw(description='Optional data for address.'),
        'hobbies': fields.List(fields.String(), description='The user hobbies.')
    }
)

user_response_model = api.model(
    'UserDocumentResponse',
    {
        'id': fields.String(description='The user id.'),
        'name': fields.String(description='The user name.'),
        'age': fields.Integer(description='The user age.'),
        'email': fields.String(description='The user email address.'),
        'address': fields.Raw(description='Optional data for address.'),
        'hobbies': fields.List(fields.String(), description='The user hobbies.')
    }
)