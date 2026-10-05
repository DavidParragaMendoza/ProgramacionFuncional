'''
8. Reimplementando filter
Escribe la función filtrar(lista, condicion) que reciba una lista y una función condición, retornando una nueva lista con los elementos conformes. No uses la función nativa filter.

✔ Salida esperada: filtrar([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0) → [2, 4, 6]
💡 Pista: Aquí sí puedes usar for interno: el bucle queda aislado dentro de la abstracción de la HOF.

'''

def filtrar(lista, condicion) -> list:
    resultado = []
    for numero in lista:
        if condicion(numero):
            resultado.append(numero)
    return resultado

#numeros pares
print(filtrar([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0))
#numeros impares
print(filtrar([1, 2, 3, 4, 5, 6], lambda x: x % 2 != 0))
#numeros mayores a 3
print(filtrar([1, 2, 3, 4, 5, 6], lambda x: x > 3))
