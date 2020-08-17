#!/usr/bin/python
# -*- coding: UTF-8 -*-
def greet_users(names):
    for name in names:
        msg="Hello "+name
        print(msg.title())
m=['hao','jia','bin']
greet_users(m)