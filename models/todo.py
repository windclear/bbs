from . import ModelMixin
from . import db
from . import timestamp


class Todo(db.Model, ModelMixin):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    created_time = db.Column(db.Integer)
    task = db.Column(db.String())

    def __init__(self, form):
        self.task = form.get('task', '')
        self.created_time = timestamp()

    def update(self, form):
        self.task = form.get('task', '')
        self.save()
