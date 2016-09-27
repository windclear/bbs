from models.topic import Topic
from models.node import Node
from routes import *
from routes.user import current_user


main = Blueprint('topic', __name__)


Model = Topic


@main.route('/new')
def new():
    u = current_user()
    ns = Node.query.all()
    return render_template('topic/new.html', c_user=u, nodes=ns)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    m = Model(form)
    m.save()
    return redirect('/')
