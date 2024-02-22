# 6th Feb 2024
x = 10
print(x) # 10
x = 100
print(x) # 100 ====> x is updated

# Arithmetic Operation
# Addition  ==========> +
# Subtraction ========> -
# Multiplication =====> *
# Divison ============> /
# Modulus(Remainder)==> %

# Program 1
a = 10
b = 15
print(a + b) # 25
print(a - b) # -5
print(a * b) # 150
print(a / b) # 0.6666
print(a % b) # 10

def Calculator(x, y):
    print(x + y) 
    print(x - y)
    print(x * y)
    print(x / y)
    print(x % y)
Calculator(4,5)
Calculator(78,56)

print("-----------")

# to avoid this repeatation we will do by function

# Program 2

# Function without parameter and without return type
def SumA():
    print(8+9)
SumA() # 17
SumA() # 17
SumA() # 17

print("-----------")

# Function with Parametr and without return return type
def SumB(x,y):
    print(x+y)
SumB(4,6) # 10
SumB(7,8) # 15
SumB(45,42) # 87

print("-----------")

# Function with Parameter and with return type
def SumC(x,y):
    return x + y
a = SumC(7,5)
print(a) # 12
print(a * a) # 144


