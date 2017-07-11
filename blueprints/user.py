# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, request, json
from flask_jwt import jwt_required

from app.models.user import User, getUserRecord
from lib.tools import sha224

usr_blueprint = Blueprint('user', __name__)


@usr_blueprint.route('/', methods=['GET'])
@jwt_required()
def index():
    listaRecords = User.query.all()
    lista = []
    for reg in listaRecords:
        lista.append(getUserRecord(reg))
    return jsonify({'retorno':'sucesso', 'user': lista})

@usr_blueprint.route('/add', methods=['POST'])
@jwt_required()
def add():

    if len(request.data) > 0:
        data = json.loads(request.data)
        userName = data['username']
        nome     = data['nome']
        password = data['password']

    else:
        userName = request.form.get('username')
        nome     = request.form.get('nome')
        password = request.form.get('password')


    password = sha224(password)

    newRecord = User(username=userName,nome=nome, password=password)
    newRecord.add(newRecord)
    return jsonify({'user':[{'retorno':'sucesso','id':newRecord.id}]})

@usr_blueprint.route('/login', methods=['POST'])
@jwt_required()
def login():
    return jsonify({'user': [{'retorno': 'erro','mensagem': 'Falha na indentificação'}]})