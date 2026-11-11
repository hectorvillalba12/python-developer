#Un metodo es una funcion.
#Todas las funciones que creemos dentro de una clase son metodos.
#Los metodos sirven para que definamos las acciones que pueda hacer nuestro objeto.

class Celular:
    def __init__(self, marca, modelo , camara): 
        self.marca = marca #
        self.modelo = modelo
        self.camara = camara
    
    def llamar(self): #metodo
        print(f'estas haciendo un llamado desde un: {self.modelo}')
    
    def cortar(self):
        print(f'el celular que esta cortando es : {self.marca}')
        
celular1 = Celular("samsung", "S23","48MP") 
celular2 = Celular("apple", "14", "50MP")

celular1.llamar()
celular2.cortar()
