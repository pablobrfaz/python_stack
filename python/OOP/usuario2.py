
class User:
    def __init__(self, username, email_address):# ahora nuestro método tiene 2 parametros!
        self.name = username			#y usamos los valores pasados para establecer el atributo de nombre
        self.email = email_address		# y el atributo email
        self.account_balance = 0
        

    def ake_withdrawal (self, username, amount):
        self.name = username
        if(self.account_balance - amount)>0:  
            self.account_balance -= amount
        else:
            print("No tiene el dinero suficiente")
        return self
    
    def make_deposit(self, other_user, amount):
        self.name = other_user
        self.account_balance += amount
        return self


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
pablo = User("Pablo Bravo", "pbravo@python.com")


guido.make_deposit(monty.name,600).make_deposit(monty.name,600).ake_withdrawal(guido.name, 300)
print(guido.account_balance, guido.name)
