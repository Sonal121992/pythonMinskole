info = {
    # "key": "value"
    # property: value
    "first": "sonal",
    "last": "khante",
    "age": 31,
    "rollNo": 12
}
print(type(info)) # <class 'dict'>

# retrieve
# filename["property"]
a = info["first"]
print(a) # sonal
print(info["age"]) # 31

# update
info['first'] = "chetan"
print(info) # {'first': 'chetan', 'last': 'khante', 'age': 31, 'rollNo': 12}

# add
info['city'] = "rourkela"
print(info) # {'first': 'chetan', 'last': 'khante', 'age': 31, 'rollNo': 12, 'city': 'rourkela'}

# len
print(len(info)) #4

# in
print("Last" in info) # False
print("last" in info) # True

# duplicate keys
print(info)

# delete
info.pop("rollNo")
print(info) # {'first': 'chetan', 'last': 'khante', 'age': 31, 'city': 'rourkela'}


# delete the dict
# del info
# print(info) # info is not defined

print("===================")

# program 2 ===> script8.py

vehicle = {
    "type": "cupe",
    "color": "white",
    "company": "tata",
    "purchase": "fresh",
    "varient": "XV",
    "accesory":"music system, back camera, seat cover, foot cover"
}

print(type(vehicle)) # <class 'dict'>

# len
print(len(vehicle)) # 3

# in
print("color" in vehicle) # True
print("Type" in vehicle) # False

# copy () ====> make duplicate memory with different address
veh2 = vehicle.copy()
print(veh2)


# retrive () ===> to get value by telling key
print(vehicle["company"]) # tata
print(vehicle["type"]) # cupe


# get() 
print(vehicle.get('company')) # tata


# add
vehicle["engine"] = "new"
print(vehicle) # added property will come here # {'type': 'cupe', 'color': 'white', 'company': 'tata', 'purchase': 'fresh', 'varient': 'XV', 'accesory': 'music system, back camera, seat cover, foot cover', 'engine': 'new'}
print(veh2) # added property will not come # {'type': 'cupe', 'color': 'white', 'company': 'tata', 'purchase': 'fresh', 'varient': 'XV', 'accesory': 'music system, back camera, seat cover, foot cover'}


# pop () ===> here we have to pass key which we want to delete
vehicle.pop("engine")
print(vehicle) # {'type': 'cupe', 'color': 'white', 'company': 'tata', 'purchase': 'fresh', 'varient': 'XV', 'accesory': 'music system, back camera, seat cover, foot cover'}


# popitem() ====> it will delete the last key from the dict
vehicle.popitem()
print(vehicle) # {'type': 'cupe', 'color': 'white', 'company': 'tata', 'purchase': 'fresh', 'varient': 'XV'}


# update
vehicle["color"] = "blue" # color from white change to white
print(vehicle) # {'type': 'cupe', 'color': 'blue', 'company': 'tata', 'purchase': 'fresh', 'varient': 'XV'}


# clear() =====> it will clear all property and values from dict
vehicle.clear() # will give blank dict
print(vehicle) # {}

# delete() ===> dict
del vehicle
print(vehicle) #  name 'vehicle' is not defined
