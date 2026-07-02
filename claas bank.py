class bankaccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def deposit(self,ammount):
        self.balance +=ammount
        print(f"deposite:{ammount}")

    def  withadraw(self,ammount):
        if ammount<=2000:
            self.balance -= ammount
            print(f"witadraw: {ammount}")    
        else:
            print("unsuffisiant balance")

b1=bankaccount("kiran",3000)
print(b1.name)
b1.deposit(7000)
print(f"total balance is: {b1.balance}")
b1.withadraw(1000)
print(b1.deposit)
print(b1.withadraw)
print(f"balance for witdraw to: {b1.balance}") 