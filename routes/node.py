from models.node import Node
from routes import *
from routes.user import current_user


main = Blueprint('node', __name__)


Model = Node


@main.route('/config')
def config():
    cu = current_user()
    ns = Model.query.all()
    return render_template('node/config.html', c_user=cu , nodes=ns)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    m = Model(form)
    m.save()
    return redirect(url_for('.config'))


@main.route('/<int:id>')
def show(id):
    u = current_user()
    m = Model.query.get(id)
    return render_template('node/show.html', c_user=u, node=m)
