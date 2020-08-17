#!/usr/bin/python
# -*- coding: UTF-8 -*-
responses={}
polling_active=True
while polling_active:
    name=raw_input("\nWhat's your name?")
    response=raw_input("Which mountain would you like to climb someday?")
    responses[name]=response

    repeat=raw_input("yes/no?")
    if repeat=='no':
        polling_active=False
print("\n---Poll results---")
for name,response in responses.items():
    print(name.title()+" would like to climb "+response.title()+".")