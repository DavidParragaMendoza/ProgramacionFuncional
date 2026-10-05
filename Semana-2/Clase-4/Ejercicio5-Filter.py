'''
Sintaxis de filter
filter(funcion, iterable)
ejemplo:
filter(lambda x: x > 5, [1, 2, 3, 4, 5, 6, 7, 8])
'''

notas: list[int] = [1,2,3,4,5,6,7, 8, 9, 10]

aprobados: list[int] = list(filter(lambda x: x >= 7, notas))

print(aprobados)