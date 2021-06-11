print('Ejercicio1')
def ejercicio1(num):
    
    for x in range(0,len(num),1):
        if(num[x]>0):
            print ("BIG")
            
        else:
            print (num[x])
            
num=[-1,3,5,-3]   
ejer1=ejercicio1(num) 


print("Ejercicio3")
def ejercicio3(arr):  
    sum=0
    for y in arr:
        if(arr[y]>0):
            sum+= y
            
    return sum   
    

arr=[-1,1,1,1]
print ("La suma del array completo es:",ejercicio3(arr)) 

print("Ejercicio4")
def ejercicio4(arr1):  
    sum=0
    
    for y in arr1:
            sum+= y / len(arr1)
    return sum    

arr1=[1,2,3,4]

print ("El promedio del array completo es:",ejercicio4(arr1)) 


print("Ejercicio5")
def ejercicio5(arr1):  
    sum=0
    
    for y in arr1:
            sum= len(arr1)
    return sum    

arr1=[]

print ("La Longuitud del array completo es:",ejercicio5(arr1)) 

print('Ejercicio6')
def ejercicio6(num):
    
    for x in range(0,len(num),1):
        if(num[x]<0):
            print ("El minimo de la lista es",num[x])
            
    if(len(num)==0):
        print ("False")
        
            
num=[1,-1,3]  
ejer6=ejercicio6(num)

print('Ejercicio7')
def ejercicio7(num):
    
    for x in range(0,len(num),1):
        if(num[x]>0):
            print ("El numero maximo de la lista es",num[x])
        
    if(len(num)==0):
        print ("False")
    

            
num=[1,-1,3]  
ejer7=ejercicio7(num)

print('Ejercicio9')
def ejercicio9(num):
    num=[37,2,1,-9]
    num.reverse()
    print (num)


ejer9=ejercicio9(num)


