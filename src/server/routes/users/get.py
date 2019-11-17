from flask import Blueprint

getBp = Blueprint('get', __name__,)

@getBp.route('/<id>', methods=['GET'])
def get(id):
    return 'GET /users/' + id + 'endpoint'

