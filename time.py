#!/usr/bin/python
# coding=UTF-8
import time
ticks = time.time()
print ticks
localtime=time.localtime(ticks)
print localtime
m=time.asctime(localtime)
print m
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print time.strftime("%a %b %d %H:%M:%S",time.localtime())
import calendar
cal=calendar.month(2020,8)
print cal
print(calendar.isleap(2020))
print(calendar.isleap(1999))
print(calendar.leapdays(1000,2000))
print(calendar.monthrange(2000,2))