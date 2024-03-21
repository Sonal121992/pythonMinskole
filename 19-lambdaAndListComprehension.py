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
print(b) # ['chetan', 'Novika', 'Indrayani']

print("===========================")

###########################################################################

# normal
transaction = []
amt = [12, 42, -15, 85, 72, -62]
for x in amt:
    if x > 0:
        print("deposit") # deposit deposit deposit deposit

# append
transaction = []
amt = [12, 42, -15, 85, 72, -62]       
for x in amt:
    if x > 0:
        transaction.append(x)
print(transaction) # [12, 42, 85, 72]

# append()
transaction = []
amt = [12, 42, -15, 85, 72, -62]  
for x in amt:
    if x > 0:
        transaction.append("deposit")
    else:
        transaction.append("withdraw")
print(transaction) # ['deposit', 'deposit', 'withdraw', 'deposit', 'deposit', 'withdraw']

# list comprehension
transaction = []
amt = [12, 42, -15, 85, 72, -62]
print(["withdraw" if x < 0 else "deposit" for x in amt]) # ['deposit', 'deposit', 'withdraw', 'deposit', 'deposit', 'withdraw']

# lambda function
transaction = []
amt = [12, 42, -15, 85, 72, -62]
print(list(filter(lambda x : x > 0, amt))) # [12, 42, 85, 72]
print(list(filter(lambda x : x < 0, amt))) # [-15, -62]

# decorator, recursive function, generators, modules

# collection
# names = ["sonal", "chetan", "novika"]
# info = {
#     "firstName": "sonal",
#     "lastName": "khante"
# }
# tupleA = (12, 42, 36)
# set = {12, 20, 56, 18, 32}
# firstName = "sonal"

# CURD operation
# methods
# loop
# element present, duplicate
