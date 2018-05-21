# encoding: utf-8
import math
from flask import Blueprint, jsonify, request
from application.models import TwarePaliWord
from application.models import ThePali

bp = Blueprint('pali_controller', __name__, url_prefix='/pali')

@bp.route('/meaning/<word>', methods=['GET'])
def meaning(word):
    try:
        similar = int(request.args.get('similarity', 60))/100.0
        limit = int(request.args.get('limit', 5))
    except:
        similar = 0.6
        limit = 5

    r = TwarePaliWord.query.filter_by(word=word).first()
    d = dict(success=False)
    if r:
        d['success'] = True
        meaning = {}
        for col in r.__table__.columns:
            meaning[col.name] = getattr(r, col.name)
        d['tware_meaning'] = meaning

    rs = ThePali.query.filter_by(word=word).order_by(ThePali.freq.desc()).all()
    if rs:
        d['success'] = True
        means = []
        for r in rs:
            meaning = {}
            for col in r.__table__.columns:
                meaning[col.name] = getattr(r, col.name)
            means.append(meaning)
        d['the_pali_meaning'] = means

    if not d['success']:
        # Find similar word
        n = int(math.ceil(len(word) * similar))
        prefix = word[:n]
        rs = TwarePaliWord.query.filter(TwarePaliWord.word.startswith(prefix)).limit(limit).all()
        
        means = []
        for r in rs:
            meaning = {}
            for col in r.__table__.columns:
                meaning[col.name] = getattr(r, col.name)
            means.append(meaning)
        d['similar_words'] = means
        
    return jsonify(d)

@bp.route('/meaning_v2/<word>', methods=['GET'])
def meaning_v2(word):
    try:
        similar = int(request.args.get('similarity', 60))/100.0
        limit = int(request.args.get('limit', 5))
    except:
        similar = 0.6
        limit = 5

    r = TwarePaliWord.query.filter_by(word=word).first()
    d = dict(success=False)
    if r:
        d['success'] = True
        meaning = {}
        for col in r.__table__.columns:
            meaning[col.name] = getattr(r, col.name)
        d['tware_meaning'] = meaning

    rs = ThePali.query.filter_by(word=word).order_by(ThePali.freq.desc()).all()
    if rs:
        d['success'] = True
        means = []
        for r in rs:
            meaning = {}
            for col in r.__table__.columns:
                meaning[col.name] = getattr(r, col.name)
            means.append(meaning)
        d['the_pali_meaning'] = means

    if not d['success']:
        # Find similar word
        n = int(math.ceil(len(word) * similar))
        prefix = word[:n]
        rs = TwarePaliWord.query.filter(TwarePaliWord.word.startswith(prefix)).limit(limit).all()
        
        means = []
        for r in rs:
            meaning = {}
            for col in r.__table__.columns:
                meaning[col.name] = getattr(r, col.name)
            means.append(meaning)
        d['similar_words'] = means
        
    return jsonify(d)
