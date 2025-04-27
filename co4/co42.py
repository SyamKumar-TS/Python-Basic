class account:
    def __init__(self,accnum,accname,acctype,balance=0):
        self.accnum=accnum
        self.accname=accname
        self.acctype=acctype
        self.balance=balance
        
    def deposit(self,amount):
        if amount>0:
            self.balance=self.balance + amount
            print("Depositted :",amount)
            print("New balance :",self.balance)
            
        else:
            print("less")
            
    def withdraw(self,amount):
        if 0<amount<=self.balance:
            self.balance=self.balance - amount
            print("Withdrawed :",amount)
            print("New balance :",self.balance)
            
        else:
            print("less")    
            
acc1=account(1234,'syam','saving',5000)   
print(acc1.deposit(500))
print(acc1.withdraw(5000))             
             
            
                
        
        