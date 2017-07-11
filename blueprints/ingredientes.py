# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, request, json
from flask_jwt import jwt_required
import logging

from app.models.ingrediente import Ingrediente, getIngredienteRecord

ingred_blueprint = Blueprint('ingrediente', __name__)

@ingred_blueprint.route('/', methods=['GET'])
@jwt_required()
def index():
    listaRecords = Ingrediente.query.all()
    lista = []
    for reg in listaRecords:
        lista.append(getIngredienteRecord(reg))
    return jsonify({'retorno':'sucesso', 'ingredientes': lista,'count':len(lista)})

@ingred_blueprint.route('/save', methods=['POST'])
@jwt_required()
def add():

    if len(request.data) > 0:
        data = json.loads(request.data)
        receita     = data['receita']
        ingrediente = data['ingrediente']
        produto     = data['produto']
        quantidade  = data['quantidade']
        unidade     = data['unidade']
    else:
        receita     = request.form.get('receita')
        ingrediente = request.form.get('receita')
        produto     = request.form.get('produto')
        quantidade  = request.form.get('quantidade')
        unidade     = request.form.get('unidade')

    try:
        if ingrediente == -1:
            newRecord = Ingrediente(receita_id=receita,descricao=produto,quantidade=quantidade,unidade=unidade)
            newRecord.add(newRecord)
            return jsonify({'ingrediente': [{'retorno': 'sucesso', 'id': newRecord.id}]})
        else:
            record = Ingrediente.query.get(ingrediente)
            if record is not None:
                record.descicao = produto
                record.quantidade = quantidade
                record.unidade = unidade
                record.update()
                return jsonify({'ingrediente': [{'retorno': 'sucesso', 'id': record.id}]})
    except Exception as e:
        logging.error(e.message)
        return jsonify({'retorno': 'erro', 'mensagem': u'Erro na gravação do ingrediente'})


@ingred_blueprint.route('/delete', methods=['POST'])
@jwt_required()
def delete():
    if len(request.data) > 0:
        data = json.loads(request.data)
        ingrediente = data['ingrediente']
    else:
        ingrediente = request.form.get('ingrediente')

    try:
        record = Ingrediente.query.get(ingrediente)
        if record is not None:
            record.delete(record)
            return jsonify({'ingrediente': [{'retorno': 'sucesso', 'id': record.id}]})
        else:
            return jsonify({'retorno': 'erro', 'mensagem': u'Não existe o Ingrediente informado para exclusão'})
    except Exception as e:
        logging.error(e.message)
        return jsonify({'retorno': 'erro', 'mensagem': u'Erro na exclusão do ingrediente'})


@ingred_blueprint.route('/list', methods=['POST'])
@jwt_required()
def list():

    if len(request.data) > 0:
        data = json.loads(request.data)
        receita = data['receita']
    else:
        receita = request.form.get('receita')

    listaRecords = Ingrediente.query.filter_by(receita_id=receita).order_by('descricao')
    lista = []
    for reg in listaRecords:
        lista.append(getIngredienteRecord(reg))
    return jsonify({'retorno': 'sucesso', 'ingrediente': lista, 'count': len(lista)})

