
print('Ejercicio1')
def ejercicio1():
    num=5
    for x in range(0, num+1, 1):
        print ('El numero es',[num-x])

ejer1=ejercicio1()

  
print('Ejercicio2')
def ejercicio2():
    num=[3,2]
    for x in num:
        if(x>=num[0]):
            print ("El primer número es",num[0])
    print ("El número retornado es",x)
   
ejer2=ejercicio2() 

""" print('Ejercicio3')
def ejercicio3():
    num=[]
    for x in range(5):
        val= int (input("ingrese el valor:"))
        num.append(val)

    for x in num:
        var=num[0]+len(num)
    print("El Primer valor de la lista mas la longitud de la lista es",var)

    return num
ejer3=ejercicio3() """

print('Ejercicio4')
def ejercicio4():   
    tam=4
    val=[7]

    for y in range(0,tam,1):
        print("la lista es ",val)

ejer4=ejercicio4() 
