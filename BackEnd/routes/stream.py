from flask import Flask, request, jsonify, Blueprint
from models import user, childrens
stream_view = Blueprint('stream_routes', __name__)

@stream_view.route('/api/v1/stream/get_stream_list', methods=['GET'])
def get_stream_list():
    return "Success"
