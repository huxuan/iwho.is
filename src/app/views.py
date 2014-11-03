#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: views.py
Author: huxuan
Email: i(at)huxuan.org
Description: views for app.
"""
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask.ext.babel import gettext

from app import app
from app import babel
from app import forms
from app import lib
from config import LANGUAGES

@babel.localeselector
def get_locale():
    if request.args.get('lang'):
        g.lang = request.args.get('lang')
    if g.get('lang'):
        return g.lang
    g.lang = request.accept_languages.best_match(LANGUAGES.keys())
    return g.lang

@app.route('/', methods=('GET', 'POST'))
def index():
    context = {
        'form': forms.SearchForm(),
    }
    if context['form'].validate_on_submit():
        query = lib.query_clean(context['form'].query.data)
        return redirect(url_for('whois', query=query))
    return render_template('index.html', **context)

@app.route('/whois/<query>')
def whois(query):
    context = {
        'form': forms.SearchForm(),
        'result': lib.get_whois(query)
    }
    return render_template('index.html', **context)
