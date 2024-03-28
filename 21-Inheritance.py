#script23.py

# program 1

# single inheritance ########################################################################
# parent - constructor , child no constructor

# student is inherited to teacher
# class Student:
#     def __init__(self, fn, ln, adharNo): # fn, ln, adharNo ====> parameter
#         self.firstName = fn # ===> property
#         self.lastName = ln
#         self.aadharNo = adharNo
#     def displayName(self):
#         print(self.firstName + " " + self.lastName)
# s1 = Student("sonal","khante","4256")
# print(s1.firstName)  # sonal =================================> # property call
# print(s1.lastName) # khante
# print(s1.aadharNo) # 4256
# s1.displayName() # sonal khante ===============> # method call

# class Teacher(Student):
#     salary = 100000
#     def displaySalary(self):
#         print(self.salary)
# s2 = Teacher("sonal","khante","4256")
# print(s2.firstName) # sonal
# print(s2.lastName) # khante
# print(s2.aadharNo) # 4256
# print(s2.salary) # 100000
# s2.displayName() # sonal khante
# s2.displaySalary() # 100000

# print("===========================")

# single level ------> 1 parent 1 child
# multi-level -------> more than two
# herarchical -------> 1 parent multiple child

# # program 2

# # single inheritance ########################################## with super property
# super class ===> parent class


# class Studnt:
#     def __init__(self, fn, ln, adhrN):
#         self.frstName = fn
#         self.lstName = ln
#         self.AdhaarNo = adhrN
#     def displayName(self):
#         print(self.frstName + " " + self.lstName)
# class Teachr(Studnt):
#     def __init__(self, fn, ln, adhrN, sal):
#         super().__init__(fn, ln, adhrN)
#         self.salry = sal
#     def displaySalary(self):
#         print(self.salry)
# s3 = Teachr("sonal", "khante", 7562, 2500000)
# print(s3.frstName) # sonal
# print(s3.lstName) # khante
# print(s3.AdhaarNo) # 7562
# print(s3.salry) # 2500000
# s3.displayName() # sonal khante
# s3.displaySalary() # 2500000

print("===============================")

# program 3

# multi-level ###################################################
# student ====> Teacher ====> Professional

class studnt:
    def __init__(self, fn, ln, adhrN):
        self.frstName = fn
        self.lstName = ln
        self.aadharNo = adhrN
    def displayName (self):
        print(self.frstName + " " + self.lstName)
class Teachr(studnt):
    def __init__(self, fn, ln, adhrN, sal):
        super().__init__(fn, ln, adhrN)
        self.salry = sal
    def displaySal (self):
        print(self.salry)
class Professn(Teachr):
    def __init__(self, fn, ln, adhrN, sal, spec):
        super().__init__(fn, ln, adhrN, sal)
        self.special = spec
    def displaySpec(self):
        print(self.special)
s5 = Professn("sonal", "khante", 5623, 2500000, "English")
print(s5.frstName) # sonal
print(s5.lstName) # khante
print(s5.salry) # 2500000
print(s5.special) # English

s5.displayName() # sonal khante
s5.displaySal() # 2500000
s5.displaySpec() # English

print("======================================")

# 24th March 2024 #################################################################
 # script24.py

# single inheritance #####################################################################
#  Grandfather
#      ||
#    Father

class Father:
    def __init__(self, fn, ln):
        self.firstName = fn
        self.lastName = ln
    def displayFatherName(self):
        print(self.firstName + " " + self.lastName)
class Son(Father): #===> here we inherit father in son
    def __init__(self, fn, ln, sn):
        super().__init__(fn, ln)
        self.sonName = sn
    def displaySonName(self):
        print(self.sonName + " " + self.lastName)
s6 = Son("Vijay", "Lambat", "Ketan")
print(s6.firstName) # Vijay
print(s6.lastName) # Lambat
print(s6.sonName) # Ketan
s6.displayFatherName() # Vijay Lambat
s6.displaySonName() # Ketan Lambat

print("=====================================")

# Father can't access child property and method
# Child is always beneficial since he is acquiring all properties

# multi-level inheritance ############################################################
# Grandfather
#      ||
#    Father
#      ||
#     Son

class Grandfather:
    def __init__(self, gn, ln):
        self.GrandName = gn
        self.lastName = ln
    def displayGFName(self):
        print(self.GrandName + " " + self.lastName)
class Father(Grandfather):
    def __init__(self, gn, ln, fn):
        super().__init__(gn, ln)
        self.FatherName = fn
    def displayFName(self):
        print(self.FatherName + " " + self.lastName)
class Son(Father):
    def __init__(self, gn, ln, fn, sn):
        super().__init__(gn, ln, fn)
        self.SonName = sn
    def displaySName(self):
        print(self.SonName + " " + self.lastName)
s6 = Son("Daulatrao", "Lambat", "Vijay", "Ketan")
print(s6.GrandName) # Daulatrao
print(s6.FatherName) # Vijay
print(s6.SonName) # Ketan
print(s6.lastName) # Lambat

s6.displayGFName() # Daulatrao Lambat
s6.displayFName() # Vijay Lambat
s6.displaySName() # Ketan Lambat

print("========================================")


# herarchial inheritance
# 1 parent ====> multi child
# //    Mother
# //     |   \
# //   Son    Daughter

# think about whatsApp 
# // starting from when whatsApp was introduce how WhatsApp was involved
# // 1. texting
# // 2. multi-media and texting
# // 3. video calling, multi-media and texting        

class Mother:
    def __init__(self, mn, ln):
        self.motherName = mn
        self.lastName = ln
    def displayMother(self):
        print(self.motherName + " " + self.lastName)
class Daughter(Mother):
    def __init__(self, mn, ln, dn):
        super().__init__(mn, ln)
        self.daughterName = dn
    def displayDaughter(self):
        print(self.daughterName + " " + self.lastName)
class Son(Mother):
    def __init__(self, mn, ln, sn):
        super().__init__(mn, ln)
        self.sonName = sn
    def displaySon(self):
        print(self.sonName + " " + self.lastName)

s7 = Daughter("Lalita", "Lambat", "Indrayani")
print(s7.motherName) # Lalita
print(s7.lastName) # Lambat
print(s7.daughterName) # Indrayani

s8 = Son("Lalita", "Lambat", "Ketan")
print(s8.motherName) # Lalita
print(s8.lastName) # Lambat
print(s8.sonName) # Ketan

s7.displayMother() # Lalita Lambat
s7.displayDaughter() # Indratyani Lambat

s8.displayMother() # Lalita Lambat
s8.displaySon() # Ketan Lambat

print("============================================")

# multiple inheritance

#   mother father
#      |    |
#       son

# single class is inherited from many class

class Mother:
    def __init__(self,mn, ln):
        print("Mother Constructor Called....")
        self.motherName = mn
        self.lastName = ln
    def displayMName(self):
        print(self.motherName + " " + self.lastName)
class Father:
    def __init__(self, fn, ln):
        print("Father constructor called....")
        self.fatherName = fn
        self.lastName = ln
    def displayFName(self):
        print(self.fatherName + " " + self.lastName)

class Son(Mother,Father):
    def __init__(self, mn, ln, sn):
        super().__init__(mn, ln)
        self.sname = sn
    def displaySName(self):
        print(self.sname + " " + self.lastName)

s9 = Son("Lalita", "Lambat", "Ketan") # Mother Constructor Called..
