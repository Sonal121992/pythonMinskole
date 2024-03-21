# 19th March 2024
# script19.py

# normal
year = [1989, 1990, 1991, 1992]
age = []
for i in year:
    x = 2024 - i
    age.append(x)
print(age) # [35, 34, 33, 32]

# With lambda function
a = list(map(lambda x:2024-x, year))
print(a) # [35, 34, 33, 32]

# with list comprehension
print([2024 - i for i in year]) # [35, 34, 33, 32]

print("=======================")

#########################################################################

# for names above 6

# normal
names = ["sonal", "chetan", "Novika", "Indrayani", "Ketan"]
above5 = []
for x in names:
    if len(x) > 5:
        above5.append(x)
print(above5) # ['chetan', 'Novika', 'Indrayani']

# list comprehension
print([x for x in names if len(x)>5]) # ['chetan', 'Novika', 'Indrayani']

# Lambda function
b = list(filter(lambda x: len(x)>5, names))
print(b)
