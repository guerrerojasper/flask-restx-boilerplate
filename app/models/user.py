from app import db

class User(db.Model):
    __name__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, nullable=False)
    email = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'User - Name: {self.name} Email: {self.email}'