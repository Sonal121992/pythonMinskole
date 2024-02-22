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


# delete
info.pop("rollNo")
print(info) # {'first': 'chetan', 'last': 'khante', 'age': 31, 'city': 'rourkela'}


# len
print(len(info)) #4

# in
print("Last" in info) # False
print("last" in info) # True

# duplicate keys
print(info)

# delete the dict
del info
print(info) # info is not defined


