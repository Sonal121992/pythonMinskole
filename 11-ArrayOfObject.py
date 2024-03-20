# script10.py

info = {
    "firstName": "sonal",
    "lastName": "khante",
    "age": 31,
    "rollNo": 12
}

print(info["firstName"]) # sonal
print(info.get("firstName")) # sonal
print(info.setdefault('city', 'rourkela'))
print(info) # rourkela
# {'firstName': 'sonal', 'lastName': 'khante', 'age': 31, 'rollNo': 12, 'city': 'rourkela'}

a = dict.fromkeys(["keyone","keytwo","keythree"])
print(a)
# {'keyone': None, 'keytwo': None, 'keythree': None}

emp = [
    {
        "firstName": "sonal",
        "lastName": "khante",
        "age": 31,
        "skills": ["html", "css", "JS"]
    },
    {
        "firstName": "chetan",
        "lastName": "khante",
        "age": 34,
        "skills": ["JS","python","cypress"]
    },
    {
        "firstName": "ketan",
        "lastName": "lambat",
        "age": 23,
        "skills": ["JS", "CS", "Django", "selenium"]
    },
    {
        "firstName": "indrayani",
        "lastName": "lambat",
        "age": 28,
        "skills": ["JS", "Java", "Playwright", "SQL"]
    }
]

print(emp[2]['firstName']) # Ketan ====> because this object in array is stores index wise

# for loop

for x in emp:
    print(x['firstName'])
# sonal
# chetan
# ketan
# indrayani

print("===================")

# program 2 ====> user with python skills

for x in emp:
    # print(x["skills"]) it will give all the skills
    if "python" in x['skills']:
        print(x["firstName"]) # chetan

# name and number of skills

for x in emp:
    print(x["firstName"] + " : " + str(len(x["skills"])))    

# sonal : 3
# chetan : 3
# ketan : 4
# indrayani : 4


# user with python skills and age > 30
    
for x in emp:
    if x["age"]>30 and "python" in x["skills"]:
        # print(x["firstName"] + ":" x["age"] + "=>" x["skills"]) # we can't use + here to concat since only str is TypeError: can only concatenate str (not "int") to str
        print(x["firstName"],x["age"],x["skills"]) # chetan 34 ['JS', 'python', 'cypress']

# average age of all the emp

total = 0
for x in emp:
    total = total + x["age"]
print(total/len(emp)) # 29.0


        

    

