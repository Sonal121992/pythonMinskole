# # 30th March 2024
# # script26.py, script28.py

# # Compile - Time error ##########################################################################################

# # A compile-time error is an error in a computer program 
# # that is detected by the compiler during the process of converting the human-readable source code into machine-readable code. 
# # These errors typically occur due to mistakes in the syntax or structure of the code, such as missing semicolons, incorrect variable names, or using variables without declaring them.
# # Compile-time errors prevent the program from being successfully compiled,
# # meaning it cannot be executed until these errors are fixed. 
# # They are typically identified by error messages provided by the compiler,
# # indicating the location and nature of the error in the code.

# # def addition(x,y):
# # print(x + y) # IndentationError: expected an indented block after function definition on line 13
# # addition(12,5)
# # # 9
# # print('----------------')

# # def add():
# # print(2 + 4) # IndentationError: expected an indented block after function definition on line 19

# # Run Time Error #####################################################################################################

# # A runtime error occurs when a program is running and encounters a problem that prevents it from continuing as expected. 
# # These errors happen during the execution of t2
# he program, rather than during the compilation process. 
# # Common examples include attempting to divide by zero, accessing memory that doesn't exist, or trying to use a variable before it has been initialized.
# # Runtime errors often cause the program to crash or produce unexpected behavior.
# # Unlike compile-time errors, which are caught by the compiler, runtime errors are typically identified during program execution.

# print('Hello') # Hello 
# x = int(input("Enter the number one: ")) # 2
# y = int(input("Enter the number two: ")) # 8
# print(x/y) # 0.25
# print("Bye") # Bye

# we will get below error if we enter input as 2 and 0
# Traceback (most recent call last):
#   File "c:\Sonal\Minskole\Python630PM\26-Error.py", line 34, in <module>
#     print(x/y) # 0.25
#           ~^~
# ZeroDivisionError: division by zero

# # print("----------------")

# # print("Hello")
# # numbers = [11,75,84,23,61]
# # print(numbers[6]) # IndexError: list index out of range
# # print('Bye')

# # Logical Error ##############################################################################################

# # A logical error occurs when the code doesn't behave as intended by the programmer. 
# # Unlike syntax errors (which the compiler catches) or runtime errors (which happen during program execution), logical errors lead to incorrect output or undesired behavior while the program is running. 
# # These errors are often caused by flawed algorithms, incorrect assumptions, or mistakes in the program's logic. 
# # Debugging logical errors involves carefully analyzing the code and using techniques like print statements or debugging tools to identify and fix discrepancies between the intended and actual behavior of the program.

# def add10Pr(amount):
#     return amount*0.10
# e = add10Pr(100)
# print(e) #10.0

# print('-------------------')

# print("Hello")
# try:
#     x = int(input("Enter the number 1: "))
#     y = int(input("Enter the number 2: "))
#     print(x/y)
# except Exception:
#     print("Invalid output")

# print("---------------------")

# def calculateBonusPlusSalary(salary):
#     return 0.10 * salary
# print(calculateBonusPlusSalary(1000))
# print("hello")
# try:
#     x = int(input("Enter the value 1: "))
#     y = int(input("Enter the value 2: "))
#     print(x/y)
# except Exception:
#     print("Invalid Input")
# print("Bye")

# if we enter 1 and 0 then we will exception as input

# print('---------------------')

# def calBonusSal(amt):
#     return amt * 0.10
# print(calBonusSal(1000)) # 100

# print('----------------------')

# # Program 1

# print('Hello')
# try:
#     a = int(input('Enter 1st Number: '))
#     b = int(input('Enter 2nd Number: '))
#     print(a/b)
# except Exception:
#     print('Please enter the correct input')
# print('Bye')
# # Here if we put other than number then output will be exception else it will execute properly

# # Program 2
# # try except else finally
# print('Hello')
# names = ['sonal', 'chetan', 'novika', 'indrayani', 'ketan']
# try:
#     a = int(input('Enter 1st Number: '))
#     b = int(input('Enter 2nd Number: '))
#     print(a/b)
#     print(names[7])
# except ArithmeticError as x:
#     print('Enter correct number', x)
# except IndexError as y:
#     print('Add more element to list', y)
# except Exception as z:
#     print('Please correct the values', z)
# print('Bye')
# # Hello
# # if we add 4 and alphabet then ans will be "Please correct the values"
# # if we add 8 and 4 i.e. proper number then ans will be actual ans
# # if we add 4 and 0 then ans will be "Enter Correct number"
# # Since we have written name[7]....if all the code executed properly the this IndexError will execute

