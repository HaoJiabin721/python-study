# coding=UTF-8
alien_0={"h":"a","o":10}
print(alien_0["h"])
print(alien_0["o"])
x=alien_0["o"]
print("you just earned "+str(x)+" points!")
alien_0["x"]=0
alien_0["y"]=15
print(alien_0)

alien_1={}
alien_1["h"]=1
alien_1["a"]=2
alien_1["o"]=3
alien_1["x"]=4
alien_1["y"]=5
alien_1["n"]=6
print(alien_1)
alien_1["h"]=8
alien_1["a"]=9
print(alien_1)
alien_2={'x_position':0,'y_position':25,'speed':'slow'}
print("original x-position:"+str(alien_2['x_position']))
print("original y-position:"+str(alien_2['y_position']))
alien_2['speed']='fast'
if alien_2['speed']=='slow':
    x_increment=1
elif alien_2['speed']=='medium':
    x_increment=2
else:
    x_increment=3
alien_2['x_position']=alien_2['x_position']+x_increment
print("new x-position: "+str(alien_2['x_position']))
del alien_2['speed']
print (alien_2)
laojie={"first_name":"hao","last_name":"qingqing","age":30,"city":"shanghai"}
print(laojie)
favorite_num={
    'hao':10,
    'jia':15,
    'bin':20,
    'xiao':64,
    'yu':85,
    'nan':95,
    }
print(favorite_num)
for key, value in favorite_num.items():
    print("\n"+key)
    print(value)
user_0={
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
    'dust':"enrico",
    }
for k, v in user_0.items():
    print("\n"+k)
    print(v)
for name in user_0.keys():
    print(name.title())
for name in sorted(user_0.keys()):
    print(name.title())
for name in user_0.values():
    print(name.title())
for name in sorted(user_0.values()):
    print(name.title())
for name in set(user_0.values()):
    print(name.title())
rivers={'nile':'egypt','changjiang':'hubei','huanghe':'henan'}
for x,y in rivers.items():
    print("the "+str(x)+" through "+str(y.title())+"!")
for x in rivers.values():
    print(x)
for y in rivers.keys():
    print(y.title())
helius=['huanghe',"yinduhe"]
for name in rivers.keys():
    print(name.title())
    if name in helius:
        print ("谢谢")
    else:
        print("don't have "+str(name))
