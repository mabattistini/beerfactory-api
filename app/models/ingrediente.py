# -*- coding: utf-8 -*-


from app.models import db, CRUD
from lib.tools import DateTimeToStr, DataHoraAgora

unidade_descricao = {'lt':'Litro(s)','ml':'Mililitro(s)','kg':'Kilo(s)',
                     'gr':'Gramas(s)','%':'%','go':'Gota(s)','ou':'Outro'}

class Ingrediente(db.Model, CRUD):

    id = db.Column(db.Integer,primary_key=True)
    receita_id = db.Column(db.Integer,db.ForeignKey('receita.id'))
    descricao = db.Column(db.String(50), nullable=False)
    quantidade = db.Column(db.Numeric,nullable=False)
    unidade = db.Column(db.String(2),nullable=False)
    created_at = db.Column(db.DateTime, default=DataHoraAgora())
    updated_at = db.Column(db.DateTime)

    def __init__(self, receita_id, descricao,quantidade, unidade):
        self.receita_id = receita_id
        self.descricao = descricao
        self.quantidade = quantidade
        self.unidade = unidade

    def __repr__(self):
        return '<Ingrediente %r>' % (self.nome)


def getIngredienteRecord(record):
    r = dict()
    r['id'] = record.id
    r['receita_id'] = record.receita_id
    r['descricao'] = record.descricao
    r['quantidade'] = str(record.quantidade)
    r['unidade'] = record.unidade
    r['unidade_descricao'] = unidade_descricao[record.unidade]
    r['created_at'] = DateTimeToStr(record.created_at)
    r['updated_at'] = DateTimeToStr(record.updated_at)
    return r
