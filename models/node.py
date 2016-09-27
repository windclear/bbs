from . import ModelMixin
from . import db
from . import timestamp


class Node(db.Model, ModelMixin):
    __tablename__ = 'nodes'
    id = db.Column(db.Integer, primary_key=True)
    created_time = db.Column(db.Integer)
    name = db.Column(db.String())
    avatar = db.Column(db.String())
    introduction = db.Column(db.String())

    topics = db.relationship('Topic', backref="node", lazy='dynamic')

    def __init__(self, form):
        self.created_time = timestamp()
        self.name = form.get('nodename', '')
        self.avatar = '/static/img/default_node.png'
        self.introduction = form.get('introduction', '')
