# 22nd April 2024

# deleting a record from file

# import os
# reclen = 20
# size = os.path.getsize('cities1.bin')
# totalRecords = int(size/reclen)

# f1 = open('cities1.bin', 'rb')
# f2 = open('cities2.bin', 'wb')

# cityToBeDeleted = input('Enter the city to be deleted : ')
# cityToBeDeleted = cityToBeDeleted + (reclen - len(cityToBeDeleted)) * " "
# cityToBeDeleted = cityToBeDeleted.encode()

# for x in range(totalRecords):
#     str = f1.read(reclen)
#     if(cityToBeDeleted != str):
#         f2.write(str)
# f1.close()
# f2.close()
# os.remove('cities1.bin')
# os.rename('cities2.bin','cities1.bin')

# regular expression
# string
str = "sonal:8668280134" #["sonal","8668280134"]
info = "sonal-khante-12/09/1992"
#print(str.split(":")[1])
print(str.split(",")[2])