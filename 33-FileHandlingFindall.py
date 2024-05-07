# 29th April 2024

# script30.py

import re

# \w ===> [a-z][A-Z][0-9]
# \b ===> blankspace

# # \w ===> [a-z A-Z 0-9]
# # \W ===> [not[a-z A-Z 0-9]]
# # \d ===> [0-9]
# # \D ===> not[0-9]
# # \b ===> blank space
# # \A ===> match only start of string
# # \Z ===> match only at end

# Program 1
# Write a code to get words starting with letter a after the space
str1 = "an apple a day keeps doctor away"
ans1 = re.findall(r'\ba[\w]*',str1)
print(ans1) # ['an', 'apple', 'a', 'away']

# Program 2
# Write a code to get whole digit like 1st, 2nd from sentence
str2 = "The meeting will be conducted on 21st and 22nd and 1st"
ans2 = re.findall(r'\d[\w]*',str2) # to get whole digit
print(ans2) # ['21st', '22nd', '1st']
ans3 = re.findall(r'\d[\d]*',str2) # to get only number
print(ans3) # ['21', '22', '1']

# Program 3
# Write a code to get the words and charcter from the sentence as asked
str3 = "one two three four five aa bb six seven 8 9 10 thousand"
ans4 = re.findall(r'\w{5}',str3) # it find all the words which have atleast 5 characters in them
print(ans4) # ['three', 'seven', 'thous']
ans5 = re.findall(r'\w{4}',str3) # here it will find all the words with atleast 4 chracters in them
print(ans5) # ['thre', 'four', 'five', 'seve', 'thou', 'sand']
ans6 = re.findall(r'\w{4,}',str3) # as we give , here it will find all words with 4 and more character
print(ans6) # ['three', 'four', 'five', 'seven', 'thousand']
ans7 = re.findall(r'\w{4,5}',str3) # here we are finding the word which have min 4 charcter and this will take upto 5 in each character
print(ans7) # ['three', 'four', 'five', 'seven', 'thous']

# Program 4
# Write a code to get digits from the list
ans8 = re.findall(r'\d{1}',str3) # here we get the single digit as ans even it will give 1 and 0 as separate from 10
print(ans8) # ['8', '9', '1', '0']
ans9 = re.findall(r'\d{1,}',str3) # here we will get whole digit as ans
print(ans9) # ['8', '9', '10'] 
ans10 = re.findall(r'\b\d{1,}\b',str3) # here we will get whole digit as ans it will look for space before and after
print(ans10) # ['8', '9', '10']

# Program 5
# Write a code staring and ending words
str4 = "one two three four five six seven eight nine ten"
ans11 = re.findall(r't[\w]*\Z',str4)
# with help of \Z it will find the words starting with letter t but present at last of string
print(ans11) # ['ten']
ans12 = re.findall(r'\At[\w]*',str4)
# with help of \A it will find the words starting with letter t but present at the start of string
print(ans12) # []
ans13 = re.findall(r'\Ao[\w]*',str4)
# with help of \A it will find the words starting with letter o but present at the start of string
print(ans13) # ['one']
ans13 = re.findall(r'\AO[\w]*',str4)
# with help of \A it will find the words starting with letter O but present at the start of string
print(ans13) # [] ===> here the characters are case sensitive

# Program 6
# Write a code to search a number, to search the multiple number just group it
str5 = "SonalLambatKhante:8668280134"
ans14 = re.search(r'\d+',str5)
print(ans14) # <re.Match object; span=(18, 28), match='8668280134'>
# therefore group
print(ans14.group()) # 8668280134

# Program 7
# Write a code
a = "apple a day keeps doctor away"
print(re.findall(r'a\w+',a)) # ['apple', 'ay', 'away'] ==> it will give only more than 1 character wala word
print(re.findall(r'a[\w]*',a)) # ['apple', 'a', 'ay', 'away'] ===> it will give any word starting with a 
