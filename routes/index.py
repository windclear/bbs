from models.user import User
from models.node import Node
from models.topic import Topic
from routes import *
from .user import current_user

main = Blueprint('index', __name__)


@main.route('/')
def index():
    cu = current_user()
    ns = Node.query.all()
    ts = Topic.query.all()[::-1]
    return render_template('index.html', c_user=cu, nodes=ns, topics=ts)
