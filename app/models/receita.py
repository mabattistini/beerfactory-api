# -*- coding: utf-8 -*-

from flask import current_app
from app.models import db, CRUD
from lib.tools import DateTimeToStr, DataHoraAgora

class Receita(db.Model, CRUD):

    id = db.Column(db.Integer,primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'),nullable=False)
    nome = db.Column(db.String(100),nullable=True)
    descricao = db.Column(db.Text,nullable=True)
    modo_preparo = db.Column(db.Text,nullable=True)
    imagem = db.Column(db.Text, nullable=True, default="")
    status = db.Column(db.String(1), nullable=True, default='A')
    created_at = db.Column(db.DateTime, default=DataHoraAgora())
    updated_at = db.Column(db.DateTime)
    ingrediente = db.relationship('Ingrediente', backref='receita', lazy='dynamic')
    producao = db.relationship('Producao', backref='receita', lazy='dynamic')

    def __init__(self, cliente, nome, descricao, preparo):
        self.cliente_id = cliente
        self.nome = nome
        self.descricao = descricao
        self.modo_preparo = preparo

    def __repr__(self):
        return '<Receita %r>' % (self.nome)


def getReceitaRecord(record):
    r = dict()
    r['id'] = record.id
    r['nome'] = record.nome
    r['descricao'] = record.descricao
    r['modo_preparo'] = record.modo_preparo
    if record.imagem is None:
        r['imagem'] = ''
    elif record.imagem <> '':
        r['imagem'] = current_app.config['URL_IMAGES'] + '/receitas/' + record.imagem
    else:
        r['imagem'] = ''
    r['status'] = record.status or 'A'
    r['created_at'] = DateTimeToStr(record.created_at)
    r['updated_at'] = DateTimeToStr(record.updated_at)
    return r

