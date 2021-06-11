import random
def randInt(min=0   , max= 50  ):
    num=0
    if(max ==50 ):
        num = random.random() *50
    
    return num
print("debería imprimir un número aleatorio entre 0 a 50:",randInt(max=50)) 		

def randInt1(min=50   , max= 0  ):
    num=0
    if(min ==50 ):
        num = random.random() *50 + 50
    
    return num
print("debería imprimir un número aleatorio entre 50 a 100:",randInt1(min=50)) 	

def randInt3(min=50   , max= 500  ):
    num=0
    if(min >=50 and  max<=500):
        num = random.random() *50 + 450
    
    return num
print("debería imprimir un número aleatorio entre 50 a 500:",randInt3(min=50, max=500)) 

def randInt2(min=0  , max=0  ):
    num=0
    if(min == 0 and max == 0 ):
        num = random.random() *100
    
    return num
print("debería imprimir un número aleatorio entre 0 a 100:",randInt2()) 