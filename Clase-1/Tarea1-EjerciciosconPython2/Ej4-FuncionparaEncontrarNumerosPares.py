'''
Ejercicio 4: Función para Encontrar Números Pares
Crea una función encontrar_pares(lista_numeros: list[int]) que retorne una nueva lista solo con los números pares de la original.

Llama a la función e imprime la nueva lista.
'''

def encontrarPares(listaNumeros: list[int]) -> list[int]:
    numerosPares: list[int] =[]
    for numero in listaNumeros:
        if numero % 2 == 0:
            numerosPares.append(numero)
    return numerosPares


listanumeros: list[int] = [1,2,3,4,5,6,7,8,9,10]

# Llamamos a la función y guardamos el resultado
numerosPares: list[int] = encontrarPares(listanumeros)  

print(f"Los números pares de la lista {listanumeros} son: {numerosPares}")