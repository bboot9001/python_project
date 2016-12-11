#!/usr/bin/env python
# encoding: utf-8

HOSTNAME_DEV = 'localhost'
DATABASE_DEV = 'pyblog_dev'
USERNAME_DEV = 'blog_dev'
PASSWORD_DEV = 'blog'
DB_URI_DEV = 'mysql://{}:{}@{}/{}'.format(
    USERNAME_DEV, PASSWORD_DEV, HOSTNAME_DEV, DATABASE_DEV)


