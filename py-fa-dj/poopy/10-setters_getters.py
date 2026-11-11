#getters:es un metodo que tenemos que utilizar para acceder a un atributo que es muy privado
#setters:modificar o establecer el valor de un atributo privado.

#son metodos para acceeder a propiedades privadas que tienen las clases. no solo acceederlas sino tambien modificarlo.

class Persona:
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self._edad = edad
        
    def get_nombre(self): #obtener nombre (get)
        return self._nombre
    
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre

hector = Persona("hector",21)
nombre = hector.get_nombre()
print(nombre)

hector.set_nombre("juan")
nombre = hector.get_nombre()
print(nombre)


