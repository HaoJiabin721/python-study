#!/usr/bin/python
# -*- coding: UTF-8 -*-
sandwich_orders=['hao','jia','bin','bin','bin','bin']
print("Bin have been sold up!")
while 'bin' in sandwich_orders:
    sandwich_orders.remove('bin')
finished_sandwiches=[]
while sandwich_orders:
    finish=sandwich_orders.pop()
    print("I made your "+finish.title()+" sandwich")
    finished_sandwiches.append(finish)
print("\n---result----")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title()+" have been done!")

def get_formatted_name(first_name,last_name):
    full_name=first_name+' '+last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("q to quit anytime")
    f_name=raw_input("First name:")
    if f_name=='q':
        break
    l_name=raw_input("Last name:")
    if l_name=='q':
        break
    print(get_formatted_name(f_name,l_name))
