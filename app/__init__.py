#!/usr/bin/env python
# encoding: utf-8
#import sys
#sys.path.append('..')

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager
from config import config


bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'




def create_app(cfg_name):
    """创建app实例"""
    app = Flask(__name__)
    app.config.from_object(config[cfg_name])
    config[cfg_name].init_app(app)


    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint, url_prefix='/main')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    return app
