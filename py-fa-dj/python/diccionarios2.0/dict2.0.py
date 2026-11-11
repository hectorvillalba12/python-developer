#creando diccionarios con dict()
diccionario = dict(nombre="hector",apellido="villalba")

#las listas no pueden ser claves porque son mutables y usamos frozenset para meter conjuntos
diccionario = {frozenset(["dalto","rancio"]):"jajaj"}

#creando diccionarios con fromkeys (todos los valores none)
diccionario = dict.fromkeys(["nombre","apellido"])

#creando diccionarios con fromkeys() cambiando el valor por defecto  a "no se"
diccionario = dict.fromkeys(["nombre","apellido"],"nose")