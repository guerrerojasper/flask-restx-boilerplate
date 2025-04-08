from flask_restx import Namespace, Resource
from mongoengine import NotUniqueError, DoesNotExist

from app import api
from app.document import UserDocument, AddressDocument, PostDocument
from app.schemas.user_mongo_schema import user_model, user_response_model
from app.schemas.post_mongo_schema import post_response_model

user_mongo_ns = Namespace(
    'user_mongo',
    description='User mongo db related operations.'
)

@user_mongo_ns.route('/')
class User(Resource):
    @user_mongo_ns.doc('list_users_mongo')
    @user_mongo_ns.marshal_with(user_response_model, code=200)
    def get(self):
        users = UserDocument.objects.all()

        return [result.to_dict() for result in users], 200
    
    @user_mongo_ns.doc('create_user')
    @user_mongo_ns.expect(user_model, validate=True)
    @user_mongo_ns.marshal_with(user_response_model, code=201)
    def post(self):
        data = api.payload
        address_data = data.pop('address', None)
        if address_data:
            data['address'] = AddressDocument(**address_data)
        
        try:
            user = UserDocument(**data)
            user.save()
        
        except NotUniqueError as e:
            user_mongo_ns.abort(409, message='Email already exists! Please use another email.')
        
        except Exception as e:
            user_mongo_ns.abort(400, message=str(e))

        return user.to_dict(), 201
    
@user_mongo_ns.route('/<string:id>')
@user_mongo_ns.param('id', description='The user identifier.')
class UserResource(Resource):
    @user_mongo_ns.doc('get_single_user')
    @user_mongo_ns.marshal_with(user_response_model, code=200)
    def get(self, id):
        try:
            user = UserDocument.objects.get(id=id)
        except UserDocument.DoesNotExist as e:
            user_mongo_ns.abort(404, message='User does not exist!')

        return [user.to_dict()], 200

    @user_mongo_ns.doc('update_user_details')
    @user_mongo_ns.expect(user_model, validate=True)
    @user_mongo_ns.marshal_with(user_response_model, code=200)
    def put(self, id):
        try:
            data = api.payload
            user = UserDocument.objects.get(id=id)
            user.update(**data)
            user.reload() # reload the document

        except UserDocument.DoesNotExist as e:
            user_mongo_ns.abort(404, message='User does not exist!')

        return [user.to_dict()], 200
    
    @user_mongo_ns.doc('delete_user')
    def delete(self, id):
        try:
            user = UserDocument.objects.get(id=id)
            user.delete()

        except UserDocument.DoesNotExist as e:
            user_mongo_ns.abort(404, message='User does not exist!')

        return [{'message': 'User deleted'}], 200

@user_mongo_ns.route('/<string:id>/posts')
@user_mongo_ns.param('id', description='The user identifier.')
class UserPostResource(Resource):
    @user_mongo_ns.doc('get_user_posts')
    @user_mongo_ns.marshal_with(post_response_model, code=200)
    def get(self, id):
        try:
            user = UserDocument.objects.get(id=id) # .get will get 1 object only
            posts = PostDocument.objects(author=user) # .objects will return all data

        except UserDocument.DoesNotExist as e:
            user_mongo_ns.abort(404, message='User does not exist!')
        
        return [post.to_dict() for post in posts], 200