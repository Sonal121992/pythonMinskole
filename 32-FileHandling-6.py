# 24th April 2024
# script29.py

# ################################# File Handling #############################################

# \w [a to z, A to Z, 0 to 9] ===> small w

# Program 1
# only one occurence
# 1. search ====> It will give out the first occurence it found
# It will not search any alpha numeric character
import re
str = "man sun mop run moon"
result = re.search(r'm\w\w',str)
# print(result.group()) #man for 'm\w\w' # this we have commented for 'm-\w\w'
if result:
    print(result.group()) # man for 'm\w\w' # it will not show any ans for 'm-\w\w'

print("=========================")

# Program 2
# gives all occurence
# 2. findall ===> will find all the occurence it found out
str2 = "man sun mop map mat rap rat shape mountain goat"
list2 = re.findall(r'm\w\w',str2)
print(list2) # ['man', 'mop', 'map', 'mat', 'mou'] 
# since the mountain has 8 words then also it will give only 3 words 
# since it will return only the given amount of character as we described here 'm\w\w'

print("=========================")

# Program 3
# 3. match
str2 = "python is good programming language use in data science"
list3 = re.match(r'p\w\w',str2)
print(list3.group()) # pyt if we are matching 'p-\w\w'
if list3: # This is for negative ans # means if we have error them then we will comment print command then instead of throughing error it will not show any ans
    # AttributeError: 'NoneType' object has no attribute 'group'
    list3.group()

print("==========================")

# Program 4
# 4. split ====> here we can use the aplhanumeric character
# split is done with the help of alpha numeric character
#\W ----- non-alpha - numeric ===> for capital W
# \W matches any character that is not a word character. 
# A word character is typically defined as alphanumeric characters (letters, digits, and underscores). 
# Non-word characters include symbols, punctuation, whitespace, etc.
# + is a quantifier that matches one or more occurrences of the preceding pattern. 
# So \W+ matches one or more non-word characters in a row.
import re
str3 = "This ; is the : 'Core' python's book"
result = re.split(r'\W+',str3)
print(result) # ['This', 'is', 'the', 'Core', 'python', 's', 'book']
# with the help of \W+ we have split the sentence at all aplha numeric character

print("===========================")

# Program 5
# 5. sub ===> use to substitute a word or character whatever we want
str4 = "I am learning javasereit and python"
list4 = re.sub(r"javasereit","javascript",str4)
print(list4) # I am learning javascript and python
# incorrect spelling is replace or substitute with correct spellinng
