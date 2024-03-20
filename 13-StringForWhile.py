# script12.py

sent = "Sun-Light Rays"
print(type(sent)) # <class 'str'>

#   0   1   2   3   4  5  6  7  8  9 10 11 12 13
#   S   u   n   -   L  i  g  h  t     R  a  y  s
# -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

print(len(sent)) # 14

# For loop

for x in range(14):
    print(x) # 1 2 3 ..............11 12 13
    print(sent[x]) # S u n ......a y s

print("===================")

for x in range(len(sent)-1, -1,-1):
    print(x) # 13 12 11 ........4 3 2 1 0
    print(sent[x]) # s y a R .... u S ===> everything in reverse

print("==================")

for x in range(50,4,-5):
    print(x) # table of 50 in reverse

print("====================")

for x in range(len(sent)):
    print(sent[x]) # Sun-Light Rays

print("====================")

for char in sent:
    print(char) # Sun-Light Rays

print("Li" in sent) # True
print("li" in sent) # False

# While Loop

i1 = 0
while(i1 < len(sent)):
    # print(i1) # 0 1 2 3 .....15
    print(sent[i1]) # Sun-Light Rays
    i1 = i1 + 1

# with while loop print in reverse
    
i2 = len(sent) - 1
while(i2 >= 0):
    print(sent[i2]) # syaR thgiL-unS
    i2 = i2 - 1



