from flask_restx import fields
from app import api

post_model = api.model(
    'PostDocument',
    {
        'title': fields.String(required=True, description='The post title.'),
        'content': fields.String(required=True, description='The post content.'),
        'author': fields.String(required=True, description='The post email address.'),
        'comment': fields.List(fields.Raw(), description='Optional payload for comments.')
    }
)

post_response_model = api.model(
    'PostDocument',
    {
        'id': fields.String(description='The post id.'),
        'title': fields.String(description='The post title.'),
        'content': fields.String(description='The post content.'),
        'author': fields.Raw(description='The post author payload.'),
        'comment': fields.List(fields.Raw(), description='Optional payload for comments.')

    }
)