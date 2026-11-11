#Consiste en proteger los elementos de una clase.
#podemos proteger metodos,variables,etc.

class MiClase:
    def __init__(self):
        self.__atributo_privado = "valor"
        
objeto = MiClase()
print(objeto.__atributo_privado)

#def _hablar(self) #metodo privado

#getters:es un metodo que tenemos que utilizar para acceder a un atributo que es muy privado
#setters:modificar o establecer el valor de un atributo privado.