# # 12th April 2024

# # script26.py ===> File Handling

# Program 1 ====> Write a code to read a jpg file and write to make it duplicate

# rb = open('vk.jpg','rb') # here we are reading the original file
# rb2 = open('vk2.jpg','wb') # here we are making/writing the copy of original file
# bytes = rb.read() # here we are reading the bytes from original file
# rb2.write(bytes) # here we are writing the same bytes for the duplicate file
# rb.close() # closing the work on orignal file 
# rb2.close() # closing the work on duplicate file

# # Program 2 ====> Make a code to write a info4.txt

# with open('info4.txt','w') as f: # This code will write a new txt file
#     f.write('I am learning js') # This will write text inside that text file
#     f.write('I am learning python') 

# # Program 3 ====> code to read a info4.txt file in terminal

# with open('info4.txt','r') as f2: # This is to read the text inside the txt file
#     str = f2.read() # This code will save the readed text in given variable like "str"
#     print(str) # This will print the text inside the file into the terminal
# # I am learning jsI am learning python

#################################################################################
# user defined data type
#################################################################################

import pickle # It stores the instance using pickle module
class Emp:
    def __init__(self,fn,ln,eml,ag):
        self.firstName = fn
        self.lastName = ln
        self.email = eml
        self.age = ag

    def displayDetails(self):
        print(self.firstName)
        print(self.lastName)
        print(self.email)
        print(self.age)

f = open('student.dat','wb') # this will open new file # this open file name 'student.dat' in binary write mode(wb)
# This file will be used to store the instances of the Emp class.
n = int(input('Enter the number of objects')) # here we will enter how many entries we want
for x in range(n): # this is the loop for number of entries
    fn = input("Enter firstName : ") # Enter first name here
    ln = input("Enter lastName : ") # Enter last name here
    eml = input("Enter Email : ") # Enter email here
    ag = input("Enter age : ") # Enter age here
    a = Emp(fn,ln,eml,ag) # It creates an instance a of the Emp class with the provided input data.
    pickle.dump(a,f) # It then uses pickle.dump() to serialize (convert to bytes) and store the instance a in the file opened earlier.
f.close()
# Enter the number of objects4
# Enter firstName : Sonal
# Enter lastName : Khante
# Enter Email : sonalkhante21@gmail.com
# Enter age : 31
# Enter firstName : Chetan
# Enter lastName : Khante
# Enter Email : chetankhante@gmail.com
# Enter age : 34
# Enter firstName : Novika 
# Enter lastName : Khante
# Enter Email : 3
# Enter age : novikakhante@gmail.com
# Enter firstName : Ketan
# Enter lastName : Lambat
# Enter Email : ketanlambat@gmail.com
# Enter age : 23
