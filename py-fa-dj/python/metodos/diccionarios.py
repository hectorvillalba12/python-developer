dict = {
    "nombre_completo" : "hectorvillalba",
    "edad" : 23,
    "titulo": "developer"
}

#keys() (devulve las claves (tambien nos sirven para iterar))
print(dict.keys())

#get() (devuelve el valor de una clave) (no me lanza ninguna excepcion y si no encuentra nada el programa continua)
print(dict.get("edad"))

#clear (elimina todo el diccionario)
#print(dict.clear())

#pop() (eliminando un elemento del diccionario)
print(dict.pop("nombre_completo"))

#items (obtiene un elemento iterable)
print(dict.items())