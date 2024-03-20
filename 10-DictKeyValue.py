# script9.py
# 

info = {
    "firstName" : "sonal",
    "lastName": "khante",
    "age": 31,
    "rollNo": 12
}
print(type(info)) # <class 'dict'>

for key in info.keys():
    print(key)
# firstName
# lastName
# age
# rollNo

print("===================")

for val in info.values():
    print(val)
# sonal
# khante
# 31
# 12

print("==================")

for k,v in info.items():
    print(k,v)
# firstName sonal
# lastName khante
# age 31
# rollNo 12
    
print("======================")

print(info["firstName"]) # sonal
for x in info:
    print(x, info[x])
# firstName sonal
# lastName khante
# age 31
# rollNo 12