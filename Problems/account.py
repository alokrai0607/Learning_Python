class Account :
    def __init__(self,AccBal,AccNo):
        self.AccBal = AccBal
        self.AccNo = AccNo


    def selfBal(self):
        return self.AccBal
    
    def debitBal(self , amount):
        self.AccBal -= amount
        print("Rs ",amount, "was debited")
        print("Total balanece is ",self.selfBal())

    def creditBal(self , amount):
        self.AccBal += amount
        print("Rs ",amount, "was credited")
        print("Total balanece is ",self.selfBal())

acc1 = Account(100000 , 1254425100)
print((acc1.AccBal))
print((acc1.AccNo))
