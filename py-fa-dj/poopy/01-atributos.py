#los atributos son variables que pertenecen a una clase

#atributos de instancia: son las que nosotros las definimos cuando instaciamos una clase (osea cuando creamos un objet0)

class Celular:
    def __init__(self, marca, modelo , camara): #init es un metodo costructor, (self) es una forma de hacer referencia a si mismo (al mismo objeto).
        self.marca = marca #definimos las propiedades. creamos la propiedad con self y luego accedemos al parametro
        self.modelo = modelo
        self.camara = camara
    
celular1 = Celular("samsung", "S23","48MP") 
celular2 = Celular("apple", "14", "50MP")
print(celular1.marca)
