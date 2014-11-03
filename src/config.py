#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: config.py
Author: huxuan
Email: i(at)huxuan.org
Description: Configuration for app.
"""

# flask-babel
LANGUAGES = {
    'en': 'English',
    'zh': '中文',
}

# flask-wtf
WTF_CSRF_ENABLED = True
SECRET_KEY = 'iwho.is.secret.key'
