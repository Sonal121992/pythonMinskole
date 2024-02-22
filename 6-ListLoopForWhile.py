# Define List
#           0       1       2           3       4       5
vehicle = ["bus", "train", "airplane", "bike", "car", "cycle"]
print(vehicle) # ['bus', 'train', 'airplane', 'bike', 'car', "cycle"]

# list stores value by index
print(vehicle[0]) # bus
print(vehicle[1]) # train
print(vehicle[2]) # airplane
print(vehicle[3]) # bike
print(vehicle[4]) # car
print(vehicle[5]) # cycle

# Number of element in List
print(len(vehicle)) # 6

# Update the value of list
vehicle[5] = "jeep"
print(vehicle) # ['bus', 'train', 'airplane', 'bike', 'car', 'jeep']

print("=========")

# list with "for loop" ===> get index and elements of list
for x in range(0,len(vehicle),1):
    print(x) # 0 1 2 3 4 5
    print(vehicle[x]) # bus train airplane bike car jeep

print("==========")

# with "for loop" ====> reverse the list 
for x in range(len(vehicle)-1, -1, -1):
    # print(x) # 5 4 3 2 1 0
    print(vehicle[x]) # jeep car bike airplane train bus

print("===========")    

# with "while loop" ====> get index and element in list
flower = ["rose", "lotus", "lily", "daisy", "jasmine"]
y = 0
while y<len(flower):
    #print(y) #  0 1 2 3 4
    print(flower[y]) # rose lotus lily daisy jasmine
    y = y + 1
print("==========")

# # with " while loop" =====> reverse the list
a = len(flower)-1
while a>=0:
    print(a) # 4 3 2 1 0
    print(flower[a]) # jasmine daisy lily lotus rose
    a = a - 1
print("===========")

# # If the particular element is present in list
print("rose" in flower) # true

# & C:/Users/SONAL/AppData/Local/Programs/Python/Python312/python.exe c:/Sonal/Minskole/Python630PM/6-ListLoopForWhile.py
