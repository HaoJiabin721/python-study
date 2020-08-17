#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 定义函数
def x(str):
    "打印任何传入的字符串"
    print str
    return


# 调用函数
x("我要调用用户自定义函数!")
x("再次调用同一函数")
def m(x,y=3):
    print x
    print y
    return
m(x=1,y=2)
m(x=3)
def n(a,*vartuple):
    print a
    for var in vartuple:
        print var
        return
n(11)
n(12,13,14)
sum=lambda arg1,arg2:arg1+arg2
print sum(1,2)
print sum(3,4)
Money = 2000


def AddMoney():
    # 想改正代码就取消以下注释:
    global Money
    Money = Money + 1


print Money
AddMoney()
print Money
from package_runoob.runoob1 import runoob1
from package_runoob.runoob2 import runoob2

runoob1()
runoob2()