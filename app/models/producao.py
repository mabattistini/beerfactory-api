# -*- coding: utf-8 -*-

from app.models import db, CRUD
from lib.tools import DateTimeToStr, DataHoraAgora

class Producao(db.Model, CRUD):

    id = db.Column(db.Integer,primary_key=True)
    receita_id = db.Column(db.Integer,db.ForeignKey('receita.id'))
    descricao = db.Column(db.String(50), nullable=False)
    data_inicio = db.Column(db.Date, default='current_date')
    data_termino = db.Column(db.Date, nullable=True)
    densidade_inicial = db.Column(db.Numeric, nullable=True)
    densidade_final = db.Column(db.Numeric, nullable=True)
    graduacao_alcoolica = db.Column(db.Numeric, nullable=True)
    created_at = db.Column(db.DateTime, default=DataHoraAgora())
    updated_at = db.Column(db.DateTime)

    def __init__(self, receita_id, descricao):
        self.receita_id = receita_id
        self.descricao = descricao

    def __repr__(self):
        return '<Producao %r>' % (self.nome)


def getProducaoRecord(record):
    r = dict()
    r['id'] = record.id
    r['receita_id'] = record.receita_id
    r['descricao'] = record.descricao
    r['data_inicio'] = record.data_inicio
    r['data_termino'] = record.data_termino
    r['densidade_inicial'] = record.densidade_inicial
    r['densidade_final'] = record.densidade_final
    r['graduacao_alcoolica'] = record.graduacao_alcoolica
    r['created_at'] = DateTimeToStr(record.created_at)
    r['updated_at'] = DateTimeToStr(record.updated_at)
    return r
