class Account:

    def __init__(self,filepath):
        self.filepath=filepath
        with open (filepath,"r") as file:
            self.balance=int(file.read())

    def withdraw(self,amount):
        self.balance=self.balance-amount
    
    def deposit(self,amount):
        self.balance=self.balance+amount

    def commit(self):
        with open (self.filepath,"w") as file:
            file.write(str(self.balance))



class Checking(Account):

    type="checking"

    def __init__(self,filepath,fee):
        Account.__init__(self,filepath)
        self.fee= fee

    def transfer(self,amount):
        self.balance=self.balance - amount -self.fee

jack_checking=Checking("balanceJack.txt",3)
print(jack_checking.balance  )
jack_checking.deposit(200)
print(jack_checking.balance  )
jack_checking.commit()
jack_checking.transfer(100)
print(jack_checking.balance  )
jack_checking.commit()
print(jack_checking.type)

john_checking=Checking("balanceJohn.txt",3)
print(john_checking.balance  )
john_checking.deposit(200)
print(john_checking.balance  )
john_checking.commit()
john_checking.transfer(100)
print(john_checking.balance  )
john_checking.commit()
print(john_checking.type)




#account=Account("balance.txt")
#print(account.balance)
#account.deposit(200)
#print(account.balance)
#account.commit()/
