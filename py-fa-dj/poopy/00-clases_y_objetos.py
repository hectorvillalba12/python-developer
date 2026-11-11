#una clase es un tipo de objeto que podemos crear. nos permite definir las caracteristicas, cualidades -
# y todo lo que va a tener nuestro objeto.

#un objeto es una instancia de una clase.

class Celular():
    marca = "samsung"
    modelo = "5"
    camara = "48MP"
    
celular1 = Celular() #creamos un objeto y le preguntamos sus propiedades
print(celular1.marca)