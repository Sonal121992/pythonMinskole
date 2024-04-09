# 1st April 2024

# bank
# class level varaiable - country
# constructor - fn, ln, accNo, Transaction
# deposit(), withdrawl()
# static - total accounts
# class level name for name changes

class Bank:
    country = 'India'
    count = 0

    def __init__(self, fn, ln, acc, bal):
        self.firstName = fn
        self.lastName = ln 
        self.accNo = acc
        self.balance = bal
        self.transaction = []
        Bank.count = Bank.count + 1
    def deposit(self, amt):
        self.balance = self.balance + amt
        self.transaction.append(amt)
    def withdrawal(self, amt):
        if (self.balance > amt):
            self.balance = self.balance - amt
            self.transaction.append(amt)
        else:
            print("Insufficient Balance")
    def lastFiveTransaction(self, x):
        return self.transaction[-x::]
    @classmethod
    def changeCountry(cls,cl):
        cls.country = cl
    @staticmethod
    def objCount():
        return Bank.count
C1 = Bank('Sonal', 'Khante', 111, 10000)
C2 = Bank('Chetan', 'Khante', 222, 25000)
C3 = Bank('Novika', 'Khante', 333, 62000)
C4 = Bank('Ketan', 'Lambat', 444, 45000)
C5 = Bank('Indrayani', 'Lambat', 555, 54000)

print(Bank.objCount()) #5 since there are 5 client or can say 5 accounts
C1.withdrawal(320)
C1.deposit(852300)
C1.withdrawal(6500)
C1.deposit(12400)
C1.deposit(3250)
C1.withdrawal(7500)
C1.deposit(5600)
print(C1.lastFiveTransaction(5)) # [6500, 12400, 3250, 7500, 5600]
# If we withdraw more amt than amt present in account then we will get "Insufficient Amount" message

# abstractMethod ########################################################################
# # RBI --------save() loan()
# # SBI --------save() loan()
# # ICICI ------save() loan()

# # complete abstraction ------------- method definition
# # partial abstraction -------------- complete method abstract

# from abc import ABC, abstractmethod
# class RBI(ABC):
#     @abstractmethod
#     def loan(self, x):
#         pass
#     @abstractmethod
#     def save(self, x):
#         pass
# # we cannot create object of abstract class
# # a = RBI()
# class SBI(RBI):
#     #loan
#     def loan(self, x):
#         print("loan is "+ str(x))
#     #save
#     def save(self,x):
#         print("save is "+str(x))
#     def branchName(self):
#         print("Nagpur")
# class ICICI(SBI):
#     #loan
#     def loan(self, x):
#         print("loan is "+str(x))
#     #save
#     def save(self, x):
#         print("save is "+str(x))
#     def branchName(self):
#         print("Nagpur")
# nagpur = SBI()
# nagpur.loan(3) # loan is 3
# nagpur.loan(13) # loan is 13
# #nagpurICICI = ICICI()
    
from abc import ABC, abstractmethod
class RBI(ABC):
    @abstractmethod
    def loan(self):
        pass
    @abstractmethod
    def save(self):
        pass
    def country(self):
        print("India")
class SBI(RBI):
    def loan(self):
        print("loan from SBI")
    def save(self):
        print("save in SBI")
class ICICI(SBI):
    def loan(self):
        print("loan from ICICI")
    def save(self):
        print("save in ICICI")
sbiTwo = SBI()
sbiTwo.loan() # loan from SBI
sbiTwo.save() # save in SBI
sbiTwo.country() # India