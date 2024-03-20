# 11th March 2024

# script16.py

# int as parameter and int as return type ######################################
def addOne(x,y):
    return x + y
a = addOne(4,5)
print(a) # 9

# float as parameter and float as return type ##################################
def addOne(x,y):
    return x + y
b = addOne(12.2, 13.5)
print(b) # 25.7

# boolean as parameter and boolean as return type ##############################
def canDrive(age, haveVehicle):
    if age > 18 and haveVehicle:
        return True
    else:
        return False
c = canDrive(19, True)
print(c) # True
d = canDrive(12, True)
print(d) # False

# string as parameter and string as return type ##############################
def greet(name):
    return ("Welcome " + name)
e = greet("Sonal!")
print(e) # Welcome Sonal!

# list as parameter and list as return type ##################################
name = ["sonal", "chetan", "novika"]
def addName(first):
    first.append("shiv")
    return name
f = addName(name)
print(f) # ['sonal', 'chetan', 'novika', 'shiv']

# dictionary as parameter and dictionary as return type #######################
info = {
    "firstName": "Sonal",
    "lastName": "Khante"
}
def addCity(info1):
    info1["city"] = "Nagpur"
    return info1
g = addCity(info)
print(g) # {'firstName': 'Sonal', 'lastName': 'Khante', 'city': 'Nagpur'}

# tuple as parameter and tuple as return type #################################
city = ("Mumbai", "Nagpur", "Rourkela")
def addValue(city1):
    city1 = list(city1)
    city1.append("Pune")
    city1 = tuple(city1)
    return city1
h = addValue(city)
print(h) #('Mumbai', 'Nagpur', 'Rourkela', 'Pune')

# set as parameter and set as return type ###################################
number = {12, 56, 42}
def addNum(num):
    number.add(75)
    return num
i = addNum(number)
print(i) # {56, 42, 75, 12}