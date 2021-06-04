    

print("Ejercicio 1")
for x in range(151):
    print(x)


print("Ejercicio 2")
for y in range(5, 1005, 5):
    print(y)

print("Ejercicio 3")
for z in range(1, 101, 1):
    print(z)
    if z%5 == 0: 
       print(z,"Conding")   
    if z%10 ==0:
       print(z,"CodingDojo")
 

print("Ejercicio 4") 
sum=0
i = 0
while i < 500000:
    
    if i % 2 != 0 :        
        sum+= i
    
    i +=1

print("La suma de los numeros impares es:",sum)

print("Ejercicio 5")
for y in range(2018, 1, -5):
    print(y)
 

print("Ejercicio 6")
lowNum=2
highNum=9 
mult=3
for h in range(1, highNum+1, 1):
    
    if h%3 == 0: 
       print("Los numeros multiplos son:",h)
