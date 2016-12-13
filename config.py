#!/usr/bin/env python
# encoding: utf-8
"""
    项目配置文件
"""
import os
from constsdef import DB_URI_DEV


basedir = os.path.abspath(os.path.dirname(__file__))

class ConfigBase:

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    @staticmethod
    def init_app(app):
        pass


class DevConfig(ConfigBase):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DB_URI_DEV
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True


config = {
    'development': DevConfig,
    'default': DevConfig
    }

