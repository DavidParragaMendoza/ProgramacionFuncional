'''
Sintaxis de map
map(funcion, iterable)
ejemplo:
map(lambda x: x * 2, [1, 2, 3, 4])
'''

notas: list[int] = [7, 8, 9, 10]

BonosNotas: list[int] = list(map(lambda x: x+1, notas))

print(BonosNotas)