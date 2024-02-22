# script7.py

# Program 1

vehicles = ["bus", "train", "car", "bike", "jeep", "airplane"]
vehicles2 = vehicles
vehicles2[1] = "metro"
print(vehicles2)
print(vehicles)

# ['bus', 'metro', 'car', 'bike', 'jeep', 'airplane']
# ['bus', 'metro', 'car', 'bike', 'jeep', 'airplane']

# creates different address i.e. vehicles and vehicles2
# but the memory is same ===> both address point to the same memory
# Therefore any changes in the vehicles2 & vehicles ===> both will have same result

# append() ====> new element added at the end of the list
#           0           1       2       3       4           5       6       7
flowers = ["rose", "jasmine", "rose", "lily", "champa", "lotus", "lotus", "marigold"]
flowers.append("sunflower")
print(flowers)
# ['rose', 'jasmine', 'rose', 'lily', 'champa', 'lotus', 'lotus', 'marigold', 'sunflower']


# pop() ====> removes element from the end of the list
flowers.pop()
print(flowers)
# ['rose', 'jasmine', 'rose', 'lily', 'champa', 'lotus', 'lotus', 'marigold']


# pop(index) ===> removes the element of the particular index
flowers.pop(5)
print(flowers)
# ['rose', 'jasmine', 'rose', 'lily', 'champa', 'lotus', 'marigold']


# remove("ele") ====> removes the particular element we want
flowers.remove("lily")
print(flowers)
# ['rose', 'jasmine', 'rose', 'champa', 'lotus', 'marigold']


# clear() ====> empty the whole list ===> gives the blank list
print(flowers.clear())
print(flowers) # []


# count("ele") ===> it count the element in the list 
#           0        1          2       3       4       5           6       7
fruit = ["apple", "mango", "grapes", "orange", "apple", "mango", "banana", "mango"]
print(fruit.count("apple")) # 2
a1 = fruit.count("mango") # 3
print(a1)


# reverse() =====> it reverse the list
fruit.reverse()
print(fruit)
# ['mango', 'banana', 'mango', 'apple', 'orange', 'grapes', 'mango', 'apple']


# insert(index, "ele") ===> inserts the element at the given index
fruit.insert(5,"cherry")
print(fruit)
# ['mango', 'banana', 'mango', 'apple', 'orange', 'cherry', 'grapes', 'mango', 'apple']


# sort() ====> arrange the list in the acscending order
fruit.sort()
print(fruit)
# ['apple', 'apple', 'banana', 'cherry', 'grapes', 'mango', 'mango', 'mango', 'orange']


# Special Case
listA = [11, 22, 33]
# listB = listA
# listB[1] = 222
print(listA) # [11, 222, 33]
#print(listB) # [11, 222, 33]

# copy() =====> copy makes separate memory
listC = listA.copy()
listC[2] = 333
print(listA) # [11, 22, 33]
print(listC) # [11, 22, 333]

# extend() ===> extends the list
listA.extend([44, 55, 66])
print(listA) # [11, 22, 33, 44, 55, 66]

# index(ele) ===> it shows the index number of the particular element
print(listA.index(55)) # 4

# update ====> to update name in list
fruits = ["apple", "banana", "cherry", "apple", "chickoo", "kiwi"]
fruits[3]="pineapple"
print(fruits) # ['apple', 'banana', 'cherry', 'pineapple', 'chickoo', 'kiwi']

# retrieve =====> to get element by index
print(fruits[4]) # chickoo


# add
fruits.append("orange")
print(fruits) # ['apple', 'banana', 'cherry', 'pineapple', 'chickoo', 'kiwi', 'orange']\

# delete
fruits.pop()
print(fruits) # ['apple', 'banana', 'cherry', 'pineapple', 'chickoo', 'kiwi']
fruits.pop(3)
print(fruits) # ['apple', 'banana', 'cherry', 'chickoo', 'kiwi']

# remove
fruits.remove("banana")
print(fruits) # ['apple', 'cherry', 'chickoo', 'kiwi']

# in
print("papaya" in fruits) # False
print("cherry" in fruits) # True

# & C:/Users/SONAL/AppData/Local/Programs/Python/Python312/python.exe c:/Sonal/Minskole/Python630PM/7-ListMethods.py