from flask import Flask, request, jsonify, Blueprint

user_view = Blueprint('routes', __name__)

@user_view.route('/api/v1/login', methods=['POST'])
def login():
    data = request.get_json()
    # do something with data
    return jsonify(data)

@user_view.route('/api/v1/get_childs_list', methods=['GET'])
def get_childs_list():
    # get child info from db
    response = {
        "id": 1,
        "name": "John",
        "age": 5,
        "description" : "hello testing!!"}
    return jsonify(response)

@user_view.route('/api/v1/send_view_event', methods=['POST'])
def send_view_event():
    data = request.get_json()
    # do something with data
    return jsonify(data)

