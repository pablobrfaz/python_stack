def beCheerful(name='', repeat=2):		# asignar defaults cuando se declare los parámetros
	print(f"good morning {name}\n" * repeat)
beCheerful()				# salida: good morning (repeated on 2 lines)
beCheerful("tim")		        # salida: good morning tim (repeated on 2 lines)
beCheerful(name="john")			# salida: good morning john (repeated on 2 lines)
beCheerful(repeat=6)			# salida: good morning (repeated on 6 lines)
beCheerful(name="michael", repeat=5)	# salida: good morning michael (repeated on 5 lines)
# NOTA: el orden de loa argumentos no importa si estamos implícitos al enviar nuestros argumentos!
beCheerful(repeat=3, name="kb")		# salida: good morning kb (repeated on 3 lines)


def printInfo(some_dict):

   print(len(some_dict['locations']), "LOCATIONS")

   for location in some_dict['locations']:

       print(location)

   print()

   print(len(some_dict['instructors']), "INSTRUCTORS")

   for location in some_dict['instructors']:

       print(location)

seattle = {

   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],

   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']

}

printInfo(seattle)