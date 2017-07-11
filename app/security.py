# -*- coding: utf-8 -*-

from werkzeug.security import safe_str_cmp
from app.models.user import User
from lib.tools import sha224

def autenticate(username, password):

    user = User.query.filter_by(username=username).first()
    if user and  safe_str_cmp(user.password , sha224(password)):
        return user
    else:
        return None


def identify(payload):
    user_id = payload['identity']
    user = User.query.get(user_id)
    return user

