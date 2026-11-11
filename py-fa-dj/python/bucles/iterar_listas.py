animales = ["gato","perro","loro","cocodrilo"]
#recorriendo la lista animales
for animal in animales:
    print(f"Ahora la varible animal es igual a: {animal}")
    
#recorriendo la lista numeros
numeros =[30,22,33,45]
for numero in numeros:
    resultado = numero * 40
    print(resultado)
    
#recorriendo dos listas del mismo tamaño al mismo tiempo
for numero,animal in zip(animales,numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2 : {animal}")
    

#con range
for num in range(5,10):
    print(num)
    

#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice} y el valor es: {valor}")
    
#usando el for else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("el bucle termino")

#todo LO ANTERIOR FUNCIONA PARA TUPLAS Y CONJUNTOS.