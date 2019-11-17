from flask import Blueprint

queryBp = Blueprint('query', __name__,)

@queryBp.route('/', methods=['GET'])
def post():
    return 'GET /users endpoint'
