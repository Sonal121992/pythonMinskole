# 8th Feb 2024

# one input and multiple outcomes
# numT > 0 and numT <=5 ---------- 5% discount
# numT > 5 and numT <=10 --------- 10% discount
# numT > 10 ---------------------- 20% discount

# Program 1

# if condition
#   statement

tkt = 7

if tkt > 0 and tkt <= 5:
    print("5% discount")
if tkt > 5 and tkt <= 10:
    print("10% discount")
if tkt > 10:
    print("20% discount")

# for 15 ---->  20% discount
# for 7 -----> 10% discount
 
print("-------------")

# Program 2

# if....elif...else

tkt1 = -19
if tkt1 > 0 and tkt1 <= 5:
    print("5% discount")
elif tkt1 > 5 and tkt1 <= 10:
    print("10% discount")
elif tkt1 > 10:
    print("20% discount")
else:
    print("Invalid Input") 

# for 4 ----> 5% discount
# for -18 ---> Invalid Input
    
print("---------")

# Program 3

# if with Grade

marks = 92
if marks > 90:
    print("Grade A")
if marks >= 75:
    print("Grade B")
if marks >= 60:
    print("Grade C")
# for 92 ====> Grade A , Grade B, Grade C
    
print("------------")

# Program 4
# if with Grade

marks1 = 92
if marks1 >= 90:
    print("Grade A")
if marks1 >= 75  and marks1 < 90:
    print("Grade B")
if marks1 >= 60 and marks1 < 75:
    print("Grade C")

# for 70 ======> Grade C
# for 92 ======> Grade A
    
print("------------")

# Program 5
# if....elif...else ===> for grade 

marks2 = 45
if marks2 >= 90:
    print("Grade A")
elif marks2 >=75:
    print("Grade B")
elif marks2 >= 60:
    print("Grade C")
else: 
    print("Try Again...")

# for 95 =====> Grade A
# for 75 ======> Try Again
    
# Program 6 
# comparison between 2 varaible

x = 5
y = 8
if x > y:
    print("x is greater")
else:
    print("y is greater")
# y is greater

# program 7
    
a = 45
b = 65
c = 75
if a > b and a > c:
    print("a is greater")
elif b > a and b > c:
    print("b is greater")
else:
    print("c is greater")
# c is greater
