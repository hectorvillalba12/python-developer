#el property nos permite definir getters,setters y deleters.
class Persona:
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self._edad = edad
    
    @property   
    def nombre(self): #obtener nombre (get)
        return self._nombre
    
    @nombre.setter
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre
            
hector = Persona("hector",21)
nombre = hector.nombre
print(nombre)
