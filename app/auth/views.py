#!/usr/bin/env python
# encoding: utf-8


from . import auth

@auth.route('/login')
def login():
    return '<h2>this is a login page</h2>'
