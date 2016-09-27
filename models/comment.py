from . import ModelMixin
from . import db
from . import timestamp


class Comment(db.Model, ModelMixin):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    created_time = db.Column(db.Integer)
    content = db.Column(db.String())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))

    def __init__(self, form):
        self.created_time = timestamp()
        self.content = form.get('content', '')
        self.user_id = form.get('user_id', 0)
        self.topic_id = form.get('topic_id', 0)

