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

# Enter unlimited names in a file and put a character to stop entering name

f = open('myfile3.txt','w')
while str != "@":
    str = input ("Enter the name " + "\n")
    if str != "@":
        f.write(str + '\n')
f.close()

