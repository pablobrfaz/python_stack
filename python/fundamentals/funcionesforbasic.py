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
            print ("El valor sumado es:", sum)
    return sum   
    

arr=[-1,1,1,1]
print (ejercicio3(arr)) 
