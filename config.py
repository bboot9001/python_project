#!/usr/bin/env python
# encoding: utf-8
"""
    项目配置文件
"""
import os
from constsdef import DB_URI_DEV


basedir = os.path.abspath(os.path.dirname(__file__))

class ConfigBase:

    @staticmethod
    def init_app(app):
        pass


class DevConfig(ConfigBase):
    DEBUG = True
    QLALCHEMY_DATABASE_URI = DB_URI_DEV

config = {
    'development': DevConfig,
    'default': DevConfig
    }

