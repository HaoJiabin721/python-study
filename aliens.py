alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}
aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)
aliens=[]
for alien_number in range(30):
    new_alien={'color':'green','point':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[0:4]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['point']=10
        alien['speed']="medium"
for alien in aliens[:10]:
    print(alien)
    print("...")
print(str(len(aliens)))
favorite_languages={
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
    }
for x,ys in favorite_languages.items():
    if len(ys) > 1:
        print("\n"+x.title()+"'s favorite are:")
        for y in ys:
            print("\t"+str(y.title()))
    elif len(ys)==1:
        print("\n"+x.title()+"'s favorite is: ")
        for y in ys:
            print("\t" + str(y.title()))

users={
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
        },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
        },
    'hj':{
        'first':'hao',
        'last':'jiabin',
        'location':'henan',
        },
    'hq':{
        'first':'hao',
        'last':'qingqing',
        'location':'shanghai',
        },
    'xiaoyu':{
        'first':'yu',
        'last':'nanluo',
        'location':'yunnan',
        },
    }
for xs,ys in users.items():
    print("\nUsername:"+str(xs.title()))
    full_name=ys['first']+' '+ys['last']
    location=ys['location']
    print("\tFull name: "+str(full_name.title()))
    print("\t location: "+str(location.title()))
hqs={
    'first_name':'hao',
    'last_name':'qingqing',
    'age':'30',
    'city':'shanghai',
    }
hjb={
    'first_name':'hao',
    'last_name':'jiabin',
    'age':'28',
    'city':'banna',
}
haos=[hqs,hjb]
for hao in haos:
    print(hao)
pets_0=[]
for p in range(30):
    pet={'color':'yellow','age':'11','high':13}
    pets_0.append(pet)
    print(str(pets_0))
for s in pets_0[:5]:
    print(str(s))
print(len(pets_0))
favorite_places={
    'hq':['lijiang','shanghai','chongqing'],
    'hjb':['hainan','henan','chongqing'],
    'xyn':['yunnan','lincang','banna'],
}
for xs,ys in favorite_places.items():
    print(str(xs.title()))
    for place in ys:
        print(str(place.title()))
for m in favorite_places['xyn']:
    print(str(m.title()))
numbers={
    'hjb':[1,3,4,5],
    'hqq':[2,3,4,5],
    'xyn':[5,8,10,11],
}
for x in numbers.keys():
    print(str(x.title()))
for y in numbers.values():
    print(y)
for ms,ns in numbers.items():
    print(str(ms.title()))
    for n in ns:
        print(str(n))
cities={
    'china':{
        'country':'banna',
        'population':'100',
        'fact':'5'
        },
    'japan':{
        'country':'kongdao',
        'pupulation':'10',
        'fact':'sb',
        },
    'canda':{
        'country':'xini',
        'populaiton':'50',
        'fact':'cao',
        },
}
for wss,zss in cities.items():
    print(str(wss.title()))
    for ws,zs in zss.items():
       print(str(ws)+" "+str(zs))