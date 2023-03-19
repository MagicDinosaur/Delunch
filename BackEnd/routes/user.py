from flask import Flask, request, jsonify, Blueprint
from models import user, childrens
user_view = Blueprint('user_routes', __name__)

@user_view.route('/api/v1/user/login', methods=['POST'])
def login():
    data = {"status": "success"}
    # do something with data
    return jsonify(data)

@user_view.route('/api/v1/user/get_child_list', methods=['GET'])
def get_child_list():
    # get child info from db
    response = {
        "status": "fail",
        "data": {
            "child_list": [
            ]
        },
        "message": "error message",
    }
    #get page and limit from request
    page_pagniation = request.get_json()
    page = page_pagniation["page"]
    limit = page_pagniation["limit"]
    child_list = childrens.get_child_list(page, limit)
    if get_child_list:
        response["status"] = "success"
        response["data"]["child_list"] = child_list
        response["message"] = "success"
    return jsonify(response)

@user_view.route('/api/v1/user/get_child_by_id')
def get_child_by_id():
    # get child info from db
    response = {
        "status": "fail",
        "data": {
            "child": {
            }
        },
        "message": "error message",
    }
    #get id from request
    id = request.get_json()["id"]
    child = childrens.get_child_by_id(id)
    if child:
        response["status"] = "success"
        response["data"]["child"] = child
        response["message"] = "success"

    return jsonify(response)

@user_view.route('/api/v1/user/make_adoption', methods=['POST'])
def make_adoption():
    response = {
        "status": "fail",
        "data": {
            "adoption_id": None
        },
        "message": "error message",
    }
    data = request.get_json()
    # do something with data
    user_id = data["user_id"]
    child_id = data["child_id"]
    adoption_id = user.make_adoption(user_id, child_id)
    if adoption_id:
        response["status"] = "success"
        response["data"]["adoption_id"] = adoption_id
        response["message"] = "success"
    return jsonify(data)


@user_view.route('/api/v1/send_view_event', methods=['GET'])
def send_view_event():
    response = {
        "status": "fail",
        "data": {
            "adoption_id": None
        },
        "message": "error message",
    }
    # do something with data
    return jsonify(response)

