#-*- coding: utf-8 -*-
'''
正则表达式模块学习
'''
import re

text = "JGood "+"\n""is a handsome boy, he is cool, clever, and so on..."
m = re.match(r"(\w+)\s", text)
if m:
    print m.group(0), '\n', m.group(1)
else:
    print 'not match'
