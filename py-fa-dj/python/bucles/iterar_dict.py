dict = {
    "nombre" : "hector",
    "apellido" : "villalba",
    "edad" : 21
}

#recorriendo diccionario con items() 
for key in dict.items():
    print(key)
    
#recorriendo diccionario con items() para obtener la clave y el valor
for datos in dict.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es: {key} y el valor es: {value}")
    