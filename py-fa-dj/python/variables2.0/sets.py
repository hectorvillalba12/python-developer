#creando un conjunto set()
conjunto = set(["dato1","dato2"])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1", "dato 2"])
conjunto2 = {conjunto1, "dato3"}
print(conjunto2)

#TEORIA DE CONJUNTOS
conjunto3 = {1,3,5,7}
conjunto4 = {1,3,7}

resultado = conjunto4.issubset(conjunto3) #issubset (subconjunto) es un metodo
print(resultado)