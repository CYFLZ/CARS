from flask import Blueprint, jsonify
from Controllers.UserController import user_controller

us_bp = Blueprint('user_bp', __name__)

@us_bp.route('/', methods=['GET'])
def listUsers():
    x = user_controller.listUsers()
    return x

@us_bp.route('/', methods=['POST'])
def createUser():
    x = user_controller.addUser()
    return x

@us_bp.route('/', methods=['PUT'])
def updateUser():
    return ""

@us_bp.route('/', methods=['DELETE'])
def deleteUser():
    return ""

# http://128.9.9.9/user/
# http://128.9.9.9/user/create
# http://128.9.9.9/user/edit