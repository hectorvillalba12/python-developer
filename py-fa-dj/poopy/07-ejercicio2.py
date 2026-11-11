#ejercicio1 de herencia y uso de super:
#Crear un sistema para una escuela.En este sistema, vamos a tener dos clases principales:-
#Persona y Estudiante. La clase Persona tendra los atributos de nombre y edad y un metodo-
#que imprima el nombre y la edad de la persona. La clase Estudiante heredara de la clase Persona-
#y tambien tendra un atributo adicional: grado y un metodo que imprima el grado del estudiante.

#Deberas utilizar super en el metodo de inicializacion (init) para reutilizar el codigo de la clase-
#padre(persona). luego crea una instancia de la clase Estudiante e imprime sus atributos y utiliza sus-
#metodos para asegurarte de que todo funciona correctamente.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def mostrar_datos(self):
        print(f"el nombre es: {self.nombre} ")
        print(f"la edad es: {self.edad}")
    
    
    
class Estudiante(Persona):
    def __init__(self, nombre, edad,grado):
        super().__init__(nombre, edad)
        self.grado = grado
        
    def mostrar_grado(self):
        print(f"Grado: {self.grado}")
        

estudiante = Estudiante("Hector",21,"2do")
estudiante.mostrar_datos()
estudiante.mostrar_grado()

#Ejercicio 2: ejercicio de herencia y MRO:
#Imagina que estas modelando animales en un zoologico. Crear tres clases: "Animal", "Mamifero" y "Ave".-
#La clase "Animal" debe tener un metodo llamado "comer". La clase "mamifero" debe tener un metodo llamado -
#"amamantar" y "volar", ademas de "comer".-

#Finalmente, juega con el orden de herencia de la clase "murcielago" y observa como cambia el MRO y -
#el comportamiento de los motodos al usas super().

class Animal:
    def comer(self):
        print("el animal esta comiendo")
    
class Mamifero(Animal):
    def amamantar(self):
        print("el animal esta amamantando")
        
    
class Ave(Animal):
    def volar(self):
        print("el animal esta volando")
    
class Muercialgo(Mamifero,Ave):
    pass

mamifero = Mamifero()
mamifero.comer()
#mamifero.volar()
mamifero.amamantar()
