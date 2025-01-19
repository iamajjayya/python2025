'''
Encapsulation : hides the internal state of an object and restricts access to it 
you use private attributes to prevent external modification


syntax :

* use __ double underscore to make an attribute privtate
* provide getter and setter methods for controlled access 



'''


class BankAccount:
    def __init__(self, balance):
        self.__balance =  balance # private attribute

    def deposit(self,amount):
        if amount > 0 :
            self.__balance += amount
        else :
            print("Deposit amount must be positive")        
        
    def withdraw(self,amount):
         if amount <= self.__balance:
             self.__balance -= amount
         else:
             print("Insufficient funds")    
                
    def get_balance(self): #getter method
        return self.__balance    



    #create an account
account =  BankAccount(1000)

print(account.get_balance())

account.deposit(5000)
print(account.get_balance())
account.withdraw(2300)
print(account.get_balance())
account.withdraw(4000)
print(account.get_balance())
account.deposit(2000)
print(account.get_balance())