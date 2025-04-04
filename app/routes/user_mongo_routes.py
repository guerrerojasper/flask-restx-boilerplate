from flask_restx import Namespace, Resource
from mongoengine import NotUniqueError

from app import api
from app.document import UserDocument, AddressDocument
from app.schemas.user_mongo_schema import user_model, user_response_model

user_mongo_ns = Namespace(
    'user_mongo',
    description='User mongo db related operations.'
)

@user_mongo_ns.route('/')
class User(Resource):
    @user_mongo_ns.doc('list_users_mongo')
    @user_mongo_ns.marshal_with(user_response_model)
    def get(self):
        users = UserDocument.objects.all()
        print(f'Users: {users}')

        return [result.to_dict() for result in users], 200
    
    @user_mongo_ns.doc('create_user')
    @user_mongo_ns.expect(user_model, validate=True)
    @user_mongo_ns.marshal_with(user_response_model)
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
    

"""
Next learning(s):
1. relation ships
2. crud operations
"""