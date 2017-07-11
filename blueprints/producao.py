# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, request, json
from flask_jwt import jwt_required

from app.models.producao import Producao, getProducaoRecord

prod_blueprint = Blueprint('producao', __name__)

@prod_blueprint.route('/', methods=['GET'])
@jwt_required()
def index():
    listaRecords = Producao.query.all()
    lista = []
    for reg in listaRecords:
        lista.append(getProducaoRecord(reg))
    return jsonify({'retorno':'sucesso', 'producao': lista,'count':len(lista)})
