
class BankAccount:
    def __init__(self,init_rate=0,balance=0,num_cuent=0):
        self.init_rate=init_rate/100
        self.balance=balance
        self.num_cuent=num_cuent
    def deposit(self, amount,num_cuent):
        self.num_cuent=num_cuent
        self.balance+=amount
        return self
    def withdraw(self, amount,num_cuent):
        self.num_cuent=num_cuent
        if(self.balance - amount)>0:
            self.balance-=amount
        else:
            print("No tiene el dinero suficiente")
        return self
    def display_account_info(self):
        return " Saldo : "+ str(self.balance) +" Cuenta : "+self.num_cuent
    def yield_interest(self):
        if(self.balance>0):
            aux=self.balance*self.init_rate
            self.balance+=aux
        return self
class User:
    def __init__(self,name,email,cuenta):
        self.name=name
        self.email=email
        self.account=BankAccount(init_rate=0.00,balance=0,num_cuent=cuenta)
    def make_deposit(self,amount,cuenta):
        self.account.deposit(amount,num_cuent=cuenta)
        return self
    def make_withdrawal(self,amount,cuenta):
        self.account.withdraw(amount,num_cuent=cuenta)
        return self
    def display_user_balance(self,cuenta):
        print("Usuario: "+ self.name+ str(self.account.display_account_info()))
        return self
    def example_method(self):
        self.account.deposit(100)
        print(self.name, self.account.balance)
        return self
usr1=User("Pablo", "pablo@python.com","123")
usr2=User("Pepe",  "pepe@python.com","1234")
usr3=User("luis",  "luis@python.com",1234)

usr1.make_deposit(100,"1234")
usr1.make_withdrawal(150,"1234")
usr1.display_user_balance("1234")