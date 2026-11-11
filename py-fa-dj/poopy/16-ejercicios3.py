#crear un juego de fusion:

#el juego consiste en crear personajes un juego y esos personajes se puedan fusionar-
#para formar personajes mas poderosos que tengan mas podes.-
#para ello deberemos cambiar el comportamiento del operador "+" para que cuando los personajes -
#se fusionen,salga un nuevo  personaje con habilidades mejoradas.-
#una posible formula es: el promedio de las habilidades de ambos, al cuadrado.

class Personaje:
    def __init__(self,nombre,fuerza,velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
    
    def __repr__(self):
        return f"{self.nombre} Fuerza: {self.fuerza}, Velocidad: {self.velocidad}"
    
    #sumar
    def __add__(self, otro_pj):
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nueva_fuerza = ((self.fuerza + otro_pj.fuerza)/2)**2
        nueva_velocidad = ((self.velocidad + otro_pj.velocidad)/2)**2
        return Personaje(nuevo_nombre,nueva_fuerza,nueva_velocidad)
        
        
goku = Personaje("goku",100,100)
vegeta = Personaje("vegeta",99,99)
jiren = Personaje("jiren",1000,1000)


vegito = goku + vegeta
jireto = vegito + jiren
print(jireto)