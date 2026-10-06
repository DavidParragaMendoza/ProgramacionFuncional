'''
Ejercicio 4: Aplanado de Matriz 2D con Filtro de Pares (FlatMap Manual con `reduce`)
Contexto: Tienes un conjunto de datos estructurado en una lista de listas (matriz 2D):

matriz = [
    [4, 6, 11, 12],
    [9, 10, 13, 14],
    [3, 5, 15, 16]
]

Consigna: Usa `reduce` con una `lambda` para aplanar (flatten) la matriz a una única lista de una sola dimensión que contenga **únicamente los números pares:

- Valor inicial: Una lista vacía `[]`.
- Operación: La `lambda` recibe `(acc, sublista)` y debe concatenar al acumulador `acc` solo los números pares encontrados en `sublista` (puedes apoyarte en un `filter` con `lambda` o una lista comprimida dentro de la propia `lambda` del `reduce`).
'''
from functools import reduce

matriz = [
    [4, 6,  11,  12],
    [9, 10, 13,  14],
    [3, 5,  15,  16]
]

numerosPares = reduce(
    #función que aplanará la matriz y filtrará los números pares
    lambda acc, sublista: acc + list(filter(lambda x: x % 2 == 0, sublista)),
    #la matriz a iterar
    matriz,
    #valor inicial del acumulador
    []
)

print(numerosPares)