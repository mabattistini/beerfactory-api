# -*- coding: utf-8 -*-

from flask import Blueprint,current_app, request, jsonify
import os, logging
from werkzeug.utils import secure_filename
from lib.tools import allowed_file

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/', methods=['GET'])
def main():
    html = ''
    html += '<html>'
    html += '<body>'
    html += '<h1>BeerFactory Webservice</h1>'
    html += '<h3>Versão 1.0.2<br>'
    html += '(c) 2017 - Todos direitos reservados</h3>'
    html += '</body>'
    html += '</html>'

    return html


@main_blueprint.route('/image/upload', methods=['GET','POST'])
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
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            return jsonify({'retorno': 'sucesso', 'mensagem': u'Arquivo enviado com sucesso'})

    return '''
     <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="http://192.168.0.10:5000" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''