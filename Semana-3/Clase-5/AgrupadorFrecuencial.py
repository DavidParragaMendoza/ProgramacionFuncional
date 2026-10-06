'''
Ejercicio 3: Agrupador Frecuencial / Group By Funcional (Acumulando en un Diccionario)
Contexto: Tienes un historial de ventas registradas por categoría de producto:

ventas_categoria = [
    "electrónica", "ropa", "electrónica", "hogar",
    "ropa", "electrónica", "alimentos", "hogar", "alimentos"
]

Consigna: Utiliza `functools.reduce` con una expresión `lambda` para construir un diccionario de frecuencias que cuente cuántas veces se repite cada categoría:

- Valor inicial del acumulador: Un diccionario vacío `{}`.
- Requisito funcional: La `lambda` debe tomar el diccionario acumulador y la categoría actual `(acc, cat)`, retornando un nuevo diccionario actualizado con el conteo 

(puedes usar la sintaxis `{**acc, cat: acc.get(cat, 0) + 1}`).

'''

from functools import reduce

ventas_categoria = [
    "electrónica", "ropa", "electrónica", "hogar",
    "ropa", "electrónica", "alimentos", "hogar", "alimentos"
]

numeroCategorias = reduce(
    #La función
    lambda acc, cat: {**acc, cat: acc.get(cat, 0) + 1},
    #El elemento a iterar:
    ventas_categoria,
    #El valor inicial:
    {}
)

print(numeroCategorias)