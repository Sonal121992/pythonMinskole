info = {
    "firstName" : "sonal",
    "lastName" : "khante",
    "age" : 31,
    "rollNo" : 12
}

print (type (info)) # <class 'dict'>

info2 = info
info2['age'] = 30
# Here it will info also

print(info) # {'firstName': 'sonal', 'lastName': 'khante', 'age': 30, 'rollNo': 12}
print(info2) # {'firstName': 'sonal', 'lastName': 'khante', 'age': 30, 'rollNo': 12}

# copy()
info3 = info.copy()
info3['age'] = 35
print(info) # {'firstName': 'sonal', 'lastName': 'khante', 'age': 30, 'rollNo': 12}
print(info3) # {'firstName': 'sonal', 'lastName': 'khante', 'age': 35, 'rollNo': 12}
# Here with copy the only info3 data will get change

# program 2
# clear()
#info.clear()
#print(info) # {}

# pop(key)
info.pop('age')
print(info) # {'firstName': 'sonal', 'lastName': 'khante', 'rollNo': 12}

# popitem()
info.popitem()
print(info) # {'firstName': 'sonal', 'lastName': 'khante'}

# update()
info.update({"city":"rourkela","language":"hindi"})
print(info)

# get()
q11 = info['city']
print(q11) # rourkela
a1 = info.get('language')
print(a1)

