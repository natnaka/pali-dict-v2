# encoding: utf-8
from flask import Blueprint

bp = Blueprint('test_controller', __name__, url_prefix='/')

@bp.route('', methods=['GET'])
def index():
    return 'Very Successful!!!', 200
