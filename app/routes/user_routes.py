from flask_restx import Namespace, Resource
from app.models.user import User
from app.schemas.user_schema import user_model, user_response_model

from app import api, db

user = Namespace(
    'users',
    description='User related operations.'
)

@user.route('/')
class UserList(Resource):
    @user.doc('list_users')
    @user.marshal_with(user_response_model)
    def get(self):
        users = User.query.all()

        return users, 200
    
    @user.doc('create_user')
    @user.expect(user_model, validate=True)
    @user.marshal_with(user_response_model)
    def post(self):
        data = api.payload
        user = User(
            name=data['name'],
            email=data['email']
        )

        db.session.add(user)
        db.session.commit()

        return user, 201
        