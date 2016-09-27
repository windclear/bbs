from models.comment import Comment
from models.node import Node
from routes import *
from routes.user import current_user


main = Blueprint('comment', __name__)


Model = Comment


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    m = Model(form)
    m.save()
    return redirect(url_for('topic.show', id=m.topic_id))

