

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def addAccounts(self,x):
        self.accounts.append(x)

    def printInfo(self):
        print(self.name)
        print()
        for i in self.accounts:
            print(i)
            print()

class Customer:
    def __init__(self, *args):
        if len(args) == 1:
            self.name = args[0]
            self.age = 'Not Defined'
            self.gender = 'Not Defined'
        elif len(args) == 2:
            self.name = args[0]
            self.age = args[1]
            self.gender = 'Not Defined'
        else:
            self.name = args[0]
            self.age = args[1]
            self.gender = args[2]
    
    def __str__(self):
        return f'Name: {self.name} Age: {str(self.age)} Gender: {self.gender}'


class Account:
    def __init__(self,customer,balance):
        self.customer=customer
        self.balance=balance
    
    def __str__(self):
        return f'{self.customer.__str__()} Balance: {str(self.balance)}'
    

b = Bank('Goldman Sachs')
c1 = Customer('Jakob', 43, 'Male')
c2 = Customer('Jimmy', 27)
c3 = Customer('Mads',23, 'Male')



a1 = Account(c1,20000)
a2 = Account(c2,20000)
a3 = Account(c3,300000)



b.addAccounts(a1)
b.addAccounts(a2)
b.addAccounts(a3)


b.printInfo()


