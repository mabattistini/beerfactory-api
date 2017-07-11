#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging, platform, os

from app import create_app

def mkDiretorio(pathDir):
    diretorios = pathDir.split(os.sep)
    pasta = ''
    drive = ''
    if pathDir.find(':') > 0:
        try:
            drive = pathDir.split(':')[0]
        except:
            pass

    if drive != "" and platform.system() == 'Windows':
        pasta = drive+":"

    for diretorio in diretorios:
        if ((platform.system() == 'Linux' and diretorio != '') or
            (platform.system() == 'Windows' and diretorio != drive+':' )):
            pasta += os.sep + diretorio
            if pasta != "":
                if not os.path.isdir(pasta):
                    os.mkdir(pasta)





app = create_app('config')

if __name__ == '__main__':

    if app.config['LOG_ACTIVE']:
        levelLog = logging.DEBUG
        if app.config['LOG_LEVEL'] == 'INFO':
            levelLog = logging.INFO
        elif app.config['LOG_LEVEL'] == 'WARNING':
            levelLog = logging.WARNING
        elif app.config['LOG_LEVEL'] == 'ERROR':
            levelLog = logging.ERROR
        elif app.config['LOG_LEVEL'] == 'CRITICAL':
            levelLog = logging.CRITICAL
        elif app.config["LOG_LEVEL"] == 'DEBUG':
            levelLog = logging.DEBUG

        if not os.path.isdir(app.config["LOG_PATH"]):
            mkDiretorio(app.config["LOG_PATH"])
        logging.basicConfig(filename=app.config["LOG_PATH"] + os.sep + app.config["LOG_FILENAME"],
                            format='%(asctime)s:%(levelname)s:%(message)s', level=levelLog)

        logging.info(u'INICIO DO PROCESSO')

    app.run(host=app.config['HOST'],
            port=app.config['PORT'],
            debug=app.config['DEBUG'])




