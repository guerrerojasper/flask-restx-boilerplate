from flask_restx import fields
from app import api

comment_model = api.model(
    'CommentDocument',
    {
        'content': fields.String(required=True, description='The comments content.'),
        'author': fields.String(required=True, description='The comments author')
    }
)

comment_response_model = api.model(
    'CommentDocument',
    {
        'content': fields.String(description='The comments content.'),
        'author': fields.String(description='The comments author')
    }
)