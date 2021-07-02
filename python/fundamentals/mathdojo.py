class MathDojo: 
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        for i in range(len(nums)):
            self.result += nums[i]
        self.result += num
        return self
    def subtract(self,num,*nums): 
        for i in range(len(nums)):
            self.result -= nums[i]
        self.result -= num
        return self

# crear una instruccion:
md = MathDojo()

# para probar:
x = md.add(8).add(8,5).add(8,5,6).subtract(1).subtract(1,8).subtract(1,8,5).result
print(x)	# debe imprimir 
# corre cada uno de los metodos algunos mas veces y valida el resultado!
