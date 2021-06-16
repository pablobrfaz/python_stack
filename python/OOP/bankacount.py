class BankAccount:
    def __init__(self,name,init_rate=0,balance=0,num_cuenta=0 ):
        self.name= name
        self.init_rate=init_rate/100
        self.balance=balance
        self.num_cuent=num_cuenta
    def deposit(self, amount,num_cuent):
        self.num_cuent= num_cuent
        self.balance+=amount
        return self
    def withdraw(self, amount,num_cuent):
        self.num_cuent=num_cuent
        if(self.balance-amount)>0:
            self.balance-=amount
        else:
            print("DINERO INSUFICIENTE")
        return self
    def display_account_info(self):
        return " Su saldo es:" + str(self.balance) +" Cuenta :"+self.num_cuent
    def yield_intereste(self):
        if(self.balance>0):
            aux=self.balance*self.init_rate
            self.balance+=aux
        return self


cuenta1 = BankAccount("cuenta1")
cuenta1.deposit(120,"123")
cuenta1.withdraw(100,"123")
print(cuenta1.name, cuenta1.balance)

