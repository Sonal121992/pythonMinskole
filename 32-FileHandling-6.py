# 24th April 2024
# script29.py

# # ################################# File Handling #############################################

# # \w [a to z, A to Z, 0 to 9] ===> small w

# # Program 1

# # **************************************************************************
# # only one occurence
# # 1. search ====> It will give out the first occurence it found
# # ***************************************************************************

# # It will not search any alpha numeric character
# import re
# str = "man sun mop run moon"
# result = re.search(r'm\w\w',str)
# # print(result.group()) #man for 'm\w\w' # this we have commented for 'm-\w\w'
# if result:
#     print(result.group()) # man for 'm\w\w' # it will not show any ans for 'm-\w\w'

# print("=========================")

# # Program 2

# # ******************************************************************************
# # gives all occurence
# # 2. findall ===> will find all the occurence it found out
# # ******************************************************************************

# str2 = "man sun mop map mat rap rat shape mountain goat"
# list2 = re.findall(r'm\w\w',str2)
# print(list2) # ['man', 'mop', 'map', 'mat', 'mou'] 
# # since the mountain has 8 words then also it will give only 3 words 
# # since it will return only the given amount of character as we described here 'm\w\w'

# print("=========================")

# # Program 3

# # **************************************************************
# # 3. match ====> match the occurence
# # ====> it will match number of words we have provided to match
# # ***************************************************************

# str2 = "python is good programming language use in data science"
# list3 = re.match(r'p\w\w',str2)
# print(list3.group()) # pyt if we are matching 'p-\w\w'
# if list3: # This is for negative ans # means if we have error them then we will comment print command then instead of throughing error it will not show any ans
#     # AttributeError: 'NoneType' object has no attribute 'group'
#     list3.group()

# print("==========================")

# # Program 4

# # ****************************************************************
# # 4. split ====> here we can use the aplhanumeric character
# # split is done with the help of alpha numeric character
# # ***************************************************************

# #\W ----- non-alpha - numeric ===> for capital W
# # \W matches any character that is not a word character. 
# # A word character is typically defined as alphanumeric characters (letters, digits, and underscores). 
# # Non-word characters include symbols, punctuation, whitespace, etc.
# # + is a quantifier that matches one or more occurrences of the preceding pattern. 
# # So \W+ matches one or more non-word characters in a row.
# import re
# str3 = "This ; is the : 'Core' python's book"
# result = re.split(r'\W+',str3)
# print(result) # ['This', 'is', 'the', 'Core', 'python', 's', 'book']
# # with the help of \W+ we have split the sentence at all aplha numeric character

# print("===========================")

# # Program 5

# # ******************************************************************
# # 5. sub ===> use to substitute a word or character whatever we want
# # ******************************************************************

# str4 = "I am learning javasereit and python"
# list4 = re.sub(r"javasereit","javascript",str4)
# print(list4) # I am learning javascript and python
# # incorrect spelling is replace or substitute with correct spelling


# # \w ===> [a-z A-Z 0-9]
# # \W ===> [not[a-z A-Z 0-9]]
# # \d ===> [0-9]
# # \D ===> not[0-9]
# # \b ===> blank space
# # \A ===> match only start of string
# # \Z ===> match only at end

# Program 1

# *****************************************************
# findall ==> will find all the occurence
# ***********************************************


import re
str = 'an apple a day keeps doctor away'

# Write a code to get the word starting from letter "a"
listA = re.findall(r'a[\w]*',str)
print(listA) # ['an', 'apple', 'a', 'ay', 'away'] # dividing at "a" letter 

# Write a code to get the word starting from letter "a" and also space before "a" letter
listB = re.findall(r'\ba[\w]*',str)
print(listB) # ['an', 'apple', 'a', 'away'] # dividing the letter who have space before "a" letter


# Program 2
import re
str = 'The meeting will be conducted on 1st and 21st of this month'

# write a code to get 1st and 21st from sentence
listC = re.findall(r'\b\d[\w]*',str)
# \b for space \d for number 
# since \b and \d is written outside bracket will search for space and number
# then \w is written inside bracket will write the result which is \w therefore will write everything number and alphabet
print(listC) # ['1st', '21st']

# write a code to get only numbers from the sentence
listD = re.findall(r'\b\d[\d]*',str) # \b is for space and \d for number
# since \b and \d is written outside bracket will only search space and number 
# since other \d is written inside bracket will only write the number only in result
print(listD) # ['1', '21']


# program 3
import re
str = "one two three four five six seven 8 9 10"

# Write the code to get three and seven in result
listE = re.findall(r'\b\w{5}\b',str)
# \b for blank space \w for aplhanumeric so it will search space then alphanumeric character till 5 points further
# the word having 5 character will display
print(listE) # ['three', 'seven']

# **************************
# search()
# **************************


# Write a code to search a word with 5 charcter after space
listF = re.search(r'\b\w{5}\b',str)
# \b for space then will search word with 5 characters in it
# whatever we search first will come will come as result
# print(listF) # <re.Match object; span=(8, 13), match='three'> ===> will get this ans if we do not write group
print(listF.group()) # three

# program 4
listG = re.match(r'\b\w{5}\b',str)
print(listG) # None

# program 5
# write a code to get word with 4 and more characters
str = "one two three four five six seven 8 9 10"
listH = re.findall(r'\b\w{4,}\b',str)
# to find all the words who are after space is alphanumeric and is 4 and more in size and space after that
print(listH) # ['three', 'four', 'five', 'seven']

# Program 6
# Write a code the words with min 3 and max 4 characters
str = "one two three four five six seven aa 8 9 10"
listI = re.findall(r'\b\w{3,4}\b',str)
# This will find the values which are of size min 3 and max 4
print(listI) # ['one', 'two', 'four', 'five', 'six']

# Program 7
# Write a code to get the digit or number 1 and more than one
str = "one two three four five six seven aa 8 9 10"
listJ = re.findall(r'\b\d{1,}\b', str)
# In this we will get digit between two spaces
print(listJ) # ['8', '9', '10']

# Program 8
# Write a code to get a word which start from t but present at the end
str = "one two three four five six seven aa 8 9 10"
listK = re.findall(r't[\w]*\Z',str)
# If it find the desired at end then only it will show the result else empty output
print(listK) # []

str = "one two three four five six seven aa 8 9 10 three"
listL = re.findall(r't[\w]*\Z',str)
print(listL) # ['three']

# Program 9
# Write a code to get a word which start from t and present at the beginning
str = "one two three four five six seven aa 8 9 10 three"
listM = re.findall(r'\At[\w]*',str)
# \A is to find the word at the start of the list matching to word start from t
print(listM) # []
# since we did not find the word starting with t at the start therefore will give the empty list

str = "two one two three four five six seven aa 8 9 10 three"
listN = re.findall(r'\At[\w]*',str)
print(listN) # ['two']
# since here with \A we are searching the word at start
# this letter is starting with t then 