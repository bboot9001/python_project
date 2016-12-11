#!/usr/bin/env python
# encoding: utf-8
#import sys
#sys.path.append('..')

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config


bootstrap = Bootstrap()
db = SQLAlchemy()




def create_app(cfg_name):
    app = Flask(__name__)
    app.config.from_object(config[cfg_name])
    config[cfg_name].init_app(app)


    bootstrap.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    return app
