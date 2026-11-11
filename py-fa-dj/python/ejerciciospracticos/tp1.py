#promedio de duracion
minimo = 2.5
maximo = 7 #lento
promedio = 4 #promedio
curso = 1.5 #mas rapido

crudo = 5
crudocurso = 3.5

#a) diferencia en porcentaje entre el curso actual y -el mas rapido, -mas lento y el promedio de los cursos
diferencia_minima= 100 - curso / minimo * 100
diferencia_maxima= 100 - curso / maximo * 100
diferencia_promedio= 100 - curso / promedio * 100
print(f"el curso dura un {diferencia_minima}% menos que el mas rapido")
print(f"el curso dura un {diferencia_maxima}% menos que el mas rapido")
print(f"el curso dura un {diferencia_promedio}% menos que el mas rapido")

#duracion de crudos (video sin editar)
crudo_promedio = 5
crudo_dalto = 3.5
#calculando el porcentaje de tiempo vacio removido
tiempo_promedio_vacio = 100 - promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - curso * 1000 // crudo_dalto / 10
#b)mostrando la cantidad de espacios vacios que se remueven (ejercio b)
print(f"un curso promedio elimina un {tiempo_promedio_vacio}% de tiempo vacio")
print(f"este curso elimino el {tiempo_vacio_dalto}% de tiempo vacio")

#Mostrando diferencias si los cursos duraran 10 horas
print(f"ver 10 horas de este curso equivale a ver {promedio * 1000 // curso / 100 }")
