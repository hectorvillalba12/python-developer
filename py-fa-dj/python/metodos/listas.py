#list (crea una lista) (es una funcion)
lista = list(["hola","chau",39])
print(lista)

#len (devuelve la cantidad de elementos de una lista) (es una funcion)
print(len(lista))

#append (agregando un elemento a la lista)
print(lista.append(22))
print(lista)

#insert(agrega un elemento a la lista en un indice especifico)
print(lista.insert(2,"nos vemos"))
print(lista)

#extend (agrega varios elementos a la lista) (hay que pasarle una lista)
print(lista.extend([False, True]))
print(lista)

#pop (elimina un elemento de la lista (por su indice))
print(lista.pop(-2)) #-1 para eliminar el ultimo, -2 para eliminar el anteultimo, y asi sucesivamente

#remove (removiendo un elemento de la lista por su valor)
print(lista.remove("chau"))
print(lista)

#clear (elimina todos los elementos de una lista)
#print(lista.clear)

#sort (ordena una lista de forma ascendente a descendente)
#reverse - invierte los elementos de una lista
list = [32,33,23,False,True]
print(list.sort(reverse=True))
print(list.reverse())
print(list)

#index (verificando si un elemento se encuentra en la lista)
print(list.index(32))