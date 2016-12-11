#!/usr/bin/env python
# encoding: utf-8
from flask import render_template,session ,redirect,url_for,current_app
from .. import db
from ..models import User
from .forms import NameForm
from . import main




@main.route('/',methods=['GET','POST'])
def index():
    form = NameFrom()
    if form.validate_onsubmit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True

        session['known'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('index.html',form=form,name=session.get('name'),
                           known=session.get('known',False))








