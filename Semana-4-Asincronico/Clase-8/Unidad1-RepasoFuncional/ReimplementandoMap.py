'''
### Ejercicio 1: Nivel Calentamiento (Reimplementando map)

**Consigna:** 

Escribe tu propia HOF llamada transformar_coleccion(funcion_transformadora, lista) que reciba una función y una lista, y devuelva una nueva lista con los resultados de aplicar la función a cada elemento (sin usar map de Python ni mutar la lista original).

Prueba tu código con:

- Una función triplicar(n) que multiplique un número por 3.
- Una función enmarcar(texto) que devuelva f"[{texto}]".

''' 

def triplicar(n: int) -> int:
    return n * 3

def enmarcar(texto: str) -> str:
    return f"[{texto}]"

def trasformarColeccion(funcion, lista) -> list:
    resultado = []
    for valor in lista:
        resultado.append(funcion(valor))
    return resultado

print(trasformarColeccion(triplicar, [1, 2, 3, 4, 5]))
print(trasformarColeccion(enmarcar, ["Hola", "Mundo", "Python"]))








'''
implementando map al ejercicio.

triplicar: list[int] = list(
    map(lambda valor: valor * 3, [1, 2, 3, 4, 5])
)
print(triplicar)

enmarcar: list[str] = list(
    map(lambda texto: f"[{texto}]", ["Hola", "Mundo", "Python"])
)
print(enmarcar)
'''