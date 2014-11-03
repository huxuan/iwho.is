#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: __init__.py
Author: huxuan
Email: i(at)huxuan.org
Description: Initialization for app.
"""

from flask import Flask
from flask.ext.babel import Babel
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object('config')
babel = Babel(app)
Bootstrap(app)

from app import views
