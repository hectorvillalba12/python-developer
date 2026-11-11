frutas = ["banana","manza","ciruela","pera","naranja","durazno"]
#evitando que se coma una naranja con la sentencia continue
for fruta in frutas:
    if fruta == "naranja":
        continue #continua con el siguiente elemento 
    print(f"me voy a comer una {fruta}")
    
#evitando que el bucle siga ejecutandose
for fruta in frutas:
    if fruta == "pera":
        break #termina el bucle
    print(f"me voy a comer una {fruta}")
print("bucle terminado")

#recorrer un cadena de texto
cadena = "hola hector"
for letra in cadena:
    print(letra)

#for en una sola linea de codigo
numeros = [2,5,8,10]
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
