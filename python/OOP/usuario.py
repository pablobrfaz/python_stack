
class User:
    def __init__(self, username, email_address):# ahora nuestro método tiene 2 parametros!
        self.name = username			#y usamos los valores pasados para establecer el atributo de nombre
        self.email = email_address		# y el atributo email
        self.account_balance = 0

    def make_deposit(self, amount):	# toma un argumento que es el monto del depósitocopy
        
    	self.account_balance += amount	

    def make_withdrawal(self, amount):	
    	self.account_balance -= amount	

    def display_user_balance (self, username, amount):
        self.name = username
        self.account_balance = amount
    
    def transfer_money(self, other_user, amount):
        self.name = other_user
        self.account_balance += amount


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
pablo = User("Pablo Bravo", "pbravo@python.com")

print(guido.name)	
print(monty.name)
print(pablo.name)

guido.transfer_money(monty.name,600)
guido.make_deposit(600)
guido.make_deposit(50)
guido.make_deposit(10)
guido.make_withdrawal(30)
print(guido.account_balance, guido.name)

monty.make_deposit(200)
monty.make_deposit(330)
monty.make_withdrawal(60)
monty.make_withdrawal(30)
print(monty.account_balance, monty.name)


pablo.make_deposit(20)
pablo.make_deposit(80)
pablo.make_deposit(30)
pablo.make_withdrawal(30)
print(pablo.account_balance, pablo.name)
