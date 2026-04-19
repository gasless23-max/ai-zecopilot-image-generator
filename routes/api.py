from flask import Blueprint

api = Blueprint('api', __name__)

@api.route('/users', methods=['GET'])
def get_users():
    return {'users': []}
