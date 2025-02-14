from flask import Blueprint, jsonify
from app.handlers.user_handler import get_users

api = Blueprint('api', __name__)

@api.route('/users', methods=['GET'])
def users():
    return jsonify(get_users()), 200
