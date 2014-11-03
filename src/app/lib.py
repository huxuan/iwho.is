#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: lib.py
Author: huxuan
Email: i(at)huxuan.org
Description: library used in app.
"""
import re
import socket

import ipaddr
import ipwhois
import pythonwhois

DOMAIN_PATTERN = re.compile('^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$')

def get_whois(query):
    """docstring for get_whois"""
    # Check whether it is a valid ip address
    try:
        ip = ipaddr.IPAddress(query)
        res = get_whois_ip(query)
        return {
            'type': 'ip',
            'res': res,
        }
    except ValueError:
        pass

    domain = '.'.join(query.split('.')[-2:])
    try:
        res = get_whois_domain(domain)
        return {
            'type': 'domain',
            'res': res,
        }
    except:
        pass

def get_whois_ip(ip):
    """docstring for get_whois_ip"""
    ip = ipwhois.IPWhois(ip)
    res = ip.lookup(inc_raw=True)['raw']
    return convert_newline(res)

def get_whois_domain(domain):
    """docstring for get_whois_domain"""
    res = pythonwhois.net.get_whois_raw(domain)
    res.reverse()
    res = '\n'.join(res)
    return convert_newline(res)

def convert_newline(s):
    s = s.replace('\r\n', '<br/>')
    s = s.replace('\n', '<br/>')
    return s

def query_clean(query):
    """docstring for query_clean"""
    query = query.strip()
    query = query.replace('http://','')
    query = query.replace('https://','')
    if query[-1] == '/':
        query = query[:-1]
    return query
