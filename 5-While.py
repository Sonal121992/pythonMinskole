# While loop
# initialization
# while(condition)
    # statement
    # increment

# program 1 
# print 1 to 3
a1 = 1
while a1<=3:
    print(a1) # 1 2 3 
    a1 = a1 + 1
print("-------")

# program 2
# print 1 to 5
a2 = 1
while a2 <= 5:
    print(a2) #  1 2 3 4 5 
    a2 = a2 + 1
print("------")

# program 3
# print table of 2
a3 = 2
while(a3<=20):
    print(a3) # 2 4 6 8 10 12 14 16 18 20
    a3 = a3 + 2
print("------")

# program 4
# print table of 5 in reverse
a4 = 50
while(a4>=5):
    print(a4) # 50 45 40 35 30 25 20 15 10 5
    a4 = a4 - 5
print("-------")

# program 5
# break statement with while loop
# print after break
a5 = 1
while a5 <=6:
    if a5 == 3:
        break
    print(a5) # 1 2
    a5 = a5 + 1
print("-------")

# program 6
# print before break
a6 = 1
while a6 <=6:
    print(a6) # 1 2 3
    if a6 == 3:
        break
    a6 = a6 + 1

# continue statment with while loop
a7 = 1
while a7 <= 6:
    if a7 == 3:
        a7 = a7 + 1
        continue 
    print(a7) # 1 2 4 5 6
    a7 = a7 + 1

print("-----------")

a8 = 1
while a8 <= 6:
    print(a8) # 1 2 3 4 5 6
    if(a8 == 3):
        a8 = a8 + 1
        continue
    a8 = a8 + 1