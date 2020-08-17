#!/usr/bin/python
# -*- coding: UTF-8 -*-
unnames=['hao','jia','bin']
names=[]
while unnames:
    name=unnames.pop()
    print("Verifying user"+name.title())
    names.append(name)
print("Pass")
for x in names:
    print(str(x.title()))
pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(str(pets))
while 'dog' in pets:
    pets.remove('dog')
print(pets)