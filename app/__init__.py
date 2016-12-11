#!/usr/bin/env python
# encoding: utf-8


from flask import Flask
from config import config

def create_app(cfg_name):
    app = Flask(__name__)
    app.config.from_object(config[cfg_name])
    config[cfg_name].init_app(app)


    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    return app
