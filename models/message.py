from . import ModelMixin
from . import db
from . import timestamp


class Message(db.Model, ModelMixin):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    created_time = db.Column(db.Integer)
    content = db.Column(db.String())

    def __init__(self, form):
        self.created_time = timestamp()
        self.content = form.get('content', '')
