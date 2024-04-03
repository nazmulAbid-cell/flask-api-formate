from flask import Blueprint, jsonify, request


test_1 = Blueprint('test1', __name__, url_prefix='/test')
test_1.version = '1.0.0-alpha' 


@test_1.route('/')
def test_route():
    return 'This is a test route form test_1'