# # 8th April 2024
# # script25.py

# # Three Modes
# # Read, Write, Append

# # Create a file and enter a name and then close it #####################################3

# # creation of object
# f = open('myfile.txt','w') # with w we are writing the file
# # taking user input
# str = input('Enter the name ')
# # writing to the file
# f.write(str)
# # closing the file
# f.close() # because of this f.close() =====> this code will not run again
# # Enter the namesonal

# # Overwriting the existing file with other name ##############################

# f = None
# try:
#     fileName = input('Enter the filename ') # here we are entering the name
#     f = open(fileName,'r') # here we are entering the filename where we want to enter name # with r we are reading the file
#     str = f.read()
#     print(str)
# except FileNotFoundError:
#     print("File not found ")
# finally:
#     if f is not None:
#         f.close()
# print('Bye')
# # Enter the name chetan
# # Enter the filename myfile.txt
# # chetan
# # Bye

# # read, write and append #######################################################

# # opening the file
# f = open("myfile2.txt", 'w') # Here we are writing the file means making a new file
# # taking input from user
# name = input('Enter the name :')
# # writing to file
# f.write(name)
# # closing
# f.close()
#  # Enter the name :Sonal

# # see the names in the file
# # give the filename
# fileName = input('Please enter the fileName :') 
# f = open(fileName,'r')
# str = f.read()
# print(str)
# f.close()
# # Please enter the fileName :myfile2.txt
# # Chetan

# f = None
# try:
#     fileName = input('Please enter the fileName :')
#     f = open(fileName, 'r')
#     str = f.read()
#     print(str)
# except FileNotFoundError:
#     print("file not found")
# finally:
#     if f is not None:
#         f.close()

# # If we delete the file####
# # Please enter the fileName :myfile2.txt
# # file not found

# # If the file is present 
# # Please enter the fileName :myfile2.txt
# # chetan ====> whatever is there in the file

# # Enter unlimited names in a file and put a character to stop entering name

# # f = open('myfile3.txt','w')
# # while str != "@":
# #     str = input ("Enter the name " + "\n")
# #     if str != "@":
# #         f.write(str + '\n')
# # f.close()

# # Open the file3.txt read it and write in that file
# # read (r) and write (w)
# # a+
# # mode 'a+' is used when opening a file in text mode for both reading and appending.

# # When you open a file in 'a+' mode:

# # If the file does not exist, it will be created.
# # If the file exists, the file pointer is placed at the end of the file, allowing you to append data to it.
# # You can read from the file using methods like read(), readline(), or readlines().
# # You can write to the file using methods like write() or writelines().

f = open('my.file3.txt','a+')
while str != '@':
    str = input("Enter the name :")
    if str != '@':
        f.write(str + '\n')
f.seek(0,0)
str2 = f.read() # ===> reading the file with print
print(str2) # Here names will enter in the existing file
f.close()

# # Import os and sys....open file by giving its name and it will give the data insode the file

import os, sys
fname = input('Enter the filename:') # Enter the filename from where you want data
if os.path.isfile(fname):
    f = open(fname, 'r')
else:
    sys.exit()
print("The file contents are: ") # Here we will get all the data from the file
str = f.read()
print(str)
f.close()

# count word character and lines

fname = input('Enter the filename: ')
if os.path.isfile(fname):
    f = open(fname, 'r')
else:
    print('file does not exist')
    sys.exit()

cc = 0
cw = 0
cl = 0

for line in f:
    cl = cl + 1
    list = line.split()
    cw = cw + len(list)
    cc = cc + len(line)
print(cl) #29
print(cw) # 29
print(cc) # 223
f.close()

