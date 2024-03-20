#          0        1         2        3      4
info = ["chinmay","sarika","poorva","mahesh","rajat"]#(type(info))


#          0          1       2   3
info = ["chinmay","deshpande",12,34]

info2 = {
    "firstName":'chinmay',
    "lastName":"deshpande",
    "age":23,
    "rollNo":34
}

#           0       1     2       3
info = ["chinmay","raj","samer","rajesh"]
# retrive 
print(info[0])

# update
info[0] = "tanmay"
print(info)

#add
info.append('samay')
print(info)

# delete
info.pop()


info2 = {
    # key      : value
    # property :value
    "firstName":"chinmay",
    "lastName":"deshpande",
    "rollNo":34,
    "age":12
}

#print(info2[0])
# retrive 
e = info2['firstName']
print(e)
e2 = info2['lastName']
print(e2)
# update 
info2['rollNo'] = 99
print(info2)
# add
e3 = info2['city'] = "nagpur"
print(info2)
#remove
info2.pop('firstName')
print(info2)
print(type(dict))


vehicle = {
    "color":"red",
    "type":"sedane",
}
print(vehicle)
print(vehicle['color'])
vehicle['color'] = "blue"
vehicle['regNo'] = 123
vehicle.pop('color')
print(vehicle)
