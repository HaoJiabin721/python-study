#!/usr/bin/python
# -*- coding: UTF-8 -*-
list=[]
list.append('haojiabin')
list.append('yunanluo')
list.append('jiajia')
print list
del list[2]
print list
print "h" in list
for m in list:print m
print len(list)
print list*3

def pets(first_name,last_name,middle_name=''):
    if middle_name:
        full_name=first_name+' '+middle_name+' '+last_name
    else:
        full_name=first_name+' '+last_name
    return full_name.title()
def persons(first_name,last_name,middle_name=''):
    if middle_name:
        person={'first':first_name,"middle":middle_name,'last':last_name}
    else:
        person = {'first': first_name, 'last': last_name}
    return person
while True:
    a=raw_input("First-name:")
    b=raw_input("Middle-name:")
    c=raw_input("Last-name:")
    msg=pets(a,c,b)
    msc=persons(a,c,b)
    print(msg)
    print(msc)