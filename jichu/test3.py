# coding=UTF-8
bs=list(range(1,21,2))
print(bs)
jss=[]
for js in range(1,21,2):
    jss.append(js)
print(jss)
hss=[]
for hs in range(3,31,3):
    hss.append(hs)
print(hss)
ass=[]
for as1 in range(1,11):
    ass.append(as1**3)
print (ass)
ass=[as1**3 for as1 in range(1,11)]
print(ass)
oss=[ose*3 for ose in range(2,20)]
print(oss)
print(oss[0])
print(oss[0:3])
print(oss[-3:])
my_foods=["bana","apple","orange"]
friend_foods=my_foods[:]
print(friend_foods)
print(my_foods)
my_foods.append("blue")
friend_foods.append('yellow')
print(friend_foods)
print(my_foods)
for s in my_foods:
    print(s)
for m in friend_foods:
    print(m)
zizu_foods=("mantou","yumi","tang","noodle","xiaocai")
for zizu in zizu_foods:
    print(zizu)
zizu_foods=("mantou","xiamu","dsaas","asda","xiaocai")
for zizu in zizu_foods:
    print(zizu)
nans=['hao','jia','bin','xiao','yu','nan']
for nan in nans:
    if nan=='nan':
        print(nan.upper())
    else:
        print(nan.title())
h='cars'
if h=='subaru':
    print"Is cars==subaru?I predict True."
    print(h=='subaru')
if h!='subaru':
    print"Is cars!=subaru? I predict True."
a="cars"
b="buss"
c="BuSS"
d="Cars"
print(a==b)
print(a!=b)
print(b==c)
print(c.lower()==b)
print(a==d)
print(a==d.lower())
x=3
y=4
if x>y:
    print ("false")
else:
    print("true")
print(x!=y)
print(x<=y)
if x>=1 and y>=1:
    print("false")
else:
    print('True')
ms=[1,2,3,4,5,6]
n=3
if n in ms:
    print ("n in ms")
else:
    print("n not in ms")
m=7
if m not in ms:
    print("m not in ms")
else:
    print("m in ms")
age=13
if age>18:
    x=0
elif age>12:
    x=10
else:
    x=20
print("your price is "+str(x)+"!")
alien_color=["green","yellow","red"]
if "green" in alien_color:
    print ("玩家获得了5个点")
if "red" in alien_color:
    print("玩家获得5个点")
else:
    print ("玩家获得0个点")
if "green" in alien_color:
    print("玩家获得5个点")
else:
    print("玩家获得10个点")
if "red" in alien_color:
    print("玩家获得15个点")
age=3
if age<2:
    print("他是婴儿")
elif age<4:
    print("他正蹒跚学步")
elif age<13:
    print("他是儿童")
elif age<20:
    print("他是青少年")
elif age<65:
    print("他是成年人")
elif age>=65:
    print("他是老年人")
favorite_food=["h","a","o"]
if "h" in favorite_food:
    print("you are h")
if "a" in favorite_food:
    print("you are a")
if "o" in favorite_food:
    print("you are o")
hs=["h","a","o"]
for h in hs:
    print("Add"+h+".")
print("\nFinished making my pizza!")
oss=["h","a","o"]
for os in oss:
    if os=="h":
        print("sorry,we have no "+str(os))
    else:
        print("OK,we have "+str(os))
print("Finish")
hss=["h","a","o","admin"]
if hss:
    for hs in hss:
        if hs=="admin":
            print("hello,admin,would you like to see a status report?")
        else:
            print("hello,"+str(hs)+",thank you for logging in again")
else:
    print("We need to find some users!")
current_users=["h","a","o","xiao","yu","nan"]
new_users=["A","b","c","nan"]
for new_user in new_users:
    if new_user.lower() in current_users:
        print("Adding "+str(new_user))
    else:
        print("sorry,no "+str(new_user))
print("Finish!")
numbers=list(range(1,10))
print(numbers)
for number in numbers:
    if number==1:
        print(str(number)+"st")
    elif number==2:
        print(str(number)+"nd")
    elif number==3:
        print(str(number)+"rd")
    elif number>3:
        print(str(number)+"th")
print("这是数字代码")