#una clase abstracta es una clase que no podemos instanciar.
#las clases abstractas sirven para crear diferentes implementaciones para tener una planilla unica.

from abc import ABC, abstractclassmethod 

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"hola, me llamo: {self.nombre} y tengo {self.edad} años")
        
    
class Estudiante(Persona):
    def __init__(self, name, edad, sexo, actividad ):
        super().__init__(name,edad,sexo,actividad)
        
        
    def hacer_actividad(self):
        print(f"estoy estudiando: {self.actividad}")


class Trabajador(Persona):
    def __init__(self, name, edad, sexo, actividad ):
        super().__init__(name,edad,sexo,actividad)
        
        
    def hacer_actividad(self):
        print(f"Actualmente estoy trabajando en el rubro de la: {self.actividad}")



hector = Estudiante("hector", 21, "masc", "programacion")
pedro = Trabajador("pedrito",30,"masc","programacion")
hector.hacer_actividad()
pedro.hacer_actividad()