# # a = 3 and b = 0
# # Hello
# # Enter 1st Number: 3
# # Enter 2nd Number: 0
# # Enter correct number division by zero
# # Bye

# # a = 4 and b = 2
# # Hello
# # Enter 1st Number: 4
# # Enter 2nd Number: 2
# # 2.0
# # Add more element to list list index out of range
# # Bye

# # a = 4 and b = h
# # Hello
# # Enter 1st Number: 4
# # Enter 2nd Number: h
# # Please correct the values invalid literal for int() with base 10: 'h'
# # Bye

# print("----------------------------------------")

# # Program 2

# try:
#     names = ["sonal", "chetan", "novika"]
#     x = int(input("Enter the value 1: "))
#     y = int(input("Enter the value 2: "))
#     print(x/y)
#     print(names[2])
#     print(m)
# except ArithmeticError as b:
#     print("Invalid Input, ", b)
# except IndexError as c:
#     print("Increase the list, ", c)
# except NameError as d:
#     print("Not Defined, ", d)
# except Exception as e:
#     print("Something went wrong, ", e)
# print("Bye")

# value x = 4 and y = 2 ############
# Enter the value 1: 4
# Enter the value 2: 2
# 2.0
# novika
# Not Defined,  name 'm' is not defined
# Bye
# Hello

# value x = 4 and y = 0 #################
# Enter the value 1: 4
# Enter the value 2: 0
# Invalid Input,  division by zero
# Bye
# Hello

# values x = 0 and y = 4 ################
# Enter the value 1: 0
# Enter the value 2: 4
# 0.0
# novika
# Not Defined,  name 'm' is not defined
# Bye
# Hello

# values x = 4 and y = 2 ------change names[2]---- names[3]
# Enter the value 1: 4
# Enter the value 2: 2
# 2.0
# Increase the list,  list index out of range
# Bye
# Hello

# print("-------------------------")

# # program 3

# try:
#     fruits = ["mango", "chickoo", "apple", "grapes"]
#     x = int(input("Enter the fruit 1 "))
#     y = int(input("ENter the fruit 2 "))
#     print(x/y)
# except ArithmeticError as arith:
#     print("Invalid Input, ", arith)
# finally:
#     print("I will always execute")


# # Enter the fruit 1 : Litchi
# # I will always execute
# # Traceback (most recent call last):
# #   File "c:\Sonal\Minskole\Python630PM\26-Error.py", line 214, in <module>
# #     x = int(input("Enter the fruit 1 "))
# #         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# # ValueError: invalid literal for int() with base 10: 'lictchi'

# # Enter 6 and 2
# # Enter the fruit 1 6
# # ENter the fruit 2 2
# # 3.0
# # I will always execute
# # Hello

# # Enter 6 and 0
# # Enter the fruit 1 6
# # ENter the fruit 2 0
# # Invalid Input,  division by zero
# # I will always execute
# # Hello

# print("-------------------------------")

# # program 6

# try:
#     x = int(input("Enter the value 1 "))
#     y = int(input("Enter the value 2 "))
#     print(x/y)
# except ArithmeticError as a:
#     print("Invalid number, ", a)
# else:
#     print("Hello")

# # Enter the number 4 and 2
# # Enter the value 1 4
# # Enter the value 2 2
# # 2.0
# # Hello

# # Enter the number 4 and 0
# # Enter the value 1 4
# # Enter the value 2 0
# # Invalid number,  division by zero
# # Hello

# # Enter the number 6 and f
# # Enter the value 1 6
# # Enter the value 2 f
# # Traceback (most recent call last):
# #   File "c:\Sonal\Minskole\Python630PM\26-Error.py", line 251, in <module>
# #     y = int(input("Enter the value 2 "))
# #         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# # ValueError: invalid literal for int() with base 10: 'f'

# print("----------------------------")

# # program 7

# print("Hello")
# try:
#     x = int(input("Enter the 1st number "))
#     y = int(input("Enter the 2nd number "))
#     print(x/y)
# except ArithmeticError as a:
#     print("Give Proper Number, ", a)
# else:
#     print("Hello")
# finally:
#     print("I will always........")
# print("Bye")

# # Enter 4 and 2
# # Hello
# # Enter the 1st number 4
# # Enter the 2nd number 2
# # 2.0
# # Hello
# # I will always........
# # Bye
# # Hello

