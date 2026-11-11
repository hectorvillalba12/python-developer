#Es hacer que cuando nosotros le demos un metodo a un objeto se comporte diferente entiendo que sus propiedades son diferentes.
class Gato():
    def sonido(self):
        return "miau"
    
class Perro():
    def sonido (self):
        return "guau"

    
gato = Gato()
perro = Perro()
print(gato.sonido())