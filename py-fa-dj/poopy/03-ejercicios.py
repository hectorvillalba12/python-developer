#Ejercicio1
class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
        
nombre = input("Digame su nombre: ")
edad = input("Digame su edad: ")
grado = input("Por ultimo, su grado: ")

estudiante = Estudiante(nombre, edad, grado)
print(f"""""
    Datos del estudiante: \n\n
    Nombre: {estudiante.nombre} \n
    Edad: {estudiante.edad} \n
    Grado: {estudiante.grado} \n
    """)

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()