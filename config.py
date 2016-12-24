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
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[BLOG]'
    FLASKY_MAIL_SENDER = 'Blog Admin <623633583@qq.com>'
    FLASKY_ADMIN = os.environ.get('BLOG_ADMIN')
    FLASKY_POSTS_PER_PAGE = 20

    def __init__(self):
        """默认没有任何操作"""
        pass

    @staticmethod
    def init_app(app):
        """ 初始化配置文件"""
        pass


class DevConfig(ConfigBase):
    """开发配置类"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DB_URI_DEV
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


config = {
    'development': DevConfig,
    'default': DevConfig
    }

