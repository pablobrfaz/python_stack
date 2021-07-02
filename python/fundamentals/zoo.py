class Zoo:
    def __init__(self, zoo_nombre):
        self.animals = []
        self.nombre = zoo_nombre
    def add_lion(self, nombre,edad, nivelsalud, nivelfelicidad, habitat):
        self.animals.append( Leon(nombre,edad,nivelsalud,nivelfelicidad,habitat) )
        return self
    def add_tiger(self,  nombre,edad,nivelsalud,nivelfelicidad,habitat):
        self.animals.append( Tigre(nombre,edad,nivelsalud,nivelfelicidad,habitat) )
        return self
    def print_all_info(self):
        print("-"*30, self.nombre, "-"*30)
        for animal in self.animals:
            animal.display_info()

class Animal(Zoo):
    def __init__(self,nombre,edad,nivelsalud,nivelfelicidad):
        self.nombre = nombre
        self.edad = edad
        self.nivelsalud = nivelsalud
        self.nivelfelicidad = nivelfelicidad
    def display_info(self):
        print("Nombre:",self.nombre,"-Nivel de Salud:",self.nivelsalud,"-Nivel de Felicidad:",self.nivelfelicidad,"-Se encuentran en el Habitat de:", self.habitat)
        return self
    def alimentacion(self):
        self.nivelsalud += 10
        self.nivelfelicidad += 10
        print("-"*30,self.nombre,"Esta Comiendo!!", "-"*30)
        return self

class Leon(Animal):
    def __init__(self, nombre, edad, nivelsalud, nivelfelicidad,habitat):
        super().__init__(nombre, edad, nivelsalud, nivelfelicidad)
        self.habitat = habitat

class Tigre(Animal):
    def __init__(self, nombre, edad, nivelsalud, nivelfelicidad,habitat):
        super().__init__(nombre, edad, nivelsalud, nivelfelicidad)
        self.habitat = habitat
class Oso(Animal):
    def __init__(self, nombre, edad, nivelsalud, nivelfelicidad,habitat):
        super().__init__(nombre, edad, nivelsalud, nivelfelicidad)
        self.habitat = habitat

alex = Leon("Alex",5,90,90,"Central Park")
mufasa = Tigre("Mufasa",10,50,50,"Selva")
peresoso = Oso("Peresoso",12,80,50,"Rio")

peresoso.display_info()
peresoso.alimentacion().display_info()
zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala",1,80,90,"Central Park")

zoo1.add_lion("Simba",2,70,90,"Central Park")

zoo1.add_tiger("Rajah",3,78,60,"Central Park")

zoo1.add_tiger("Shere Khan",4,80,75,"Central Park")

zoo1.animals[0].alimentacion().display_info()
zoo1.animals[1].alimentacion().display_info()
zoo1.animals[2].alimentacion().display_info()
zoo1.animals[3].alimentacion().display_info()
zoo1.print_all_info()

