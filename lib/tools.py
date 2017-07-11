# -*- coding: utf-8 -*
from flask import current_app
import  subprocess
import datetime
import hashlib


def DataHoraAgora():
    return datetime.datetime.now()

def DateTimeToStr(dtm):
    if dtm is not None:
        return datetime.datetime.strftime(dtm, '%d/%m/%Y %H:%M:%S')
    else:
        return ''


def SystemCmd(command):

    commandStr = []
    for c in command.split(' '):
        commandStr.append(c)
    r = subprocess.check_output(commandStr)
    return r

def sha224(text):
    r =  hashlib.sha224(text).hexdigest()
    return r

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']