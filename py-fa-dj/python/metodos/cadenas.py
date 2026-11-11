# Los  metodos son funciones aplicadas a objetos
#todos los metodos son funciones pero no todas las funciones son metodos

cadena1 = "hola-me-llamo-hector"
cadena2 = "bienvenido"

#dir (devuelve la lista de atributos validos del objeto pasado) (ejecuta algo) (una funcionde python)
print(dir(cadena1))

#upper (convierte a mayuscula)
print(cadena1.upper())

#lower (convierte a minuscula)
print(cadena1.lower())

#capitalize (convierte la primera letra en mayuscula)
print(cadena1.capitalize())

#find(buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1)
print(cadena1.find("d"))

#index (buscamos una cadena en otra cadena,si no hay coincidencias lanza una excepcion)
print(cadena1.index("l"))

#isnumeric (si es numerico devuelve true sino devuelve false)
print(cadena1.isnumeric())

#isalpha (si es alfanumerico devuleve true sino devuelve false)
print(cadena1.isalpha())

#count (contamos las coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de veces que coincida)
print(cadena1.count("a"))

#len (cuenta la cantidad de caracteres que tiene una cadena) (es una funcion)
print(len(cadena1))

# startwith (verificamos si una cadena empieza con otra cadena dada, si  es asi devuelve true)
print(cadena1.startswith("h"))

#endswith (verificamos si una cadena termina con otra cadena dada, si  es asi devuelve true)
print(cadena1.endswith("r"))

#replace (remplaza un pedazo de la cadena dada, por otra dada)
print(cadena1.replace("hola","holi"))

#split (separar cadenas con la cadena que le pasemos) (crea una lista)
print(cadena1.split("-"))