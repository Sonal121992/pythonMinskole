# script14.py, script15.py

# Tuple() ===> allow duplicate values
alpha = ("A", "B", "C", "D", "B", "A")
print(type(alpha)) # <class 'tuple'>
print(alpha) # ('A', 'B', 'C', 'D')
print(len(alpha)) # 4
a1 = list(alpha) # =====> Convert Tuple to list
print(a1) # ['A', 'B', 'C', 'D']

# Set() ===> do not allow duplicate values
a = {11,22,33,44,55,33,22,11}
print(type(a)) # <class 'set'>
print(a) # {33, 22, 55, 11, 44} ===> will interchange location of element inside the set
print(len(a)) # 5 ====> eventhough there are 8 elements it will avoid duplication and will return original length

# stores the value by index??? ====> No
# print(setA[0]) # TypeError: 'set' object is not subscriptable

for x in a:
    print(x) # 33 22 55 11 44

# Methods
    
# add() ====> to add the element in the set
a.add(66)
print(a) # {33, 66, 22, 55, 11, 44}

# pop() ====> remove the item from beginning
a.pop()
print(a)  # {66, 22, 55, 11, 44}

# remove() ====> remove the given element from set
a.remove(55)
print(a) # {66, 22, 11, 44}

# union(setName) ===> mix the two sets 
B = {77,88,99} 
C = a.union(B)
print(C) #{66, 99, 22, 88, 11, 44, 77}

# intersection(setName) ===> display common element between two
D = {11,22,44,33}
E = {22,55,33,66}
F = D.intersection(E)
print(F) # {33, 22}

# symmetric_difference() ===> returned set contains a mix of items that are not present in both sets.
G = D.symmetric_difference(E)
print(G) #{66, 11, 44, 55}

# symmetric_difference_update() ===> updates the original set by removing items that are present in both sets, and inserting the other items.
D.symmetric_difference_update(E)
print(D) # {66, 11, 44, 55}
print(E)

x = {11,22,33,7}
y = {22,44,33,55,99,88}
x.symmetric_difference_update(y)
print(x) # {99, 7, 55, 88, 11, 44}

# difference() ====>  returned set contains items that exist only in the first set, and not in both sets.
z = x.difference(y)
print(z) # {11, 7}

z1 = y.difference(x)
print(z1) # {33, 22}-

# difference_update() ===> removes the items that exist in both sets.
x.difference_update(y)
print(x) # {7, 11}

y.difference_update(x)
print(y) # {33, 99, 22, 55, 88, 44}

# issubset() ===> Returns whether another set contains this set or not
z2 = x.issubset(y)
print(z2) # False
z3 = y.issubset(x)
print(z3) # False
p={7,11,29}
q={7,32,56,11,85,29}
z4=p.issubset(q)
print(z4) # True
print("==============")

# issuperset() ===> Returns whether this set contains another set or not. First set should conatins all items of second set
z5 = p.issuperset(q)
print(z5) # False
z6 = q.issuperset(p)
print(z6) # True
print("==============")

# isdisjoint() ===> Returns whether two sets have a intersection or not
z7 = p.isdisjoint(q)
print(z7) # False

z8 = q.isdisjoint(p)
print(z8) # False

a = {1, 2, 3}
b = {5, 6, 7}
z9 = a.isdisjoint(b)
print(z9) # True

# update() ===> Insert the items from one set into another set
a.update({14,10,16,17})
print(a) # {16, 1, 2, 3, 17, 10, 14}

# discard() ===> Remove the specified item
a.discard(3)
print(a) # {16, 1, 2, 17, 10, 14}

# clear() ===> 	Removes all the elements from the set
a.clear()
print(a) # set()
