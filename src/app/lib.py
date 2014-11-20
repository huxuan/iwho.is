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
import threading

import ipaddr
import ipwhois
import pythonwhois
import tldextract

from app import db
from app import tasks
from whois import WHOIS_SERVER

DOMAIN_PATTERN = re.compile('^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$')
REDIS_KEY_IP = 'iwhois_ip_%s'
REDIS_KEY_DOMAIN = 'iwhois_domain_%s'

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

    domain = tldextract.extract(query)
    try:
        res = get_whois_domain(domain)
        return {
            'type': 'domain',
            'res': res,
        }
    except:
        raise

def get_whois_ip(ip):
    """docstring for get_whois_ip"""
    res = db.get(REDIS_KEY_IP % ip)
    if res:
        return res
    else:
        return get_real_whois_ip(ip)

def get_real_whois_ip(ip):
    """docstring for get_real_whois_ip"""
    ip = ipwhois.IPWhois(ip)
    res = convert_newline(ip.lookup(inc_raw=True)['raw'])
    db.set(REDIS_KEY_IP % ip, res)
    return res

def get_whois_domain(domain):
    """docstring for get_whois_domain"""
    res = db.get(REDIS_KEY_DOMAIN % domain.registered_domain)
    if res:
        thread = threading.Thread(target=get_real_whois_domain, args=[domain])
        thread.daemon = True
        tasks.put(thread)
        return res
    else:
        return get_real_whois_domain(domain)

def get_real_whois_domain(domain):
    """docstring for get_real_whois_domain"""
    server = WHOIS_SERVER.get(domain.suffix, '')
    res = pythonwhois.net.get_whois_raw(domain.registered_domain, server=server,
            never_cut=False)
    res.reverse()
    res = convert_newline('\n'.join(res))
    db.set(REDIS_KEY_DOMAIN % domain.registered_domain, res)
    return res

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
