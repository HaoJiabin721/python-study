#!/usr/bin/python
# -*- coding: UTF-8 -*-

def city_country(city,country):
    citys='"'+city+','+country+'"'
    return citys.title()
while True:
    print("输入：")
    print("按q退出")
    city_1=raw_input("输入city；")
    if city_1=='q':
        break

    country_1=raw_input("输入country：")
    if country_1=='q':
        break
    get_city_country=city_country(city_1,country_1)
    print(get_city_country)
