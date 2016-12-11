#!/usr/bin/env python
# encoding: utf-8


from flask_wtf import Form

from wtforms import StringField,SubmitField
from etforms.validators import Required

class NameForm(Form):
    name = StringField('what is your name?',validators=[Required()])
    submit = SubmitField('Submit')
