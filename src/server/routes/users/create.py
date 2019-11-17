from flask import Blueprint

createBp = Blueprint('create', __name__,)

@createBp.route('/', methods=['POST'])
def post():
    return 'POST /users endpoint'
