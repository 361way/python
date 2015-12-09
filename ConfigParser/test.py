#!/usr/bin/env python
# coding=utf-8
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('test.ini')

print parser.get('site', 'url')
