'''
Problema
Dada una lista de calificaciones, obtener otra lista con las notas aprobadas ajustadas con un punto extra.
'''
notas : list[int] = [5, 8,9,6,10]
'''
aprobadas: list[int] = []

for nota in notas:
    if nota >= 7:
        aprobadas.append(nota + 1)
'''

aprobadas = list(
    map(lambda nota: nota +1,
        filter(lambda nota: nota >=7, notas))
)


print (aprobadas)


