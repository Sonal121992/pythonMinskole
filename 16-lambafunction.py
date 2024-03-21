# script17.py
# 11th March 2024

# lamba function

def addA(x,y):
    return x + y
a = addA(12,4)
print(a) # 16

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# syntax=====> lambda arguments : expression

add = lambda x, y:x+y
b = add(12,2)
print(b) # 14

add1 = lambda x,y:x+y
print(add1(4,5)) # 9 

c = lambda x: x*x
print(c(2)) # 4

# function as parameter to another function
add = lambda x, y:x+y
def addNum(fn, x, y):
    f = fn(x, y)
    return f
d = addNum(add, 12, 4)
print(d) # 16

sub = lambda x, y:x-y
def subNum(fn, x, y):
    f = fn(x, y)
    return f
e = subNum(sub, 12, 4)
print(e) # 8

# function as return type
def add():
    return lambda x, y:x+y
f = add()
print(f) # <function add.<locals>.<lambda> at 0x0000021DB1BFD300>
f1 = f(42, 12)
print(f1) # 54
