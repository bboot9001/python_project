#!/usr/bin/env python
# encoding: utf-8

from . import main

@main.route('/')
def index():
    return '<h2>this is a main page </h2>'






