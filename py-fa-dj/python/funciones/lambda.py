#lambda es una forma de crear una funcion anonima (es anonima porque no tiene nombre)
#podemos almacenarlas en varibles
#retorna automaticamente

#creando una funcion lambda para multiplicar por 2
multiplicar_por_dos = lambda x : x*2
print(multiplicar_por_dos(5)) # va a devolver 10

#creando una funcion comun que diga si es para o no
def es_par(num):
    if(num%2==0):
        return True

#usando filter con una funcion comun. (sirve para usar una funcion que nos devuleva true/false y que haga una lista para todos los valores eran true)
numeros =[1,2,3,4,5,6,7,8,9,10]
numeros_pares = filter(es_par,numeros)
print(list(numeros_pares))

#creando lo mismo que antes pero con lambda
numeros_pares = filter(lambda numero:numero%2 == 0, numeros)
print(list(numeros_pares))