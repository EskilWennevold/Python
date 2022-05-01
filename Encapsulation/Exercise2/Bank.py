class Bank:
    def __init__(self):
        self._accounts=[]
    
    @property
    def accounts(self):
        return self._accounts
    
    @accounts.setter
    def accounts(self, account):
        if(len(self._accounts) == 0):
            self._accounts.append(account)
        else:
            if(self._accounts[0].cust != account.cust):
                self._accounts.append(account)
    
class Account:
    def __init__(self, no, cust):
        self.no=no
        self.cust=cust

    @property
    def no(self):
        return self._no
    
    @no.setter
    def no(self, no):
        self._no=no
    
    @property
    def cust(self):
        return self._cust
    
    @cust.setter
    def cust(self, cust):
        self._cust=cust

class Customer:
    def __init__(self, name, age):
        if(age >= 18):
            self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name=name

cust = Customer("Eric", 18)
acc = Account(2000,cust)
acc1 = Account(2000,cust)


bank = Bank()
bank.accounts = acc
bank.accounts = acc1
print(bank.accounts)


