from flask import Blueprint, jsonify, request
from . import db
from .models import User

main = Blueprint('main', __name__)


@main.route('/user', methods=['POST'])
def add_user():
    user_data = request.get_json()
    new_user = User(name=user_data['name'], email=user_data['email'])
    db.session.add(new_user)
    db.session.commit()
    return user_data


@main.route('/users')
def users():
    users_list = User.query.all()
    users = []
    for user in users_list:
        users.append({'name': user.name, 'email': user.email})
    return jsonify({'users': users})
