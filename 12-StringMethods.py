# script11.py

first_name = 'sonal'
print(first_name) # sonal
print(type (first_name)) # <class 'str'>

last_name = "khante"


middle_name = """

chetan

"""
print(type(middle_name)) # <class 'str'>

info = '''

We are learning Python

'''
print(info)

# Methods ###############################################

# How to get character from string

     
word = " Learning Python "

#0   1   2   3   4   5   6  7  8  9  10 11 12 13 14 15 16
#    L   e   a   r   n   i  n   g     P  y  t  h  o  n
#-17-16-15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 

# retreive
print(word[-11]) #n
print(word[6]) #n
print(word[-2]) #o
print(word[8]) # space

print("==========================")

# Program 2

#strint[startIndex,EndIndex(not included),stepSize]

a = word[5::]
print(a) # ing Python

a1 = word[-9::]
print(a1) #ng Python

a2 = word[2:13:1]
print(a2) #arning Pyth

a3 = word[7:-2:]
print(a3) # g Pyth

a4 = word[-7:-2:]
print(a4) # Pyth

a5 = word[-7:9:]
print(a5) # blank

a6 = word[0:11:2]
print(a6) #Lann y

a7 = word[-1:-4]
print(a7) # blank

print("==================")

# upper() ===> capitised all alphabets
a8 = word.upper()
print(a8) #LEARNING PYTHON

# lower() ===> small all the letters
a9 = word.lower()
print(a9) # learning python

# count('character') ===> counts the number of character in the word
a10 = word.count('n')# we have to pass the argument with the method
print(a10) # 3

# isupper() ===> want all letters in caps
a11 = word.isupper()
print(a11) # False

word2 = "SONAL"
a12 = word2.isupper()
print(a12) # True

# islower() =====> want all letters in small
a12 = word.islower()
print(a12) # False

word3 = "sonal" 
a13 =  word3.islower()
print(a13) # True
print(word3.islower()) # True

# len() ====> calaculate the length of whole character

print(len(word)) #15

# lstrip() ===> removes the space from left side
a14 = word.lstrip()
print(a14) # Learning Python
print(len(a14)) #16

# rstrip() ====> removes the space from right side
a15 = word.rstrip()
print(a15) #  Learning Python
print(len(a15)) # 16

# strip() ===> removes spaces from both side
a16 = word.strip()
print(a16) #Learning Python
print(len(a16))#15

print("=============")

# startswith()
a17 = word.startswith(" Lea")
print(a17) # True
a18 = word.startswith(" le")
print(a18) # False

print("============")

# endswith()
a19 = word.endswith("hon ")
print(a19) # True
a20 = word.endswith("hon")
print(a20) # False

# replace()
a21 = word.replace("Python", "JavaScript")
print(a21) #  Learning JavaScript
print(word) #  Learning Python

print("===============")

# isdigit()
a22 = "123".isdigit() # digit is 0-9
print(a22) # True

# isalpha()
a23 = "1233#A".isalpha()
print(a23) # False

# isalnum()
a24 = "1233#".isalnum()
print(a24) # False

a25 = "hello"
print(a25.isalnum()) # True
a26 = "1234"
print(a26.isalnum()) # True
a27 = "h123"
print(a27.isalnum()) # True
a28 = "h12#"
print(a28.isalnum()) # False

print("==================")

# isspace() ===> return true only if have white space else will return false

print(word.isspace()) # False
letter = " "
a29 = letter.isspace() # True
print(a29)
letter1 = " a"
a30 = letter1.isspace() # False
print(a30)
 
# capitalize() ===> capitalize the first word of the letter or sentence
name = "sonal"
print(name.capitalize()) # Sonal

# istitle() ===> returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.
print(word.istitle()) # True
print(name.istitle()) # False
a31 = "I am learning Python"
print(a31.istitle())

# join() ===> converts list to string, returns string by joing with special character

info = ["sonal", "khante", "8668280134"]
print(type(info)) # list
a32 = "@".join(info)
print(a32) # sonal@khante@8668280134
print("-".join(info)) # sonal-khante-8668280134

# split() ===> split at the character we define and returns a list

email = "sonalkhante21@gmail.com"
print(email.split('@')) # ['sonalkhante21', 'gmail.com']
print("===============")

# find() ====> method finds the first occurrence of the specified value. and returns -1 if the value is not found.

# method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found.

# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# L e a r n i n g   P  y  t  h  o  n

print(word.find('n', 3)) # 5
print(word.find('n',9)) # 15
print(word.find('a',10)) # -1 ====> since not character available 
print("=============")

# removeprefix()

email1 = "gmail.com@sonal"
email2 = "gmail.com@chetan"
email3 = "gmail.com@novika"

print(email1.removeprefix("gmail.com@"))

# we want like ["sonal", "chetan", "novika"]

student = [email1, email2, email3]
list = []
for x in student:
    b1 = x.removeprefix("gmail.com@")
    list.append(b1)
    print(list) #['sonal', 'chetan', 'novika']

print("==============")

students = {
    "1": "sonaladmin",
    "2": "chetanceo",
    "3": "kukucustomer",
    "4": "novikamanager"
}

role = ["admin", "ceo", "customer", "manager"]
names = []
# we want result as names = ["sonal", "chetan", "kuku", "novika"]
for x in students.values():
    for y in role:
        if y in x:
            b2 = x.removesuffix(y)
            names.append(b2)
print(names) # ['sonal', 'chetan', 'kuku', 'novika']

print("============")

# swap()

b1 = "hello"
print(b1.swapcase()) # HELLO
b2 = "SUNLIGHT"
print(b2.swapcase()) # sunlight
print("============")

# zfill()

letter2 = "Good-Morning"
letter3 = "Good-Night"
print(letter2.zfill(20)) # 00000000Good-Morning
print(letter3.zfill(15)) # 00000Good-Night
