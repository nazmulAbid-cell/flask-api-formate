from flask import Blueprint, jsonify, request


test = Blueprint('test', __name__, url_prefix='/test')
test.version = '1.0.0-alpha' 


@test.route('/test')
def test_route():
    return 'This is a test route'