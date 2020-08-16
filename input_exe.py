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

