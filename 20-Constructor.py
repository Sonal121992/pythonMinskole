# 19th March 2024, 20th March 2024

# script20.py , script21.py
# constructor

# class Person:

#     # field and properties
#     first_name = "sonal"
#     last_name = "khante"

#     # instance
#     def walk(self):
#         print("I am walking")
#     def talk(self):
#         print("I am talking")
# name = Person()
# print(name.first_name) # sonal
# print(name.last_name) # khante
# name.walk() # I am walking
# name.talk() # I am talking

# name2 = Person()
# print(name2.first_name)
# print(name2.last_name)
# name2.walk()
# name2.talk()
# name2.first_name = "chetan"
# name2.last_name = "khante"
# print(name2.first_name) # chetan
# print(name2.last_name) # khante

# Program 2
class PersonB:
    #constructor
    def __init__(self,fn,ln):
        self.first_name = fn
        self.last_name = ln
    def walk(self):
        print("I am walking")
    def talk(self):
        print("I am talking")
one = PersonB("sonal","khante")
two = PersonB("chetan", "khante")
print(one.first_name) # sonal
print(one.last_name) # khante

print(two.first_name) # chetan
print(two.last_name) # khante

two.city = "nagpur"
print(two.city) # nagpur

# Assignment
# Vehicle
# type model
# start(), stop()

class PersonC:
    def __init__(self, fn, ln):
        self.first_Name = fn
        self.last_Name = ln

    def displayName(self):
        print(self.first_Name + " " + self.last_Name)

first = PersonC("sonal", "khante")
second = PersonC("chetan", "khante")
print(first.first_Name) # sonal
print(first.last_Name) # khante
print(second.first_Name) # chetan
print(second.last_Name) # khante
first.displayName() # sonal khante
second.displayName() # chetan khante

# Program 2

class PersonD:
    country = "Bharat"
    def __init__(self, fn, ln):
        self.firstName = fn
        self.lastName = ln

    def displayName(self):
        print(self.firstName + " "+ self.lastName)

    @classmethod
    def changeCountry(cls, cnty):
        cls.country = cnty

Per1 = PersonD("sonal", "khante")
Per2 = PersonD("chetan", "khante")
Per3 = PersonD("novika", "khante")
print(Per1.firstName) # sonal
print(Per1.lastName) # khante
print(Per1.country) # Bharat
Per1.country = "India"
print(Per1.country) # India
print(Per2.country) # Bharat
print(Per3.country) # Bharat
PersonD.changeCountry("Hindustan")
print(Per1.country) # India
print(Per2.country) # Hindustan
print(Per3.country) # Hindustan

print("========================================")
# script22.py

# class instance methodof

class Person:
    
    #constructor
    def __init__(self,fn,ln): # fn and ln are parameters
        # instance varaibles
        self.firstName = fn # self.firstname is property
        self.lastName = ln

    # instance method
    def displayName(self):
        print(self.firstName + " "+self.lastName)

    # lastName Update
    def updateName(self, ln):
        self.lastName = ln

sonal = Person("sonal","khante")
print(sonal.firstName) #sonal =====> property call
print(sonal.lastName) #khante
sonal.displayName() # sonal Khante =====> method call
sonal.updateName("chetan")
#class instance, class method

print('=========================================')

# Program 2

class Home:
    country = "India"
    #constructor
    def __init__(self, fn, ln):
        self.firstName = fn
        self.lastName = ln
    # instance method
    def updateName(self, ln, fn):
        self.firstName = fn
        self.lastName = ln
    # class method
    @classmethod
    def updateCountry(cls, cnty):
        cls.country = cnty
h = Home("sonal", "khante")
print(h.firstName) # sonal
print(h.lastName) # khante
print(h.country) # India
h.country = "Bharat"
h1 = Home("chetan", "khante")
print(h1.country) # India
h1.updateCountry("Hindustan")
print(h.country) # Bharat 
print(h1.country) # Hindustan

# static method
# count number of objects

# Program 3

class Fruit:
    count = 0
    Fru = "Orange"
    def __init__(self,ff,sf):
        self.firstfru = ff
        self.secfru = sf
        Fruit.count = Fruit.count + 1
    def displayFru(self):
        print(self.firstfru + " ," + self.secfru)
    @classmethod
    def updateFruit(cls,frt):
        cls.Fru = frt
    @staticmethod
    def countObj():
        return Fruit.count
    
fru1 = Fruit("banana","mango")
fru2 = Fruit("cherry","pineapple")
a = Fruit.countObj()
print(a) # 2
