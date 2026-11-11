#Metodo De Resolocion De Orden

#Hacer referencia a el orden el que python busca metodos y atributos en las clases.

class A:
    def hablar(self):
        print("Hola desde A")

class B(A):
    def hablar(self):
        print("Hola desde B")
        
class C(A):
    def hablar(self):
        print("Hola desde C")
        
class D(B,C):
    def hablar(self):
        print("Hola desde D")
        
d = D()
d.hablar()

print(C.mro())#con mro nos dice el orden de como se ejecutan las clases