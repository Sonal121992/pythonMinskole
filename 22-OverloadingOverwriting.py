# script25.py
# 26th March 2024, 27th March 2024

# overloading ===> same class same method name, different signature

class Calculator:
    # def addition(self,x,y):
    #     print(x+y)
    # def addition(self, x, y, z):
    #     print(x + y + z)
    # def addition(self, x, y, z, a):
    #     print(x +  y + z + a)
# But this set of code is not workable
# therefore we will design code using None
    def addition (self, x = None, y = None, z = None, a = None):
        if(x!=None and y!=None and z!=None and a!=None):
            print(x+y+z+a)
        elif(x!=None and y!=None and z!=None):
            print(x+y+z)
        elif(x!=None and y!=None):
            print(x+y)
cal = Calculator()
cal.addition(4,5) # 9
cal.addition(4,5,5) # 14
cal.addition(4,5,5,3) # 17

print("=====================================")

# class Addition:
#     def add(x,y):
#         print(x+y)
#     def add(x,y,z):
#         print(x+y+z)
#     def add(x,y,z,a):
#         print(x+y+z+a)
# a = Addition() # a is object
# a.add(4,6)
# a.add(4,6,5)
# a.add(4,6,5,2)
# TypeError: Addition.add() missing 1 required positional argument: 'a'

# therefore reconstruct the above code with none and if elif

class Addition:
    def add(self, x = None, y = None, z = None, a = None):
        if x!=None and y!=None and z!=None and a!=None:
            print(x+y+z+a)
        elif x!=None and y!=None and z!=None:
            print(x+y+z)
        elif x!=None and y!=None:
            print(x+y)
a = Addition() # a is object
a.add(4,6) #10
a.add(4,6,5) #15
a.add(4,6,5,2) #17

print("===========================")

# class Dog:
#     def talk(self): # method hai
#         print("bow bow")
# class Human:
#     def talk(self):
#         print("hello hi")
# def show_talk(obj): # function hai
#     obj.talk()
# # class ke bahar hai esiliye function hai
# # else class se attached ya andar hota to method hota hai jaise talk
# a = Dog()
# b = Human() 
# # a and b obj hai
# show_talk(a) # bow bow
# show_talk(b) # hello hi

print("=============================")

class Seed:
    def fruit(self):
        print("Mango", "Chickoo", "Apple")
class Seedless:
    def fruit(self):
        print("Banana", "pineapple")
def name(obj):
    obj.fruit()
c = Seed()
d = Seedless()
name(c) # Mango Chickoo Apple
name(d) # Banana pineapple

print("=============================")

# program 3
# Overwriting
# class Dog:
#     def talk(self):
#         print("bow bow")
# class Human:
#     def talk(self):
#         print("Hello Hi")
# class Duck:
#     def sound(self):
#         print("Quack Quack")
# def show_talk(obj):
#     obj.talk()

# a = Human()
# b = Dog()
# e = Duck()

# show_talk(a)
# show_talk(b)
# show_talk(e) # AttributeError: 'Duck' object has no attribute 'talk'

class Dog:
    def talk(self):
        print("bow bow")
class Human:
    def talk(self):
        print("Hello Hi")
class Duck:
    def sound(self):
        print("Quack Quack")
def show_talk(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    else:
        obj.sound()

a = Human()
b = Dog()
e = Duck()

show_talk(a) # Hello Hi
show_talk(b) # bow bow
show_talk(e) # Quack Quack

# Program 4
class Red:
    def flower(self):
        print("Red","Hisbiscus")
class Yellow:
    def flower(self):
        print("Marigold", "Champa", "Sunflower")
class Pink:
    def waterFlower(self):
        print("Lotus")
def name(flo):
    if hasattr(flo,"flower"):
        flo.flower()
    else:
        flo.waterFlower()
x = Red()
y = Yellow()
z = Pink()

name(x) # Red Hisbiscus
name(y) # Marigold Champa Sunflower
name(z) # lotus