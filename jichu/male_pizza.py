def make_pizza(x,y,**toppings):
    profile={}
    profile['first']=x
    profile['last']=y
    for key , value in toppings.items():
        profile[key]=value
    return profile