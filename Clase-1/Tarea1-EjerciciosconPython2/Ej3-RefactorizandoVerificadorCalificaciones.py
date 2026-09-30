'''
Ejercicio 3: Refactorizando el Verificador de Calificaciones
Crea una función obtener_feedback_calificacion(calificacion: float) que retorne un texto ("Sobresaliente", "Notable", etc.) basado en la nota.

Llama a la función e imprime el feedback retornado.
'''


def obtenerFeedbackCalificacion(calificacion: float) -> str:
    if calificacion >= 9:
        return "Sobresaliente"
    elif calificacion >= 8:
        return "Notable"
    elif calificacion >= 7:
        return "Bien"
    else:
        return "Insuficiente"

# Llamamos a la función y guardamos el resultado
calificacion: float = float(input("Ingrese la calificación: "))
# Obtenemos el feedback basado en la calificación
feedback: str = obtenerFeedbackCalificacion(calificacion)
# Imprimimos el feedback
print(f"El feedback para la calificación {calificacion} es: {feedback}")