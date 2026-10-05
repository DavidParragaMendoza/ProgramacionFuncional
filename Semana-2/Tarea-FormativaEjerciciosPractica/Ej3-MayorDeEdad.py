'''
3. Filtrado con filter
De edades = [15, 22, 17, 30, 16, 41], conserva únicamente las edades de personas que pueden votar legalmente (18 años o más).
💡 Pista: La condición debe retornar un booleano (True o False), no alterar el elemento.
'''

#lista de edades
listaEdaddes:list[int] = [15, 22, 17, 30, 16, 41]


#filtrar las edades mayores o iguales a 18
mayorDeEdad= list(
    filter(lambda edad: edad >=18, listaEdaddes)
)

#mostrar el resultado
print(mayorDeEdad)