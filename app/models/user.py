# -*- coding: utf-8 -*-

from app.models import db, CRUD
from lib.tools import DateTimeToStr, DataHoraAgora

class User(db.Model, CRUD):

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    nome = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(100),nullable=False)
    created_at = db.Column(db.DateTime, default=DataHoraAgora())
    updated_at = db.Column(db.DateTime)

    def __init__(self,username, nome, password):
        self.username = username
        self.nome = nome
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.username)

def getUserRecord(record):
    r = dict()
    r['id'] = record.id
    r['username'] = record.username
    r['nome'] = record.nome
    r['password'] = record.password
    r['created_at'] = DateTimeToStr(record.created_at)
    r['updated_at'] = DateTimeToStr(record.updated_at)
    return r


