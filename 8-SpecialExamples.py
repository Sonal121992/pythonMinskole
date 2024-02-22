# Calculate age from birth year
year = [1989, 1995, 1992, 2000]
age = []
for x in year:
    #print(2024-x)#35 29 32 24
    age.append(2024-x)
print(age) # [35, 29, 32, 24]


# Filter the numbers above 50
marks = [45, 85, 65, 12, 37, 82, 91, 30]
above50 = []
below50 = []
for x in marks:
    if(x > 50):
        above50.append(x)
    else:
        below50.append(x)
print(above50) # [85, 65, 82, 91]
print(below50) # [45, 12, 37, 30]



# make a total of whole array
digit = [12, 4, 16, 8]
sum = 0
for x in digit:
    sum = sum + x
print(sum) # 40


# write str "Welcome to " before city name
city = ["pune", "nagpur", "wardha", "rourkela"]
for x in city:
    print("Welcome to "+ x)

# Welcome to pune
# Welcome to nagpur
# Welcome to wardha
# Welcome to rourkela