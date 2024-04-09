# 31st March 2024, 

# why to handle exceptions???
# exceptions vs Syntax Error


# 1. Built in
# 2. User Define / Custom / Raising / Exception

a = 100
b = 200
c = 0

print(a/b) # 0.5
#print(a/c) # ZeroDivisionError: division by zero ===> this is an exception error
print("Hello World") #Hello World

# Syntax Error
#print("Hello World) 
      # SyntaxError: unterminated string literal (detected at line 17)

print("===========================")

####################################################

name = 'SONAL'
print(name) # SONAL
print(name[0]) # S
print(name[1]) # O
# print(name[6]) # IndexError: string index out of range =====> This is an exception error

print('===================================')

#######################################################

a = 100
b = 'one'
#print(a+b) # TypeError: unsupported operand type(s) for +: 'int' and 'str'  ====> 

print("========================")

########################################################
# Cases with only exception

# try:
#     code trial
# except:
#     stattement

#######################################################

# Program 1
a = 100
try:
    b = 0
    c = a/b
    print(c)
except:
    print("Some Error Occured!") # Since division with 0 is not possible therfore exception will run
print("Hello")
# Some Error Occured!
# Hello
print("----------")

# Program 2
name = 'SONAL'
try:
    print(name[7])
except:
    print("Something went wrong!!!") # since the 7th index is not present will give exception 
# Something went wrong!!!
print("-----------")

# Case: No exception
a = 100
name = 'SONAL'
try:
    b = 100
    c = a/b
    print(c) #1.0
    print(name[2]) # N
except:
    print("Error") # since no error it will not display

print("---------")

# Case: Zero div exception
a=100
name = 'SONAL'
try:
    b = 0
    c = a/b
    print(c)
    print(name[3])
except:
    print("Error") 
# Error

print("--------")

# Case: Index Exceptions
a = 100
name = 'SONAL'
try:
    b = 100
    c = a/b
    print(c)
    print(name[9])
except:
    print("Error Occured!!!")
# 1.0
# Error Occured!!!

print("==========")
# Multiple exception cases under one ttry...except block

# providing more specific Error type using basic exception class

#Program 1
a = 100
name = 'SONAL'
try:
    b = 100
    c = a/b
    print(c)
    print(name[7])
except Exception as e:
    print("Some Error occured!!!", e)
# 1.0
# Some Error occured!!! string index out of range 
# Yaha string index out of range hai....humne ye text diya nai lekin...khud hoge statement dega jo bhi error hai
print('--------------')

# program 2
a = 100
name = 'SONAL'
try:
    b = 20
    c = a/b
    print(c)
    print(name[3])
except Exception as e:
    print('Some Error Occured!!!', e)
print('Hello World!!')
# 5.0
# A
# Hello World!!
print('----------')

# program 3
a = 100
name = 'SONAL'
try:
    b = 0
    c = a/b 
    print(c)
    print(name[3])
except Exception as result: # Exception error is stored in the variable 'result'
    print("Error Occured!!!", result)
print("Hello World!")
# Error Occured!!! division by zero ------# this divison by zero is auto-generated and stored in result
# Hello World!
print('--------------')

# program 4
a = 20
name = 'SONAL'
try:
    b = 0
    c = a/b
    print(c)
    print(name[3])
except Exception as x:  # Exception error is stored in the variable 'x'
    print("Some Error Occured!!!", x)
except Exception as y:  # Exception error is stored in the variable 'y'
    print("Error Occured!!", y)
print('Hello World!!!')
# Some Error Occured!!! division by zero
# Hello World!!!
print('----------------')

# using multiple except blocks for specific errors
# for the developer team
a = 100
name = 'SONAL'
try:
    b = 0
    c = a/b
    print(c)
    print(name[0])
except ZeroDivisionError as x: # Instead of Exception here we are using actual error exception
    print("Some Error Occured!!!", x)
except IndexError as y:
    print('Error Occured', y) # Instead of Exception here we are using actual index error exception
print("Hello World!!")
# Some Error Occured!!! division by zero
# Hello World!!
print('----------')

'''
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- EncodingWarning
           +-- ResourceWarning
'''
###########################################################

# try:
#     code trial
# except:
#     statement
# else:
#     code
# finally:
#     code

###########################################################

# Program 1
a = 100
name = 'SONAL'
try:
    b = 100
    c = a/b
    print(c)
    print(name[0])
except ZeroDivisionError as x:
    print("Some Error Occured", x)
except IndexError as y:
    print("Error Occured", y)
else:
    print("Code Executed Successfully!!!")
print("Hello World!!!")
# 1.0
# S
# Code Executed Successfully!!!
# Hello World!!!
print('---------------------------')

# program 2
a = 100
name = 'SONAL'
try:
    b = 100
    c = a/b
    print(c)
    print(name[3])
