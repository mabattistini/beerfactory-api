# -*- coding: utf-8 -*-

from flask import Blueprint, request, jsonify, current_app
import logging, os
from lib.tools import allowed_file
from werkzeug.utils import secure_filename

upload_blueprint = Blueprint('upload', __name__)



@upload_blueprint.route('/teste', methods=['GET'])
def teste():
    html = ''
    html += '<html>'
    html += '<body>'
    html += '<h1>BeerFactory Webservice</h1>'
    html += '<h3>Versão 1.0.1<br>'
    html += '(c) 2017 - Todos direitos reservados</h3>'
    html += '</body>'
    html += '</html>'

    return html


@upload_blueprint.route('/image/receita', methods=['GET','POST'])
def uploadFile():
    if request.method == 'POST':


        if 'file' not in request.files:
            logging.error(u'Request não contém um file part')
            return jsonify({'retorno': 'erro', 'mensagem': u'Não foi adicionado um arquivo'})

        file = request.files['file']

        if file.filename == '':
            logging.error(u'Não foi fornecido um arquivo')
            return jsonify({'retorno': 'erro', 'mensagem': u'Não foi adicionado um arquivo'})

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER']+os.sep+'receitas', filename))
            return jsonify({'retorno': 'sucesso', 'mensagem': u'Arquivo enviado com sucesso'})

    return '''
     <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="http://192.168.0.10:5050/upload/image/receita" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''