print("Ejercicio1")
x = [ [5,2,3], [10,8,9] ] 
x[1]=[15,8,9]

print(x)

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]= {'first_name':  'Michael', 'last_name' : 'Briant'}
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['soccer']= 'Andres' , 'Ronaldo', 'Rooney'
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]
z[0]={'x': 10, 'y': 30}
print(z)

print("Ejercicio2")
def iteratedic(some_dict1):

    print(len(some_dict1),"FIRST_NAME")

    for x in some_dict1:

       print('first_name -',x['first_name'],',', 'last_name -', x['last_name'])

    print()


students = [
            {'first_name':  'Michael', 'last_name' : 'Jordan'},
            {'first_name' : 'John', 'last_name' : 'Rosales'},
            {'first_name' : 'Mark', 'last_name' : 'Guillen'},
            {'first_name' : 'KB', 'last_name' : 'Tonel'},
           
        ]

iteratedic(students)

print("Ejercicio3")
def iteratedic2(some_dict2):

    print(len(some_dict2),"Nombres y Apellidos")

    for x in some_dict2:

       print(x['first_name'])

    print()
    
    for x in some_dict2:

       print(x['last_name'])

    print()

students = [
            {'first_name':  'Michael', 'last_name' : 'Jordan'},
            {'first_name' : 'John', 'last_name' : 'Rosales'},
            {'first_name' : 'Mark', 'last_name' : 'Guillen'},
            {'first_name' : 'KB', 'last_name' : 'Tonel'},
           
        ]

iteratedic2(students)

print("Ejercicio4")
def iteratedic3(some_dict3):
   print(len(some_dict3['locations']), "LOCATIONS")

   for location in some_dict3['locations']:

       print(location)

   print()

   print(len(some_dict3['instructors']), "Instructors")

   for location in some_dict3['locations']:

       print(location)

   print()

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
iteratedic3(dojo)