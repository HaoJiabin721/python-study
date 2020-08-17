#!/usr/bin/python
# -*- coding: UTF-8 -*-
Class Dog():
    def _init_(self,name,age):
        self.name=name
        self.age=age

    def sit(self):
        print(self.name.title()+" is now sitting.")

    def roll_over(self):
        print(self.name.title()+" rolled over!")