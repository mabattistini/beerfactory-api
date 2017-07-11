# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, request, json, current_app
from flask_jwt import jwt_required
import logging

from app.models.receita import Receita, getReceitaRecord

receita_blueprint = Blueprint('receita', __name__)

@receita_blueprint.route('/', methods=['GET'])
@jwt_required()
def index():
    listaRecords = Receita.query.all()
    lista = []
    for reg in listaRecords:
        lista.append(getReceitaRecord(reg))
    return jsonify({'retorno':'sucesso', 'receita': lista,'count':len(lista)})


@receita_blueprint.route('/list', methods=['POST'])
@jwt_required()
def lista():

    if len(request.data) > 0:
        data = json.loads(request.data)
        cliente_id = data['cliente_id']
    else:
        cliente_id = request.form.get('cliente_id')

    listaRecords = Receita.query.filter_by(cliente_id=cliente_id).order_by('nome')
    lista = []
    for reg in listaRecords:
        lista.append(getReceitaRecord(reg))
    return jsonify({'retorno':'sucesso', 'receita': lista,'count':len(lista)})


@receita_blueprint.route('/save', methods=['POST'])
@jwt_required()
def gravar():

    if len(request.data) > 0:
        data = json.loads(request.data)
        cliente   = data['cliente']
        receita   = data['id']
        nome      = data['nome']
        descricao = data['descricao']
        preparo   = data['modo_preparo']
    else:
        cliente   = request.form.get('cliente')
        receita   = request.form.get('id')
        nome      = request.form.get('nome')
        descricao = request.form.get('descricao')
        preparo   = request.form.get('modo_preparo')

    try:
        if receita == -1:
            newRecord = Receita(cliente=cliente, nome=nome, descricao=descricao, preparo=preparo)
            newRecord.add(newRecord)
            return jsonify({'receita': [{'retorno': 'sucesso', 'id': newRecord.id}]})
        else:
            record = Receita.query.get(receita)
            if record is not None:
                record.nome = nome
                record.descricao = descricao
                record.modo_preparo = preparo
                record.update()
                return jsonify({'retorno': 'sucesso', 'id': record.id})
            else:
                return jsonify({'retorno':'erro','mensagem':u'Receita não encontrada'})
    except Exception as e:
        logging.error(e.message)
        return jsonify({'retorno': 'erro', 'mensagem': u'Erro na gravação da receita'})


@receita_blueprint.route('/delete', methods=['POST'])
@jwt_required()
def delete():
    if len(request.data) > 0:
        data = json.loads(request.data)
        receita = data['receita']
    else:
        receita = request.form.get('receita')

    try:
        record = Receita.query.get(receita)
        if record is not None:
            record.delete(record)
            return jsonify({'receita': [{'retorno': 'sucesso', 'id': record.id}]})
        else:
            return jsonify({'retorno': 'erro', 'mensagem': u'Não existe a Receita informada para exclusão'})
    except Exception as e:
        logging.error(e.message)
        return jsonify({'retorno': 'erro', 'mensagem': u'Erro na exclusão da Receita'})
