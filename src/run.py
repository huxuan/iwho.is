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
    app.run(host="0.0.0.0")

if __name__ == '__main__':
    main()
