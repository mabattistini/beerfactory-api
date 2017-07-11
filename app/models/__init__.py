# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class CRUD():

    def add(self, resource,commit=True):
        db.session.add(resource)
        if commit:
            return db.session.commit()

    def update(self):
        return db.session.commit()

    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()

    def commit(self):
        return db.session.commit()

    def rollback(self):
        return db.session.rollback()
