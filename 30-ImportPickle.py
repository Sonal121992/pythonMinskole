# 18th April 2024

import pickle
class Emp:
    def __init__(self,fn,ln,sal):
        self.firstName = fn
        self.lastName = ln
        self.salary = sal

    def displayInfo(self):
        print(self.firstName)
        print(self.lastName)
        print(self.salary)
f = open('emp.dat','wb')
users = int(input('Enter the number of users : '))

for a in range(users):
    fn = input("Enter the firstName : ")
    ln = input("Enter the lastName : ")
    sal = input("Enter the salary : ")
    e = Emp(fn, ln, sal)
    pickle.dump(e, f)
f.close()
f = open('emp.dat','rb')
while True:
    try:
        e = pickle.load(f)
        e.displayInfo()
    except EOFError:
        print("EOF file reached")
        break
f.close()