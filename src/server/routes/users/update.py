from flask import Blueprint

updateBp = Blueprint('update', __name__)

@updateBp.route('/<id>', methods=['PUT'])
def put(id):
    return 'PUT /users/' + id + 'endpoint'
