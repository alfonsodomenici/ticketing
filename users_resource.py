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
    fname = request.json['firstname']
    lname = request.json['lastname']
    user = request.json['user']
    password = request.json['password']
    year = request.json['yearBirthDate']
    created = createUser(fname,lname,user,password,year)
    return jsonify(created)

@users_res.route('/users/<int:userId>',methods=['DELETE'])
def delete(userId):
    deleteUser(userId)
    return Response(status=204)