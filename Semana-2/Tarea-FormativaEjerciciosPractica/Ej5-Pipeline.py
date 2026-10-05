'''
5. Pipeline funcional: Composición
A partir de notas = [4, 7, 9, 3, 8, 6] realiza en cadena:

Conservar únicamente calificaciones aprobadas (>= 6).
Sumar 1 punto extra de bonificación a cada nota aprobada.
Ordenar el resultado de mayor a menor.
💡 Pista: Lee de adentro hacia afuera: aplica filter, pasa el resultado a map, y finalmente a sorted(..., reverse=True).

'''


listaNotas = [4, 7, 9, 3, 8, 6]

#ordenar las notas aprobadas con bonificación de mayor a menor
notasAprobadas = sorted(
    map(lambda nota: nota +1, 
        filter(lambda nota: nota >=6, listaNotas)),
        key=lambda nota: nota, reverse=True
)
print(notasAprobadas)
