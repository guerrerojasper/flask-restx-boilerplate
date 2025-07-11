from mongoengine import Document, StringField, ReferenceField, ListField, EmbeddedDocument, EmbeddedDocumentField
from .user_details import UserDocument

class CommentDocument(EmbeddedDocument):
    content = StringField(required=True)
    author = StringField(required=True)

    def to_dict(self):
        return {
            'content': self.content,
            'author': self.author
        }

class PostDocument(Document):
    """Post document."""
    meta = {
        'collection': 'post'
    }
    title = StringField(required=True)
    content = StringField(required=True)
    author = ReferenceField(UserDocument) # ReferenceField for connecting another document - relationship
    comment = ListField(EmbeddedDocumentField(CommentDocument)) # List to embedded document - relationship

    def to_dict(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'content': self.content,
            'author': {
                'id': str(self.author.id),
                'name': self.author.name,
                'email': self.author.email
            } if self.author else None,
            'comment': [
                {
                    'content': comment.content,
                    'author': comment.author
                }

                for comment in self.comment
            ]
        }