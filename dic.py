#!/usr/bin/python

dict = {'Name': 1, 'Age': 7, 'Class': 'First', 'm':2}

print dict['Name']
print dict['m']
dict['m']=9
dict['Age']="haojiabin"
print dict['m']
print dict['Age']
print str(dict)
del dict
m=('h','a','o')
n=(1,2,3)
dict2=dict.fromkeys(m,2)
dict3=dict.fromkeys(m,n)
dict4=dict.fromkeys(m,[1,2,3])
print dict2
print dict3
print dict4
dict5={'x':1,'y':2,'z':3}
print dict5
print dict5.setdefault('x')
print dict5.setdefault('v',4)
print dict5.values()
s=dict5.pop('x')
print s
k=dict5.popitem()
print (k)