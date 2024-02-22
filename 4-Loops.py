# loops are of two types
# while and for loop

# for loop without break

# for x in range(startIndex, EndIndex(not included), stepSize):
#   statement

# just range
for x in range(5):
    print(x) # 0 1 2 3 4

print("---------")

# print from 0 to 9
for x in range(10):
    print(x) # 0 1 2 3 4 5 6 7 8 9
print("==========")

# print table of 2
for x in range(2,21,2):
    print(x) # 2 4 6 8 10 12 14 16 18 20
print("=========")

for x in range(11):
    print(x*2) # 2 4 6 8 10 12 14 16 18 20
print("----------")

# print range in reverse 5 to 1
for x in range(5,0,-1):
    print(x) # 5 4 3 2 1
print("========")

# print reverse table of 2
for x in range(20, 1, -2):
    print(x) # 20 18 16 14 12 10 8 6 4 2
print("----------")

# table of 10 in reverse
for x in range(100, 9, -10):
    print(x) # 100 90 80 70 60 50 40 30 20 10
print("===========")

# break statement with for loop

# print after break statement
for x in range(1, 6):
    if x == 3:
        break
    print(x) # 1 2

print("--------")

# print before break statement
for x in range(1, 6):
    print(x) # 1 2 3 
    if x == 3:
        break

print("--------")

#  print after continue statement
for x in range(1,6):
    if x == 3:
        continue
    print(x) # 1 2 4 5

# print before continue statement
for x in range(1,6):
    print(x) # 1 2 3 4 5 
    if x==3:
        continue

