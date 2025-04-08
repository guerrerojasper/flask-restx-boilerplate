from flask_restx import Namespace, Resource

from app import api
from app.document import PostDocument, CommentDocument, UserDocument
from app.schemas.post_mongo_schema import post_model, post_update_model, post_response_model
from app.schemas.comment_mongo_schema import comment_model, comment_response_model

post_mongo_ns = Namespace(
    'post_mongo',
    description='Post mongo related operations.'
)

@post_mongo_ns.route('/')
class Post(Resource):
    @post_mongo_ns.doc('list_post')
    @post_mongo_ns.marshal_with(post_response_model, code=200)
    def get(self):
        posts = PostDocument.objects.all().select_related()
        # Fun fact:
        # While referencefield lazy load (lazy dereferencing) the user document data when access per document
        # It is recommended to use select_related() to just load one time the related fields
        # Although referencefield also save the related data to cache for much more faster loading for future queries!
    
        return [post.to_dict() for post in posts], 200
    
    @post_mongo_ns.doc('create_post')
    @post_mongo_ns.expect(post_model, validate=True)
    @post_mongo_ns.marshal_with(post_response_model, code=201)
    def post(sel):
        data = api.payload
        user_email = data['author']
        try:
            user = UserDocument.objects.get(email=user_email)
            comments = data.pop('comment', None)
            if comments:
                data['comment'] = [CommentDocument(**comment) for comment in comments]

            post = PostDocument(
                title=data['title'],
                content=data['content'],
                author=user,
                comment=data['comment']
            )
            post.save()
        except UserDocument.DoesNotExist as e:
            post_mongo_ns.abort(404, message='The user email did not exists!')                  
        
        return [post.to_dict()], 201

@post_mongo_ns.route('/<string:id>')
@post_mongo_ns.param('id', description='The post identifier.')
class PostResource(Resource):
    @post_mongo_ns.doc('get_post')
    @post_mongo_ns.marshal_with(post_response_model, code=200)
    def get(self, id):
        try:
            post = PostDocument.objects.get(id=id)

        except PostDocument.DoesNotExist as e:
            post_mongo_ns.abort(404, message='The post does not exist!')
        
        return [post.to_dict()], 200
    
    @post_mongo_ns.doc('update_post')
    @post_mongo_ns.expect(post_update_model, validate=True)
    @post_mongo_ns.marshal_with(post_response_model, code=200)
    def put(self, id):
        try:
            data = api.payload
            post = PostDocument.objects.get(id=id)
            post.update(**data)
            post.reload()
        except PostDocument.DoesNotExist as e:
            post_mongo_ns.abort(404, message='The post does not exist!')

        return [post.to_dict()], 200
    
    @post_mongo_ns.doc('delete_post')
    def delete(self, id):
        try:
            post = PostDocument.objects.get(id=id)
            post.delete()

        except PostDocument.DoesNotExist as e:
            post_mongo_ns.abort(404, message='The post does not exist!')

        return [{'message': 'Post deleted!'}], 200
       

@post_mongo_ns.route('/<string:id>/comment')
@post_mongo_ns.param('id', description='The post identifier.')
class PostCommentResource(Resource):
    @post_mongo_ns.doc('get_comments_from_post')
    @post_mongo_ns.marshal_with(comment_response_model, code=200)
    def get(self, id):
        try:
            post = PostDocument.objects.get(id=id)
            comments = post.comment
        except PostDocument.DoesNotExist as e:
            post_mongo_ns.abort(404, message='The post does not exist!')

        return [comment.to_dict() for comment in comments], 200
  
    @post_mongo_ns.doc('post_comments')
    @post_mongo_ns.expect(comment_model, validate=True)
    @post_mongo_ns.marshal_with(post_response_model, code=200)
    def post(self, id):
        try:
            data = api.payload

            post = PostDocument.objects.get(id=id)
            comment = CommentDocument(**data)

            post.comment.append(comment) # append to ListField(Comment embedded document)
            post.save()

        except PostDocument.DoesNotExist as e:
            post_mongo_ns.abort(404, message='The post does not exists!')  

        return [post.to_dict()], 200 
