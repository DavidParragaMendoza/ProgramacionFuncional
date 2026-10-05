'''
10. Reto: Generador de reportes
Como servicio backend, procesa la siguiente estructura:

estudiantes = [
    {"nombre": "Ana",  "notas": [8, 9, 7],   "activo": True},
    {"nombre": "Luis", "notas": [5, 6, 4],   "activo": True},
    {"nombre": "Mara", "notas": [10, 9, 10], "activo": False},
    {"nombre": "Leo",  "notas": [7, 8, 9],   "activo": True},
]
Genera un reporte con los alumnos activos, su promedio calculado dentro de la lambda, ordenados descendentemente por promedio y desempatando alfabéticamente por nombre.

✔ Salida esperada: [("Ana", 8.0), ("Leo", 8.0), ("Luis", 5.0)]
💡 Pista de desempate: Si usas reverse=True, inviertes también el abecedario. Puedes evitarlo ordenando por key=lambda x: (-x[1], x[0]).
Bonus: Obtén al mejor estudiante activo en una línea usando max() con key.

'''

estudiantes = [
    {"nombre": "Ana",  "notas": [8, 9, 7],   "activo": True},
    {"nombre": "Luis", "notas": [5, 6, 4],   "activo": True},
    {"nombre": "Mara", "notas": [10, 9, 10], "activo": False},
    {"nombre": "Leo",  "notas": [7, 8, 9],   "activo": True},
]


reporte = sorted(
    # 2. Calcular promedios y generar reporte
    map(lambda estudiante: (estudiante["nombre"], sum(estudiante["notas"]) / len(estudiante["notas"])), 
        # 1. Filtrar estudiantes activos
        filter(lambda est: est["activo"], estudiantes)),
        # 3. Ordenar por promedio (descendente) y nombre (ascendente)
        key=lambda x: (-x[1], x[0]))

print(reporte)

#Mejor estudiante activo
mejorEstudiante = max(reporte, key=lambda x: x[1]) 
print(f"Mejor estudiante activo: {mejorEstudiante[0]}, Promedio: {mejorEstudiante[1]}")