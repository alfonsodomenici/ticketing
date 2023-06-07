from flask import Blueprint,jsonify,request,Response
from users_store import *
users_res = Blueprint("users_resource",__name__)

@users_res.route('/users',methods=['GET'])
def allUsers():
    return jsonify(getAllUsers())

@users_res.route('/users/<int:userId>',methods=['GET'])
def find(userId):
    found = findUserById(userId)
    if found is None:
        return Response(status=404)
    else:
        return jsonify(found)

@users_res.route('/users',methods=['POST'])
def create():
    (request.json)
    return "vuoi creare un nuovo user"

@users_res.route('/users/<int:userId>',methods=['DELETE'])
def delete(userId):
    return "vuoi eliminare lo user con id:" + str(userId)