# # Enter 6 and 0
# # Hello
# # Enter the 1st number 6
# # Enter the 2nd number 0
# # Give Proper Number,  division by zero
# # I will always........
# # Bye
# # Hello

# # Enter 4 and h
# # Enter the 1st number 4
# # Enter the 2nd number h
# # I will always........
# # Traceback (most recent call last):
# #   File "c:\Sonal\Minskole\Python630PM\26-Error.py", line 286, in <module>
# #     y = int(input("Enter the 2nd number "))
# #         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# # ValueError: invalid literal for int() with base 10: 'h'

# A single try block can be followed by several except block ====> True
# Multiple except blocks can be used to handle multiple exceptions ====> True
# We cannot write except block with try block =====> False
# Else block and finally block are not compulsory ====> True
# When there is no exception raised else block is exceuted after try block ===> True
# Finally block is always executed ===> True


# # Program 3
# print("Hello")
# try:
#     a = int(input("Enter number 1: "))
#     b = int(input("Enter number 2: "))
#     print(a/b)
# except ArithmeticError as x:
#     print("Enter proper number, ", x)
# finally:
#     print('I will always execute')
# print('Bye')

# # input a = 4 and b = 2
# # Hello
# # Enter number 1: 4
# # Enter number 2: 2
# # 2.0
# # I will always execute
# # Bye

# # input a = 8 and  b = 0
# # Hello
# # Enter number 1: 8
# # Enter number 2: 0
# # Enter proper number,  division by zero
# # I will always execute
# # Bye

# # input a = 8 and b = t
# # Hello
# # Enter number 1: 8
# # Enter number 2: t
# # I will always execute
# # Traceback (most recent call last):
# #   File "c:\Sonal\Minskole\Python630PM\25-Error.py", line 130, in <module>
# #     b = int(input("Enter number 2: "))
# #         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# # ValueError: invalid literal for int() with base 10: 't'

# Logical Errors ###############################################################

# to return total and avg #############################

def avg(list):
    total = 0
    for x in list:
        total = total + x
        avg = total/len(list)
        return total , avg
try:
    tot, av = avg([4,5,6,2,8])
    print(tot)
    print(av)
except TypeError as a:
    print('Type Error ,', a)
except ZeroDivisionError as b:
    print("zero division, cannot pass empty list, ", b)
except Exception as c:
    print('Error, ', c)

# if list  avg([4,5,6,2,8,'t'])
# 4
# 0.6666666666666666

# if list avg([])
# Type Error , cannot unpack non-iterable NoneType object ======> TypeError

# if list avg([4,5,6,2,8])
# 4
# 0.8   

# if list avg([0,0,0,0,0])
# 0
# 0.0

print('-----------------------------')

# Division 

try:
    x = int(input("Enter the number: "))
    y = 1/x
except ValueError as d:
    print("Enter number only", d)
finally:
    print("We are not catching the exceptions....")
print("The inverse is ", y)

# Enter the number: 50
# We are not catching the exceptions....
# The inverse is  0.02

# Enter the number: f
# We are not catching the exceptions....
# Traceback (most recent call last):
#   File "c:\Sonal\Minskole\Python630PM\26-Error.py", line 411, in <module>
#     x = int(input("Enter the number: "))
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'f'

# After adding Value Error except
# Enter the number: f
# Enter number only invalid literal for int() with base 10: 'f'
# We are not catching the exceptions....
# Traceback (most recent call last):
#   File "c:\Sonal\Minskole\Python630PM\26-Error.py", line 417, in <module>
#     print("The inverse is ", y)
#                              ^
# NameError: name 'y' is not defined


print('------------------------------')

# handling assertion
try:
    x = int(input("Enter the number between 5 and 10 : "))
    assert x >= 5 and x <= 10
    print("The number enter is ", x)
except AssertionError as h:
    print("The condition is not fulfilled", h)

# Proper Number #######
# Enter the number between 5 and 10 : 8
# The number enter is  8

# Number less than 5 ########
# Enter the number between 5 and 10 : 3
# The condition is not fulfilled

# Number greater than 10 #######
# Enter the number between 5 and 10 : 15
# The condition is not fulfilled

print("---------------------------")

# Banking with exception
class lowBalance(Exception):
    def __init__(self, msg):
        self.msg = msg
def check(dict):
    for k, v in dict.items():
        if(v < 2000):
            raise lowBalance("The value is below 20K, please add amount")