except ZeroDivisionError as x:
    print("Error", x)
except IndexError as y:
    print("Error Occured!!!", y)
else:
    print("Code Executed Successfully!!!")
finally:
    print("This will always execute")
print("Hello World!!!")
# 1.0
# A
# Code Executed Successfully!!!
# This will always execute
# Hello World!!!
print('----------------')

# program 3
a = 100
name = 'SONAL'
try:
    b = 100
    c = a/b
    print(c)
    print(name[8])
except ZeroDivisionError as x:
    print("Error", x)
except IndexError as y:
    print('Error',y)
else:
    print('Code Executed Successfully!!!')
finally:
    print('This will always get executed')
print('Hello World!')
# 1.0
# Error string index out of range
# This will always get executed
# Hello World!
print('---------------------')

# CUSTOM ERROR i.e. RAISING EXCEPTIONS
# https://docs.python.org/3.10/library/exceptions.html

# INPUT IN PYTHON

# RASISING CUSTOME EXCEPTION ###################################################
##### we need even number in numerical form !!!

# Program 1
x = input("Enter a number : ")
print('-----------------')

# Program 2
x = int(input("Enter the number: "))
if x % 2 != 0:
    print("Number is not even")
else:
    print("Number is even")
# Enter the number: 2
# Number is even
print('--------------------')

# RAISING EXCEPTION ###############################################################

x = int(input("Enter the number: "))
if x % 2 != 0:
    raise Exception("Enter even number only")
else:
    print("Number entered is even")
# Enter the number: 6
# Number entered is even
print('------------------------')

# if enetered odd number
# Traceback (most recent call last):
#   File "c:\Sonal\Minskole\Python630PM\24-ExceptionHandlingRahulSir.py", line 374, in <module>
#     raise Exception("Enter even number only")
# Exception: Enter even number only

# so will change the code 

# CALCULATING AGE #############################################################

current_year = 2024
year_born = 1992
age = current_year - year_born
print(age) 
# 32
print('--------------')

# case 2 : age is negative
curr_year = 2024
yr_born = 2030
ag = curr_year - yr_born
print(ag) 
# -6
print('---------------')

# RAISING EXCEPTION ##########################################################
C_Yr = 2024
B_Yr = 2021
if B_Yr > C_Yr:
    raise Exception ("Birth year is greater than current year")
else:
    age = C_Yr - B_Yr
    print(age) # 3
print('------------')
# Traceback (most recent call last):
#   File "c:\Sonal\Minskole\Python630PM\24-ExceptionHandlingRahulSir.py", line 410, in <module>
#     raise Exception ("Birth year is greater than current year")
# Exception: Birth year is greater than current year

# C_Yr = 2024
# B_Yr = 2050
# if B_Yr > C_Yr:
#     raise Exception("Invalid birth year")
# else:
#     age = C_Yr - B_Yr
#     print(age)
# print('Acc Balance')
# print('------------------)

# Traceback (most recent call last):
#   File "c:\Sonal\Minskole\Python630PM\24-ExceptionHandlingRahulSir.py", line 422, in <module>
#     raise Exception("Invalid birth year")
# Exception: Invalid birth year

# CONVERTING THE LOGIC INTO FUNCTION #################################################

def calculate_age(year_born):
    current_year = 2024
    if year_born > current_year:
        raise Exception("Invalid year of birth")
    else:
        age = current_year - year_born
        print(age)
# calling the function
try:
    calculate_age(1992)
except:
    print("Some error occured")
print("Acc Balance")
# 32
# Acc Balance
print('-------------------------')

# for invalid ####################################

def calculate_age(born_year):
    current_year = 2024
    if (born_year > current_year):
        raise Exception("Invalid birth year")
    else:
        age = current_year - born_year
        print(age)
# calling the function
try:
    calculate_age(2050)
except:
    print("Invalid year of birth !! Please enter correct year")
print("Acc Balance")
# Invalid year of birth !! Please enter correct year
# Acc Balance
print('----------------------------')

# Program 1 ####################################################################

a = 100
name = 'SONAL'
try:
    b = 100
    c = a/b
    print(c)
    print(name[8])
except ZeroDivisionError as x:
    print('Error Occured', x)
except IndexError as y:
    print('Error Occured', y)
else:
    print("Code executed successfully")
finally:
    print("This will always get executed")
print("Hello World!!!")
# 1.0
# Error Occured string index out of range
# This will always get executed
# Hello World!!!
print('-------------------------')

a = 100
name = 'SONAL'
try:
    b = 0
    c = a/b # ZeroDivisionError
    print(c)
    print(name[10]) # IndexError
except ZeroDivisionError as x:
    print("Error Occured")
except IndexError as y:
    print("Error Occured", y)
else:
    print("Code executed successfully")
finally:
    print("I will always execute")
# Error Occured
# I will always execute