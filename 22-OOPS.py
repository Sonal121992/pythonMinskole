# script25.py
# 26th March 2024, 27th March 2024

# While these concepts are all related to the broader topic of object-oriented programming and function/method handling in Python, they are not directly interrelated to each other. 
# Each concept has its distinct meaning and purpose in Python programming:

# Overloading ==>  deals with defining multiple methods with the same name but different parameters or argument types, allowing for more flexible function usage.
# Overwriting  ==> refers to redefining a method or function with the same name, replacing the previous definition.
# Overriding ==> specifically involves a subclass defining a method with the same name and parameters as its superclass, allowing for specialized behavior in the subclass while still inheriting from the superclass.
# Duck typing  ==> is a design philosophy that focuses on an object's behavior and capabilities rather than its specific type, promoting flexibility and readability in Python code.
# These concepts are related in the sense that they all pertain to methods, functions, and object-oriented programming in Python, but they are distinct concepts with separate purposes and applications.

# 1. Overloading:

class OverloadedCalculator:
    def __init__(self, value=0):
        self.value = value

    def add(self, other):
        if isinstance(other, int):
            return self.value + other
        elif isinstance(other, OverloadedCalculator):
            return self.value + other.value
        else:
            raise TypeError("Unsupported type for addition")

#  In this example, the add method can handle two types of arguments: int and OverloadedCalculator instances.

# 2. Overwriting:

class OverwritingExample:
    def example_method(self):
        print("Original method")

    def example_method(self, new_version=True):
        if new_version:
            print("New overwritten method")
# In this example, the example_method is overwritten by a new version with an additional parameter.
            
# 3. Overriding:
            
class Parent:
    def parent_method(self):
        print("Parent's method")

class Child(Parent):
    def parent_method(self):
        print("Child's method overriding parent's method")

# In this example, the Child class overrides the parent_method from the Parent class.
        
# 4. Duck Typing:

def print_name(thing):
    if hasattr(thing, "name") and callable(getattr(thing, "name")):
        print(thing.name())

class Person:
    def name(self):
        return "John"

class Car:
    def name(self):
        return "Tesla"

print_name(Person())  # Output: John
print_name(Car())  # Output: Tesla

# In this example, the print_name function uses duck typing to print the name of objects that have a name method, regardless of their actual type.

            
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

# Duck Typing #############################################

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

print("============================")

# program 3

print("hello"  + "bye") # hellobye
print(12 + 4) # 16
print([11,22,33] + [44,55,66]) # [11,22,33,44,55,66]

class Bookx:
    def __init__(self,pages):
        self.pages = pages
    def __add__(self,others):
        return self.pages + others.pages
class Booky:
    def __init__(self,pages):
        self.pages = pages
    def __add__(self,others):
        return self.pages + others.pages
ramayan = Bookx(1200)
mahabharat = Booky(450)
print(ramayan.pages + mahabharat.pages) # 1650
print(ramayan + mahabharat) # 1650
print(mahabharat + ramayan) # 1650

print("==================")

# program 4

print(4>2) # True

class Booka:
    def __init__(self,pages):
        self.pages = pages
    def __add__(self,others):
        return self.pages > others.pages
class Bookb:
    def __init__(self,pages):
        self.pages = pages
    def __add__(self,others):
        return self.pages > others.pages
ram = Booka(10)
sham = Bookb(20)

print(ram.pages > sham.pages) # False
# print(ram > sham) # TypeError
# print(sham > ram) # TypeError

print ("===============================")


# overriding#################################

class RBI:
    def loan(self):
        print("I am a loan from WorldBank")
    def save(self):
        print("I save in WorldBank")

class SBI(RBI):
    def loan(self):
        print("I am a loan from SBI")
        super().loan()
    def save(self):
        print("I save in SBI")
        super().save()
class PNB(RBI):
    def loan(self):
        print("I have loan in PNB")
        super().loan()
    def save(self):
        print("I save in PNB")
        super().save()
a = SBI()
a.loan()
a.save()

# I am a loan from SBI
# I am a loan from WorldBank
# I save in SBI
# I save in WorldBank
    
