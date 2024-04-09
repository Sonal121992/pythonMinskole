# script25.py
# 26th March 2024, 27th March 2024

# While these concepts are all related to the broader topic of object-oriented programming and function/method handling in Python, 
# they are not directly interrelated to each other. 
# Each concept has its distinct meaning and purpose in Python programming:

# Overloading 
# ==>  deals with defining multiple methods with the same name but different parameters or argument types, 
# allowing for more flexible function usage.

# Overwriting  
# ==> refers to redefining a method or function with the same name, replacing the previous definition.

# Overriding 
# ==> specifically involves a subclass defining a method with the same name and parameters as its superclass, 
# allowing for specialized behavior in the subclass while still inheriting from the superclass.

# Duck typing  
# ==> is a design philosophy that focuses on an object's behavior and capabilities rather than its specific type, 
# promoting flexibility and readability in Python code.

# These concepts are related in the sense that they all pertain to methods, functions, and object-oriented programming in Python, 
# but they are distinct concepts with separate purposes and applications.

###################################################################################################################################

#=================================================
                # Overloading 
#=================================================
# ==>  deals with defining multiple methods with the same name but different parameters or argument types, 
# allowing for more flexible function usage.

class OverloadedCalculator:
    def __init__(self, value = 0):
        self.value = value
    def add(self, other):
        if isinstance(other, int):
            return self.value + other
        elif isinstance(other, OverloadedCalculator):
            return self.value + other.value
        else:
            raise TypeError("Unsupported type for addition")
a = OverloadedCalculator()
a.add(0)
a.add(5)

print("------")

class Calculator:
    # def addition(self,x,y):
    #     print(x+y)
    # def addition(self, x, y, z):
    #     print(x + y + z)
    # def addition(self, x, y, z, a):
    #     print(x +  y + z + a)
# But this set of code is not workable
# therefore we will design code using None
    def addition(self, x = None, y = None, z = None, a = None):
        if(x!=None and y!=None and z!=None and a!=None):
            print(x+y+z+a)
        elif(x!=None and y!=None and z!=None):
            print(x+y+z)
        elif(x!=None and y!=None):
            print(x+y)
a = Calculator()
a.addition(4,6,7,3)
a.addition(4,6,7)
a.addition(4,6)

print("===================")

#===============================================
                    # Overwriting 
#================================================ 
# ==> refers to redefining a method or function with the same name, replacing the previous definition.

class OverwritingExample:
    def example_method(self):
        print("Original method")

    def example_method(self, new_version=True):
        if new_version:
            print("New overwritten method")
# In this example, the example_method is overwritten by a new version with an additional parameter.

print('----------')

# Write a program so that after overwriting will receive actual result like add, sub, multipl
class BookX:
    def __init__(self, pages):
        self.pages = pages
    def __add__(self, others):
        return self.pages + others.pages
class BookY:
    def __init__(self,pages):
        self.pages = pages
    def __add__(self, others):
        return self.pages + others.pages
ramayan = BookX(4500)
mahabharat = BookY(7400)
print(ramayan.pages + mahabharat.pages) # 11900
print(ramayan + mahabharat) # 11900
print(mahabharat + ramayan) # 11900

print("------------")
# Write a program to get ans as "True" and "False"

class Ram:
    def __init__(self, pages):
        self.pages = pages
    def __gt__(self,others):
        return self.pages > others.pages
class Maha:
    def __init__(self,pages):
        self.pages = pages
    def __it__(self,others):
        return self.pages > others.pages
Ramay = Ram(650)
Mahabha = Maha(450)
print(Ramay.pages > Mahabha.pages) # True
print(Ramay > Mahabha) # True
#print(Ramay < Mahabha) # Not supported for the instance

# print("===================")

#================================================
                # Overriding 
#================================================
# ==> specifically involves a subclass defining a method with the same name and parameters as its superclass, 
# allowing for specialized behavior in the subclass while still inheriting from the superclass.

class Parent:
    def parent_method(self):
        print("Parent's method")

class Child(Parent):
    def parent_method(self):
        print("Child's method overriding parent's method")
        super().parent_method()

b = Child()
b.parent_method()
# Child's method overriding parent's method
# Parent's method

# In this example, the Child class overrides the parent_method from the Parent class.

print('-----------')

class RBI:
    def loan(self): #===> method
        print("I have loan from RBI")
    def save(self):
        print("I save in RBI")
class SBI(RBI):
    def loan(self):
        print("I have loan from SBI")
        super().loan()
    def save(self):
        print("I save in SBI")
        super().save()
class BOB(RBI):
    def loan(self):
        print("I have loan from BOB")
        super().loan()
    def save(self):
        print("I save in BOB")
        super().save()
call = SBI()
call.loan()
call.save()
# I have loan from SBI
# I have loan from RBI
# I save in SBI
# I save in RBI 
   
print("-----------")

class Food:
    def streetFood(self):
        print("I love street food")
class NorthFood(Food):
    def streetFood(self):
        print("Samosa, Kulcha, Maggi, Momos")
        super().streetFood()
class SouthFood(Food):
    def streetFood(self):
        print("Dosa, Sambhar Vada, Idli, Uttapam")
        super().streetFood()
c = SouthFood()
c.streetFood()
# Dosa, Sambhar Vada, Idli, Uttapam
# I love street food

print("============")

#======================================================
                    # Duck typing #
#====================================================
# ==> is a design philosophy that focuses on an object's behavior and capabilities rather than its specific type, 
# promoting flexibility and readability in Python code.

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

print("-----------------")

class Dog:
    def sound(self):
        print("Bow Bow")
class Duck:
    def sound(self):
        print("Quack Quack")
class Human:
    def talk(self): # ===> ye method hai
        print("Hello hi")
def call_sound(obj): # ===> this function bcoz out from class
# class ke bahar hai esiliye function hai
# else class ke andar hota to method hai
    if hasattr(obj, 'sound'):
        obj.sound()
    else:
        obj.talk()
d = Dog()
e = Duck()
f = Human()
call_sound(d)
call_sound(e)
call_sound(f)

print("-------------")

class Red:
    def flower(self):
        print("Rose", "Showflower", "Tulip")
class Yellow:
    def flower(self):
        print("Champa","Sunflower","Marigold")
class WaterFlower:
    def pink(self):
        print("Lotus")
def call_flow(a):
    if hasattr(a,"flower"):
        a.flower()
    else:
        a.pink()
g = Red()
call_flow(g) # Rose Showflower Tulip

h = Yellow()
call_flow(h) # Champa Sunflower Marigold

i = WaterFlower()
call_flow(i) # Lotus