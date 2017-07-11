# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask_jwt import JWT
from app.security import autenticate, identify

def create_app(config_filename):

    tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

    app = Flask(__name__, template_folder=tmpl_dir, static_folder=static_dir, static_url_path='/static')
    app.config.from_object(config_filename)
    app.secret_key = app.config['SECRET_KEY']

    jwt = JWT(app, autenticate, identify)

    from app.models import db
    db.init_app(app)

    from blueprints.main import main_blueprint
    from blueprints.user import usr_blueprint
    from blueprints.cliente import cliente_blueprint
    from blueprints.receita import receita_blueprint
    from blueprints.ingredientes import ingred_blueprint
    from blueprints.producao import prod_blueprint
    from blueprints.upload import upload_blueprint

    app.register_blueprint(blueprint=main_blueprint, url_prefix="/")
    app.register_blueprint(blueprint=upload_blueprint, url_prefix="/upload")
    app.register_blueprint(blueprint=usr_blueprint,  url_prefix="/user")
    app.register_blueprint(blueprint=cliente_blueprint,  url_prefix="/cliente")
    app.register_blueprint(blueprint=receita_blueprint,  url_prefix="/receita")
    app.register_blueprint(blueprint=ingred_blueprint,  url_prefix="/ingrediente")
    app.register_blueprint(blueprint=prod_blueprint,  url_prefix="/producao")


    return app
