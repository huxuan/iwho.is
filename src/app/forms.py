#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: forms.py
Author: huxuan
Email: i(at)huxuan.org
Description: Forms used in app.
"""

from flask.ext.babel import gettext
from flask_wtf import Form
from wtforms import StringField

class SearchForm(Form):
    """docstring for SearchForm"""
    query = StringField()
