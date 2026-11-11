#las funciones son codigos que ya estan creados. Para que nosotros reutilizemos como queramos.
#Una funcion es un fragmento de codigo que podemos utilizar en cualquier momento.
#las funciones build-in son funciones integradas por python.

#Encontrando el numero mayor de una lista
numeros = [4,7,1,22,34]
numeros_mas_alto = max(numeros)
print(numeros_mas_alto)

#Encontrando el numero menor de una lista
numeros_mas_bajo = min(numeros)
print(numeros_mas_bajo)

#redondeando a 6 decimales
numero = round(12.32344,2) #con la coma ponemos los decimales que queramos dejar
print(numero)

#retorna false -> 0, vacio, false , none \ True --> distinto a  0, true, cadena, dato no vacio
resultado_bool = bool("dddd")
print(resultado_bool)

#Retorna true, si todos los valores son verdaderos
resultado_all = all([22,"false",[222]])
print(resultado_all)

#suma todos los valores de un iterable
suma_total = sum(numeros)
print(suma_total)