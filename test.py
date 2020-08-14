#!/usr/bin/python
# -*- coding: UTF-8 -*-
fo=open("1.text","w+")
print fo.name
print fo.closed
print fo.mode
print fo.softspace
fo.write("www,runoob.com!\nVery good site!\n")
fo.close()
fo=open("1.text","r+")
str=fo.read(20)
print str
position=fo.tell()
print position
position=fo.seek(0,0)
a=fo.read(10)
print a
print position
import os
os.rename("1.py","2.py")
print os.getcwd()