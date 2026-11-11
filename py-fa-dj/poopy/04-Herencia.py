#La herencia permite a la clase hija a acceder a todos los metodos y tener las propiedades de la clase padre.
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print("Hola, estoy hablando  un poco")
        
class Empleado(Persona): #empleado esta heredando los atributos de la clase persona
    def __init__(self,nombre, edad, nacionalidad, trabajo,salario):
        super().__init__(nombre,edad,nacionalidad) #esto queremos que herede lo hacemos con super e init.
        self.trabajo = trabajo
        self.salario = salario
        

roberto = Empleado("roberto",43,"argentino","dev",1000)
roberto.hablar()

    