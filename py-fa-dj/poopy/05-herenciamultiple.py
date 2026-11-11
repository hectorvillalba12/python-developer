class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print("Hola, estoy hablando un poco")
        
class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        return(f"mi habilidad es: {self.habilidad}")

        
class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad,habilidad,empresa,salario):
        Persona.__init__(self,nombre, edad, nacionalidad) #de persona heredamos nombre,edad y nacionalidad
        Artista.__init__(self,habilidad)#de Artista heredamos la habilidad
        self.salario = salario
        self.empresa = empresa
    
    def presentarse(self):
        print(f"Hola, soy: {self.nombre}, {self.mostrar_habilidad()} y trabjo en {self.empresa}")
        
Hector = EmpleadoArtista("Hector",43,"argentino","cantar","programador",100000)
Hector.presentarse()

herencia = issubclass(Artista,Persona) #artista es una subclase de persona?
intancia = isinstance(Hector,EmpleadoArtista) #Hector es una instancia de la clase EmpleadoArtista?
print(herencia,intancia)