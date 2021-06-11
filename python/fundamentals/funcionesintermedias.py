import random
def randInt(min=0   , max= 0  ):
    num=0
    if(min and max == 0):
        num = random.random() *50
    
    return num
print(randInt(0)) 		    # debería imprimir un número aleatorio entre 0 a 100