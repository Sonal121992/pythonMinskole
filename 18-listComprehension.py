# script18.py
# 13th March 2024

# list Comprehension

# find the present age
list = [1989, 1990, 1991, 1992, 1992, 1994, 1995]
ages = []
for x in list:
    ages.append(2024-x)
print(ages) # [35, 34, 33, 32, 32, 30, 29]

# expression loop condition
age = [2024 - x for x in list]
print(age) # [35, 34, 33, 32, 32, 30, 29]

# Square of the numbers
num = [1,2,3,4,5,6,7,8,9,10]
sq = [x * x for x in num]
print(sq) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# even number from num list
even = [x for x in num if x % 2 == 0]
print(even) # [2, 4, 6, 8, 10]

# to detect odd or even in list for given num
num1 = [3, 4, 5, 7 ,2, 8, 9, 6]
detect = ["even" if x % 2 == 0 else "odd" for x in num1]
print(detect) # ['odd', 'even', 'odd', 'odd', 'even', 'even', 'odd', 'even']

# mr/mrs
name = ["sonali", "chetan", "novika"]
f = ["Mr/Mrs " + x for x in name if len(x)>5]
print(f) # ['Mr/Mrs sonali', 'Mr/Mrs chetan', 'Mr/Mrs novika']
g = ["Mrs " + x if x.endswith("i") or x.endswith("a") else "Mr " + x for x in name ]
print(g) #['Mrs sonali', 'Mr chetan', 'Mrs novika']

