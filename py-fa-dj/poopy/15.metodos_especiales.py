#los metodos especiales son funciones que tienen un nombre especial reservado.
#estan creados con la unica finalidad de que nosotros podramos crear funcionalidades especiales que con metodos normales no podriamos crearlos.


#contructor construye el objeto
class Persona:
    def __init__(self,name,age): 
        self.name = name
        self.age = age
        
    #(str)devuelve una respresentacion del objeto en una cadena de texto
    def __str__(self):
        return f"Persona(nombre={self.name},edad={self.age})"
    
    
    
hector = Persona("hector", 21)
print(hector)