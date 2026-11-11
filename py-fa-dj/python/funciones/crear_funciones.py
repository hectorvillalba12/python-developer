#def- se utiliza para decirle al programa que vamos a crear nuestra propia funcion

#creando  una funcion simple.
def saludar():
    print("hola hector, como estas?")
    
#ejecutando la funcion simple
saludar() 

#creando una funcion que tenga parametros (los parametros son variables que se crean para ser usados dentro de la funcion)
def saludo(nombre):
    print(f"hola {nombre} como estas?")
saludo("pibe")

#otro ejemplo

def alumno(nombre,sexo):
    if(sexo == "femenino"):
        adjetivo = "alumna"
    elif (sexo == "masculino"):
        adjetivo = "alumno"
    else:
        adjetivo = "binario"
    print(f"hola {nombre}, mi {adjetivo} como andas?")
    
alumno("roman", "masculino")

#crear una funcion que nos retorne multiples valores
def crear_contrasenia_random(num):
    list_de_caracteres = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contrasenia = f"{list_de_caracteres[c1]}{list_de_caracteres[c2]}{list_de_caracteres[c3]}{num*2}"
    return contrasenia, num #retornar valores lo que nos permite es el dato poder guardarlo
#desempaquetando la funcion
password, primer_numero = crear_contrasenia_random(2)
print(f"Tu contraseña nueva es: {password}")
print(f"El numero utilizado para crearla fue: {primer_numero}")


