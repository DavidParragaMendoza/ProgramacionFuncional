'''
Ejercicio 5: Calculadora de Estadísticas con NumPy
Importa la biblioteca numpy con el alias np.
Crea una función calcular_estadisticas_np que acepte una lista de números.
Dentro de la función, convierte la lista a un arreglo de NumPy: arreglo = np.array(lista_numeros).
La función debe retornar un diccionario con las siguientes estadísticas, calculadas con funciones de NumPy:
    "media": np.mean(arreglo)
    "mediana": np.median(arreglo)
    "desviacion_estandar": np.std(arreglo)
Llama a la función e imprime el diccionario resultante.
'''

import numpy as np 

def calcularEstadisticasNp(listaNumeros: list[float]) -> dict[str, float]:
    arreglo = np.array(listaNumeros)
    media: float = np.mean(arreglo)
    mediana:float = np.median(arreglo)
    desviacionEstandar: float = np.std(arreglo)

    estadisticas: dict[str, float] = {
        "media": media, 
        "mediana": mediana,
        "desviacion_estandar": desviacionEstandar 
        }
    
    return estadisticas

# Llamamos a la función y guardamos el resultado
listaNumeros: list[float] = [10, 8, 7, 9, 6, 5]

estadisticas: dict[str, float] = calcularEstadisticasNp(listaNumeros)
# Imprimimos el diccionario resultante
print(f"Las estadísticas calculadas para la lista {listaNumeros}: Son las siguientes:")
print(f"Media: {estadisticas['media']}")
print(f"Mediana: {estadisticas['mediana']}")
print(f"Desviación estándar: {estadisticas['desviacion_estandar']}")