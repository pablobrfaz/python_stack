def varargs(arg1, *args):
    print("Got ", arg1, " and ", args)
varargs("one") 			# salida: Got one and ()
varargs("one", "two") 	        # salida: Got one and ('two',)
varargs("one", "two", "three")  

def varargs(arg1, *args):
    for a in args:
    	print(a)
varargs("one", "two", "three") # salida: two, three


class MathDojo:
    def __init__(self):
    	self.result = 0
    def add(self, num, *nums):
        self.num= num
        print(num,nums)

    def subtract(self, num, *nums):
    	self.num= num
        print(num,nums)

# crear una instruccion:
md = MathDojo()
# para probar:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# debe imprimir 5
# corre cada uno de los metodos algunos mas veces y valida el resultado!