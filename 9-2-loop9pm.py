# loop

vehicle = {
    "model": "latest",
    "type": "cupe",
    "color":"white",
    "regNo": 123
}

print(vehicle['color']) # white
for item in vehicle:
    print(item, vehicle[item])
# model latest
# type cupe
# color white
# regNo 123

for x in vehicle.keys():
    print(x)
# model
# type
# color
# regNo
    
for y in vehicle.values():
    print(y)
# latest
# cupe
# white
# 123
    
for k,v in vehicle.items():
    print(k, v)
# model latest
# type cupe
# color white
# regNo 123
    
