'''
Ejercicio 2: Calculadora de Área de Círculo
Importa la biblioteca math.

Crea una función llamada calcular_area_circulo que acepte un parámetro radio (float).

Dentro de la función, usa math.pi y la fórmula del área (π * r²) para calcular el área.

La función debe retornar el área calculada.

Llama a la función, guarda el resultado en una variable e imprímelo.
'''

import math

def calcularAreaCirculo(radio: float) -> float:
    areaCiruculo: float = math.pi * (radio **2)
    return areaCiruculo


# Llamamos a la función y guardamos el resultado
radio: float = float(input("Ingrese el radio del circulo: "))
area: float = calcularAreaCirculo(radio)
# Imprimimos el resultado
print(f"El área del círculo con radio {radio} es: {area}")