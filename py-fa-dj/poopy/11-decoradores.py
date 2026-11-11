# En python un decorador es una funcion que decora a otra.(agrega un codigo extra a la funcion que ya existia).

def decorador(funcion): #funcion decoradora
    def funcion_modificada():#creacion de la funcion
        print("antes de llamar a la funcion")#ejecuta un codigo antes
        funcion()#ejecuta la funcion que le pasamos como parametro
        print("despues de llamar a la funcion")#ejecuta un codigo despues
    return funcion_modificada #nos devuelve la funcion que creo

# def saludo():
#     print("hola juan")

# saludo_modificado = decorador(saludo)
# saludo_modificado()

@decorador #funcion decoradora
def saludo(): 
    print("hola juan")
saludo()
