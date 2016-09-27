from models.node import Node
from routes import *


main = Blueprint('node', __name__)


Model = Node


@main.route('/config')
def config():
    ns = Model.query.all()
    return render_template('node/config.html', nodes=ns)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    m = Model(form)
    m.save()
    return redirect(url_for('.config'))
