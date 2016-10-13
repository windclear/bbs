from models.node import Node
from routes import *
from routes.user import current_user

from functools import wraps

main = Blueprint('node', __name__)


Model = Node


def admin_required(f):
    @wraps(f)
    def function(*args, **kwargs):
        # print('admin required')
        if current_user().id != 1:
            # print('not admin')
            abort(404)
        return f(*args, **kwargs)
    return function


@main.route('/config')
@admin_required
def config():
    cu = current_user()
    ns = Model.query.all()
    return render_template('node/config.html', c_user=cu , nodes=ns)


@main.route('/add', methods=['POST'])
@admin_required
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
