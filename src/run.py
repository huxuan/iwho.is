#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: run.py
Author: huxuan
Email: i(at)huxuan.org
Description: run script for app.
"""
import sys

from app import app

def main():
    """docstring for main"""
    if sys.argv[0] != 'uwsgi':
        app.debug = True
#     if app.debug:
#         import logging
#         from logging.handlers import FileHandler
#         file_handler = TheHandlerYouWant(...)
#         file_handler.setLevel(logging.WARNING)
#         app.logger.addHandler(file_handler)
    app.run(host="0.0.0.0", debug=True)

if __name__ == '__main__':
    main()
