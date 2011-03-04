#!/usr/bin/python
# vim: set fileencoding=utf-8
# -*- coding: utf-8 -*-

from os import *
from sys import *

def trans(a):
	baseA = ord(u'A')
	basea = ord(u'a')

	diff = ord(a) - ord(u'Ａ')
	if ( diff >= 0 and diff <= 25 ):
		return unichr(diff+baseA)

	diff = ord(a) - ord(u'ａ')
	if ( diff >= 0 and diff <= 25 ):
		return unichr(diff+basea)

	if  ( a == u'　'):
		return u' '
	elif( a == u'’'):
		return u'\''
	elif( a == u'｜'):
		return u'|'
	elif( a == u'（'):
		return u'('
	elif( a == u'）'):
		return u')'
	return a

name=argv[1].decode('utf-8')
new_name=u""
for i in name:
	new_name = new_name + trans(i)

print new_name
