from flask_restx import Namespace, Resource

from app import api
from app.document import PostDocument, UserDocument
from app.schemas.post_mongo_schema import post_model, post_response_model

post_mongo_ns = Namespace(
    'post_mongo',
    description='Post mongo related operations.'
)

@post_mongo_ns.route('/')
class Post(Resource):
    @post_mongo_ns.doc('list_post')
    @post_mongo_ns.marshal_with(post_response_model)
    def get(self):
        posts = PostDocument.objects.all().select_related()
        # Fun fact:
        # While referencefield lazy load (lazy dereferencing) the user document data when access per document
        # It is recommended to use select_related() to just load one time the related fields
        # Although referencefield also save the related data to cache for much more faster loading for future queries!
    
        return [post.to_dict() for post in posts], 200
    
    @post_mongo_ns.doc('create_post')
    @post_mongo_ns.expect(post_model, validate=True)
    @post_mongo_ns.marshal_with(post_response_model)
    def post(sel):
        data = api.payload
        user_email = data['author']

        user = UserDocument.objects.get(email=user_email)
        if user:
            post = PostDocument(
                title=data['title'],
                content=data['content'],
                author=user,
                comment=data['comment']
            )
            post.save()

        else:
            post_mongo_ns.abort(404, message='The user email did not exists!')
        
        return [post.to_dict()], 201
