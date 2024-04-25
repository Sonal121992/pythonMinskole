## 21st April 2024

# ######################### File Handling ################################################

## 1. Write a Program to enter the number of city you want to enter and then enter that particular number of cities.

# reclen = 20
# with open('cities1.bin','wb') as f: # open because we opening new file and wb because we are write that file
#     n = int(input('Enter the number of cities : ')) # here we are entering the int
#     for x in range(n): # this loop will continue till n entered
#         city = input('Enter the city : ') # Pune Nagpur .....
#         city = city + (reclen - len(city)) * " " 
#         #20 -len(city) * " ", 
#         #20-4 * " " for Pune,
#         #16 * " "
#         # So the other city writing will start after 16 gap line after writing city name "Pune"
#         #12345678910111213141516192012345678910111213141516171819201
#         #Pune                       Nagpur                         Wardha
#         #With words the gap is 20
#         city = city.encode()
#         # converts the Unicode representation of the string into a sequence of bytes using a specified encoding.
#         # Encoding allows you to represent text as a sequence of bytes, which is necessary for storage or transmission over networks.
#         f.write(city) # It write the whole city in file



## 2. Write a program to find or read the city from record that is already available (Get the data with record number)

# reclen = 20
# with open('cities1.bin','rb') as f: # rb will read the file
#     n = int(input('Record number : ')) # Here we will put the number 1, 2, 3, or 4
#     # 1 indicates the record number 1
#     # 2 indicate the record number 2
#     # likewise we can find any record from the file
#     f.seek(reclen * (n-1)) # seek will be use to find the data 
#     # 20 * (4-1)
#     # 20 * 3
#     # 60  =====> will go on column/line no 60 directly to read the character
#     str = f.read(reclen) # read that reclen means line
#     str = str.decode() # decode that str to get into terminal
#     print(str) #Print that str to terminal



## 3. Write the program to get the total number of records present and also the whole size of the file

# import os
# reclen = 20
# size = os.path.getsize('cities1.bin') # This will show us size of whole file
# totalRecords = int(size/reclen) # size of whole file /gap we have provided
# print(size) #80
# print(totalRecords) #4

# ## 4. Write the program to see whether the particular city name is present in the record or not

# # we have to join above 3 number code with this to get ans as we want totalrecords
# with open('cities1.bin','rb') as f: # Here we can read the cities1.bin file
#     city = input('Enter the city : ') # Enter the city name which we want to find
#     city = city.encode() # Encode the city name into bytes which is the understanable language for system
#     position = 0 # we will start from position 0
#     found = False 
#     # It initializes the variable found to False. 
#     # This means that initially, the condition represented by found is not met, indicating that a certain condition or search result has not been found yet.
#     for x in range(totalRecords): # for is use to go into loop
#         f.seek(position) # we have to start from 0 position
#         foundcity = f.read(reclen) # read the data inside cities1.bin file which is save with the varaible reclen
#         if city in foundcity:
#             print('City Found') # If we found the city then print this msg
#             found = True # as it is found therefore the condition is true
#             break # Break the loop if the condition is true
#         position = position + reclen # If the condition is not true then add the position to get further in column to search the city
#     if not found: # If the city name is not found during whole loop then below line will get print
#         print('City Not Found')

# If we enter the city name which is "already present" in the record then then we get "City Found"
# If we enter the city name which is "not present" in the record then we get "City not Found"


# 5. Write a program to update the file with new name (replace the existing city name with new city name)

# 1. 'w' (write mode):  Opens a file for writing. If the file doesn't exist, it creates a new file. 
#                       If the file exists, it truncates (empties) the file before writing. 
#                       You can only write data to the file in this mode.

# 2.'r' (read mode): Opens a file for reading. 
#                    The file must exist; otherwise, it raises a FileNotFoundError. 
#                    You can only read data from the file in this mode.

# 3. 'wb' (write binary mode): Opens a file for writing in binary mode. 
#                              Similar to 'w', but it writes data in binary format. 
#                              Useful when working with non-text data like images or binary files.

#  4. 'rb' (read binary mode): Opens a file for reading in binary mode. 
#                              Similar to 'r', but it reads data in binary format. 
#                              Useful when reading non-text files.

#  5. 'r+b' (read/write binary mode): Opens a file for both reading and writing in binary mode. 
#                                     The file must exist, and you can read from or write to any part of the file. 
#                                     Useful when you need to both read and modify the contents of a binary file.

import os
gap = 20 # always use reclen instead of gap .....reclen means record length
size1 = os.path.getsize('cities1.bin')
totalRecods1 = int(size1/gap)

with open('cities1.bin','r+b') as f:
    replc = input('Enter the city to replace : ')
    replc = replc + (gap - len(replc)) * " "
    replc = replc.encode()

    updt = input('Enter city to replace with : ')
    updt = updt + (gap - len(updt)) * " "
    updt = updt.encode()

    position = 0
    found = False

    for x in range(totalRecods1):
        f.seek(position)
        nme = f.read(gap)
        if nme == replc:
            found = True
            f.seek(-20,1)
            f.write(updt)
            break
        position = position + gap
    if not found:
        print("City not Found")

# if we enter the city name which is present in the file then it will replace the file with new name and update it
# if we enter the city name which is not present in the record then it will give "CIty not Found"

