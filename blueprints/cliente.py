# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, request, json
from flask_jwt import jwt_required

from app.models.cliente import Cliente, getClienteRecord
from lib.tools import sha224
import logging

cliente_blueprint = Blueprint('cliente', __name__)


@cliente_blueprint.route('/', methods=['GET'])
def index():
    listaRecords = Cliente.query.all()
    lista = []
    for reg in listaRecords:
        lista.append(getClienteRecord(reg))
    return jsonify({'retorno':'sucesso', 'cliente': lista,'count':len(lista)})


@cliente_blueprint.route('/registrar', methods=['POST'])
@jwt_required()
def add():
    print request.data
    if len(request.data) > 0:
        data = json.loads(request.data)
        nome     = data['nome']
        email    = data['email']
        telefone = data['telefone']
        password = data['password']
    else:
        nome     = request.form.get('nome')
        email    = request.form.get('email')
        telefone = request.form.get('telefone')
        password = request.form.get('password')

    password = sha224(password)

    try:
        newRecord = Cliente(nome=nome, email=email, telefone=telefone, password=password)
        newRecord.add(newRecord)
        return jsonify({'cliente': [{'retorno': 'sucesso', 'id': newRecord.id}]})
    except Exception as e:
        loggin.error(e.message)
        return json.jsonify([{'code':600,'retorno': 'erro','mensagem':e.message}]),600


@cliente_blueprint.route('/altera/dados', methods=['POST'])
@jwt_required()
def alteraDados():

    if len(request.data) > 0:
        data = json.loads(request.data)
        id     = data['id']
        nome     = data['nome']
        email    = data['email']
    else:
        id       = request.form.get('id')
        nome     = request.form.get('nome')
        email    = request.form.get('email')

    editRecord = Cliente.query().get(id)
    editRecord.nome = nome
    editRecord.email = email
    editRecord.update()
    return jsonify({'cliente': [{'retorno': 'sucesso', 'id': editRecord.id}]})

@cliente_blueprint.route('/altera/senha', methods=['POST'])
@jwt_required()
def alteraSenha():

    if len(request.data) > 0:
        data = json.loads(request.data)
        id       = data['id']
        password = data['password']
    else:
        id       = request.form.get('id')
        password = request.form.get('password')

    password = sha224(password)

    editRecord = Cliente.query().get(id)
    editRecord.password = password
    editRecord.update()
    return jsonify({'cliente': [{'retorno': 'sucesso', 'id': editRecord.id}]})



@cliente_blueprint.route('/login',methods=['POST'])
@jwt_required()
def login():

    if len(request.data) > 0:
        data = json.loads(request.data)
        email    = data['email']
        password = data['password']
        token_notification = data['token_notification']
    else:
        email    = request.form.get('email')
        password = request.form.get('password')
        token_notification = request.form.get('token_notification')

    password = sha224(password)

    record = Cliente.query.filter_by(email=email).filter_by(password=password).first()
    if record is not None:
        if record.password == password:
            #record.token_gcm = token_notification
            #record.update()
            return jsonify({'cliente': [{'retorno': 'sucesso', 'data': getClienteRecord(record)}]})

    return jsonify({'user': {'retorno': 'erro', 'mensagem': u'Falha na indentificação'}})