try:
    bank = {"raj":1000, "sonal":50500, "chetan":450000, "novika":321500}
    check(bank)
    print("All above 20 thousand")
except lowBalance as lowbal:
    print(lowbal)

# if the all bank balance is above 20K ....bank = {"raj":1000000, "sonal":50500, "chetan":450000, "novika":321500}
# All above 20 thousand

# if any one of the balance is lower than 20K....
# The value is below 20K, please add amount



# # program 4
# print('Hello')
# try:
#     a = int(input("Enter the 1st number: "))
#     b = int(input("Enter the 2nd number: "))
#     print(a/b)
# except ArithmeticError as x:
#     print("Enter Correct number, ", x)
# else:
#     print("I run correctly")
# finally:
#     print("I will always execute")
# print("Bye")

# # input a=4 and b=2
# # Hello
# # Enter the 1st number: 4
# # Enter the 2nd number: 2
# # 2.0
# # I run correctly
# # I will always execute
# # Bye

# # input a=4 and b=0
# # Hello
# # Enter the 1st number: 4
# # Enter the 2nd number: 0
# # Enter Correct number,  division by zero
# # I will always execute
# # Bye

# # input a=4 and b=u
# # Hello
# # Enter the 1st number: 4
# # Enter the 2nd number: u
# # I will always execute
# # Traceback (most recent call last):
# #   File "c:\Sonal\Minskole\Python630PM\25-Error.py", line 169, in <module>
# #     b = int(input("Enter the 2nd number: "))
# #         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# # ValueError: invalid literal for int() with base 10: 'u'

print("-----------------------------------")

# Program 1

try:
    fruit = ["apple", "mango", "pineapple", "chickoo"]
    a = int(input("Enter 1st number :"))
    b = int(input("Enter 2nd number :"))
    print(a/b)
    print(fruit[5])
except ArithmeticError as arith:
    print("Please enter correct number ", arith)
except IndexError as ind:
    print("Add more values to a list")

# entered number 4 and 2 , and fruit[3]
# Enter 1st number :4
# Enter 2nd number :2
# 2.0
# chickoo

# Entered number 4 and 2 , and fruit[6]
# Enter 1st number :4
# Enter 2nd number :2
# 2.0
# Add more values to a list # -----> here we have called index error

# Entered number 4 and 0, and fruit[2]
# Enter 1st number :4
# Enter 2nd number :0
# Please enter correct number  division by zero # ----------> Here we have called Arithmetic Error

# print('---------------------------------')

# Program 2

# print("Hello")
# try:
#     print(34/0)
# finally:
#     print("I will always execute")
# print("Bye")

# # Hello
# # I will always execute
# # Traceback (most recent call last):
# #   File "c:\Sonal\Minskole\Python630PM\26-Error.py", line 569, in <module>
# #     print(34/0)
# #           ~~^~
# # ZeroDivisionError: division by zero

print('-----------------------------------')

# Program 3

def calAvg(list):
    [11,22,33][44]
    total = 0
    for item in list:
        total = total + item
    avg = total/len(list)
    return total, avg
try:
    a, b = calAvg([1,2,3,4,'a'])
    print(a)
    print(b)
except TypeError as i:
    print("Enter the correct input ", i)
except ZeroDivisionError as j:
    print('Arithmetic Exception, enter correct value ', j)
except Exception as k:
    print("Please enter correct input ", k)

# since we have taken [11,22,33][44] and  a, b = calAvg([1,2,3,4,5])
# Please enter correct input  list index out of range

# Now we have taken [11,22,33,44] and  a, b = calAvg([1,2,3,4,5])
# 15 =====> total
# 3.0 ====> avg

# Now we have taken [11,22,33,44] and  a, b = calAvg([1,2,3,4,'a'])
# Enter the correct input  unsupported operand type(s) for +: 'int' and 'str'

print('------------------------------------')

print('Hello')
try:
    x = 5
    assert x > 1 and x <= 9
    print(x)
except AssertionError as a:
    print("Condition not matched", a)
print("Bye")

# Since x = 18
# Hello
# Condition not matched
# Bye

# Since x = 7
# Hello
# 7
# Bye


# A single try block can be followed by several except block ====> True
# Multiple except blocks can be used to handle multiple exceptions ====> True
# We cannot write except block with try block =====> False
# We cannot write try block with except block =====> False
# Else block and finally block are not compulsory ====> True
# When there is no exception raised else block is exceuted after try block ===> True
# Finally block is always executed ===> True