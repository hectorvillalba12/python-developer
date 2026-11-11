#forma no optima de sumar valores
def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
    return numeros_sumados

resultado = suma([5,3,9])
print(resultado)

#forma optima de sumar valores:
def suma_total(numeros):
    return sum([*numeros])
resultado2 = suma_total([3,6,5,7,8,])
print(resultado2)





#utilizando el operador (*) como argumento (*args)
def suma(nombre, *numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"

resultado = suma("hector",5,6,4,3,4,5)
print(resultado)