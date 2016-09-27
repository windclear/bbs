from . import ModelMixin
from . import db
from . import timestamp


class User(db.Model, ModelMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    created_time = db.Column(db.Integer)
    username = db.Column(db.String())
    password = db.Column(db.String())
    avatar = db.Column(db.String())
    introduction = db.Column(db.String())

    topics = db.relationship('Topic', backref="user")
    comments = db.relationship('Comment', backref="user")

    def __init__(self, form):
        super(User, self).__init__()
        self.created_time = timestamp()
        self.username = form.get('username', '')
        self.password = form.get('password', '')
        self.avatar = '/static/img/default_user.png'
        self.introduction = form.get('introduction', '')

    def validate_login(self, u):
        return u is not None and u.username == self.username and u.password == self.password

    def valid(self):
        valid_username = User.query.filter_by(username=self.username).first() is None
        valid_username_len = len(self.username) >= 3
        valid_password_len = len(self.password) >= 3
        # valid_captcha = self.captcha == '3'
        msgs = []
        if not valid_username:
            message = '用户名已经存在'
            msgs.append(message)
        if not valid_username_len:
            message = '用户名长度必须大于等于 3'
            msgs.append(message)
        if not valid_password_len:
            message = '密码长度必须大于等于 3'
            msgs.append(message)
        # elif not valid_captcha:
        #     message = '验证码必须输入 3'
        #     msgs.append(message)
        status = valid_username and valid_username_len and valid_password_len
        return status, msgs
