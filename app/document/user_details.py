from mongoengine import Document, StringField, IntField, EmailField, EmbeddedDocument, EmbeddedDocumentField, ListField

class AddressDocument(EmbeddedDocument):
    """An embedded document for storing address details."""
    city = StringField(required=True)
    zip_code = StringField(required=True)

class UserDocument(Document):
    """A user document."""
    meta = {
        'collection': 'user'
    }
    name = StringField(required=True, max_length=100)
    age = IntField(required=True, min_value=0, max_value=150)
    email = EmailField(required=True, unique=True)
    address = EmbeddedDocumentField(AddressDocument) # embed address document
    hobbies = ListField(StringField()) # a list of hobbies

    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'age': self.age,
            'email': self.email,
            'address': {
                'city': self.address.city,
                'zip_code': self.address.zip_code
            } if self.address else None,
            'hobbies': self.hobbies
        }