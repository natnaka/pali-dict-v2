# encoding: utf-8
from flask import Blueprint, jsonify
from application.models import TwarePaliWord

bp = Blueprint('pali_controller', __name__, url_prefix='/pali')

@bp.route('/meaning/<word>', methods=['GET'])
def meaning(word):
    r = TwarePaliWord.query.filter_by(word=word).first()
    d = dict(success=False)
    if r:
        d['success'] = True
        meaning = {}
        for col in r.__table__.columns:
            meaning[col.name] = getattr(r, col.name)
        d['meaning'] = meaning
    return jsonify(d)
