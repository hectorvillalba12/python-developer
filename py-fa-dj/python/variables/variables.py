nombre = "hector"
apellido = "villalba"

print (nombre, apellido)

numero = 10
numero += 1
print(numero) #da 11

#concatenacion
nombre = "hector"
bienvenida = "hola " + nombre + " ¿como estas?"
print(bienvenida)

#concateancion con f strings
nombre = "ramon"
bienvenido = f"hola {nombre} que hace?"
print(bienvenido)

#operador (del) -> sirve para que una variable no este mas declarada, es un operador para borrar datos
#ejemplo-> del bienvenida

#operador de pertenencia (in/not in)
nombre = "juan"
hola = f"esta {nombre} aca"

print("juan" not in hola)


