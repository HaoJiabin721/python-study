#!/usr/bin/python
# -*- coding: UTF-8 -*-
places={}
active=True
while active:
    name=raw_input("\nWhat's your name?")
    place=raw_input("Where do you like?")
    places[name]=place
    repeat=raw_input("Cotinue? yes/no?")
    if repeat=='no':
        active=False
print("\n---result---")
for name,place in places.items():
    print(name.title()+" love to go "+place.title())