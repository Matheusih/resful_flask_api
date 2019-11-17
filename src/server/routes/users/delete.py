from flask import Blueprint

deleteBp = Blueprint('delete', __name__,)

@deleteBp.route('/<id>', methods=['DELETE'])
def delete(id):
    return 'DELETE /users/' + id + ' endpoint'
