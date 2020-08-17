#!/usr/bin/python
# -*- coding: UTF-8 -*-
# def make_album(names,pyths,musics=""):
#    if music:
#         persons={'first':names,'last':pyths,'music':musics}
#         return persons
#    else:
#        persons = {'first': names, 'last': pyths}
#        return persons
# while True:
#     print("names:")
#     print("pyths:")
#     name = raw_input("name?")
#     if name=='q':
#         break
#     pyth = raw_input("pyths?")
#     if pyth=='q':
#         break
#     music = raw_input("music?")
#     if pyth=='q':
#         break
#
#     album=make_album(name,pyth)
#     print(album)
#     album = make_album(name, pyth, music)
#     print(album)
#
# def greet_users(names):
#     for name in names:
#         msg="hello! "+name.title()+"!"
#         print(msg)
# usernames=['hao','jia','bin']
# greet_users(usernames)
#
# names=["hao","jia",'bin']
# name1=[]
# # def show_magicians(ww):
#     for name in ww:
#         print(name.title())
# def make_great(name):
#     #for name in names:
#     for i in range(len(names)):
#         names[i]="The Great "+names[i].title()
#         print(names[i])
#     #return names

# def AAA(qqq):
#     for name in qqq:
#       name = "The Great " + name
#       name1.append(name)
#
#
# AAA(names)
# for n in name1:
#     print(n.title())
# # show_magicians(name1)
from male_pizza import make_pizza as sb
s=sb('hao','jia',bin='hao',yu='nan')
print(s)
from bianli import greet_users as sm
n=['hao','jia','bin']
sm(n)