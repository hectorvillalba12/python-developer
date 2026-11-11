lista = ["hector", True, 1.90]
print(lista)
print(lista[1]) # asi accedemos a los elementos de la lista
lista[2] = "maquina" #asi cambiamos el dato de una lista
print(lista)

#tupla (no se pueden modificar)
tupla= ("hector", True, 1.90)
print(tupla)

#conjunto (set)
cojunto = {"hector", True, 1.90}
cojunto = {"crack"}
print(cojunto)

#diccionario (dict)
diccionario = {
    "nombre": "hector",
    "edad": 21,
    "altura": 1.90
}

print(diccionario)
print(diccionario["altura"]) #asi accedemos a un elemento del dict
