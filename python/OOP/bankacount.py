
class BankAccount:
	def __init__(self, name): 
            self.name= name
            self.int_rate = 0.02
            self.balance = 0

	def deposit(self, amount):
		self.balance += amount
                
               
	def withdraw(self, amount):
		if amount > 0:
                 self.balance -= amount
                 print(self.balance)
                 return self
                          
                
                

	def display_account_info(self):
            print(self)


	def yield_interest(self, amount):
            if amount >0:
                self.balance = self.balance *self.int_rate 
                print("El interes de la cuenta es",self.balance)
                return self
                

cuenta1 = BankAccount("cuenta1")
cuenta2 = BankAccount("cuenta2")


cuenta1.deposit(700)
cuenta1.deposit(600)
cuenta1.withdraw(11)
print(cuenta1.balance, cuenta1.name)

cuenta1.yield_interest(600)