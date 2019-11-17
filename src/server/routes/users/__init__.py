from .create import createBp
from .get import getBp
from .update import updateBp
from .delete import deleteBp
from .query import queryBp

def registerUsersBlueprints(app):
    app.register_blueprint(createBp, url_prefix='/users')
    app.register_blueprint(updateBp, url_prefix='/users')
    app.register_blueprint(deleteBp, url_prefix='/users')
    app.register_blueprint(getBp, url_prefix='/users')
    app.register_blueprint(queryBp, url_prefix='/users')
