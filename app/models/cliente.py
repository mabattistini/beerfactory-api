# -*- coding: utf-8 -*-

from app.models import db, CRUD
from lib.tools import DateTimeToStr, DataHoraAgora

class Cliente(db.Model, CRUD):

    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(200),unique=True,nullable=True)
    telefone = db.Column(db.String(20),nullable=True)
    password = db.Column(db.String(100),nullable=False)
    imagem = db.Column(db.Text,nullable=True,default="")
    token_gcm = db.Column(db.Text,nullable=True)
    status = db.Column(db.String(1),nullable=True,default='A')
    created_at = db.Column(db.DateTime, default=DataHoraAgora())
    updated_at = db.Column(db.DateTime)
    receita = db.relationship('Receita', backref='cliente', lazy='dynamic')

    def __init__(self, nome, email, telefone, password):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.password = password

    def __repr__(self):
        return '<Cliente %r>' % (self.nome)

def getClienteRecord(record):
    r = dict()
    r['id'] = record.id
    r['nome'] = record.nome
    r['email'] = record.email
    r['telefone'] = record.telefone
    r['token_gcm'] = record.token_gcm
    r['password'] = record.password
    r['imagem'] = record.imagem or ''
    r['status'] = record.status or 'A'
    r['created_at'] = DateTimeToStr(record.created_at)
    r['updated_at'] = DateTimeToStr(record.updated_at)
    return r


