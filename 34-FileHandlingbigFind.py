#1st May 2024

# script31.py

# Program 1

import re
str = "sonal sakshi she shreya sr supriya sonam sayali shweta sir shrejeet shrimay"
# Write a code to find the words starting with s and followed with "o" or "n" and have space before and after
a1 = re.findall(r'\bs[on][\w]*\b',str) 
print(a1) # ['sonal', 'sonam']
# Write a code to find the words starting with s and followed with "h" or "r" and have space before and after
a2 = re.findall(r'\bs[hr][\w]*\b',str)
print(a2) # ['she', 'shreya', 'sr', 'shweta', 'shrejeet', 'shrimay']

# Program 2
# dd-mm-yy

str1 = 'sonal 12-09-1992, chetan 7-12-1989, novika 10 Jan 2021, indrayani 22-07-95, ketan 29-7-00'
# Write a code to get all the dob which are number form
a3 = re.findall(r'\d{1,2}-\d{1,2}-\d{2,4}',str1) # to get the ans in the form of dd-mm-yy or dd-mm-yyyy
print(a3) # ['12-09-1992', '7-12-1989', '22-07-95', '29-7-00']
# Write a code to get the ans exactly in the form dd-mm-yyyy
a4 = re.findall(r'\d{2}-\d{2}-\d{4}',str1)
print(a4) # ['12-09-1992']

# Program 3

# Part 1
str2 = "Hello World"
a5 = re.search(r'^he',str2) # as it is case sensitive therefore it will print else statement 
# as the str contains He not he
if a5:
    print("string starts with He")
else:
    print("string does not start with He")
#string does not start with He

# Part 2
a6 = re.search(r'^He',str2) # as it is case sensitive therefore it will print if statement
# as the str contains He at the start
if a6:
    print("string starts with He")
else:
    print("string does not start with He")  
# string starts with He

# Program 4

str3 = "Hello World  .. I am from India"
a7 = re.search(r'from India$',str3) # $ sign at end will search the character at the end of the sentence
if a7:
    print("str ends with dia")
else:
    print("str does not end with dia")
# str ends with dia

# Program 5

str4 = "Hello WoRld"
a8 = re.search(r'world$',str4)
if a8:
    print("ends with world")
else:
    print("Does not ends with world")
# Does not ends with world

a9 = re.search(r'world$',str4, re.IGNORECASE)
if a9:
    print("ends with world")
else:
    print("Does not ends with world")
#ends with world -====> when we write a Ignorecase ===> means ignore case sensitive


# Program 6
str5 = "Sonal got 95 marks , Chetan got 89 marks Sejal got 60 marks"
a10 = re.findall(r'\d{1,2}',str5) # it will find all the 2 digits from the sentence
print(a10) # ['95', '89', '60']

a11 = re.findall(r'[A-Z][a-z]*',str5)
print(a11) # ['Sonal', 'Chetan', 'Sejal']
# it found all the names because as we mentioned capital first then small aplhabet
# likewise it give in the ans

# program 6
str3 = "The meeting will start at either 9am or 9pm else at evening 6pm"

# search - firstOccurence
# match - start of string 
# findall - all occurences