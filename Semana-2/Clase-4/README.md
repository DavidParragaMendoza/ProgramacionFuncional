# ⚙️ Funciones de orden superior y lambdas

> **Semana 2 · Clase 4**
> Abstracción, transformación y composición de datos con funciones en Python.

## 📌 En esta clase

- Qué son las funciones de orden superior (**HOFs**).
- Cómo reemplazar patrones repetitivos por abstracciones reutilizables.
- Sintaxis y usos apropiados de las funciones `lambda`.
- HOFs nativas: `map`, `filter` y `sorted`.
- Composición de transformaciones mediante pipelines funcionales.

## 🧭 Índice

1. [Funciones de orden superior](#-funciones-de-orden-superior)
2. [Del patrón repetitivo a la abstracción](#-del-patrón-repetitivo-a-la-abstracción)
3. [Funciones anónimas o lambdas](#-funciones-anónimas-o-lambdas)
4. [HOFs nativas de Python](#-hofs-nativas-de-python)
5. [Composición y pipelines funcionales](#-composición-y-pipelines-funcionales)
6. [Ejemplo: ranking de un videojuego](#-ejemplo-ranking-de-un-videojuego)

---

## 🧠 Funciones de orden superior

Una **función de orden superior** (*Higher-Order Function* o **HOF**) cumple al
menos una de estas condiciones:

1. Recibe otra función como argumento.
2. Devuelve una función como resultado.

Su objetivo es separar:

- **La estructura común:** por ejemplo, recorrer una lista.
- **El comportamiento específico:** qué transformación aplicar a cada elemento.

Esta separación permite escribir funciones más reutilizables, expresivas y
fáciles de mantener.

## 🔁 Del patrón repetitivo a la abstracción

### El problema imperativo

Funciones como `duplicar(lista)` y `elevar_al_cuadrado(lista)` suelen repetir
la misma estructura:

1. Crear una lista vacía.
2. Recorrer los elementos con `for`.
3. Transformar cada elemento.
4. Agregar el resultado con `.append()`.
5. Retornar la lista.

Solo cambia la operación aplicada, pero el recorrido se vuelve a escribir.

### La solución funcional

Creamos una sola función que recibe la transformación:

```python
def transformar_lista(transformacion, lista):
    return [transformacion(elemento) for elemento in lista]
```

La infraestructura común vive en `transformar_lista`; la operación concreta se
inyecta mediante el parámetro `transformacion`.

```python
numeros = [1, 2, 3, 4]

duplicados = transformar_lista(lambda x: x * 2, numeros)
cuadrados = transformar_lista(lambda x: x ** 2, numeros)

print(duplicados)  # [2, 4, 6, 8]
print(cuadrados)   # [1, 4, 9, 16]
```

## ✨ Funciones anónimas o lambdas

Una **lambda** es una función pequeña, anónima y de una sola expresión. Se
define directamente en el lugar donde se necesita, sin declarar una función
formal con `def`.

### Sintaxis

```python
lambda parametros: expresion
```

| Parte | Función |
| --- | --- |
| `lambda` | Indica que se está creando una función anónima. |
| `parametros` | Valores de entrada, como `x` o `a, b`. |
| `:` | Separa los parámetros de la lógica. |
| `expresion` | Operación que se evalúa y retorna automáticamente. |

Ejemplos:

```python
duplicar = lambda x: x * 2
sumar = lambda a, b: a + b

print(duplicar(5))  # 10
print(sumar(2, 3))  # 5
```

> **Buena práctica:** utiliza lambdas para operaciones breves y claras. Si la
> lógica necesita varias líneas o una explicación, prefiere `def`.

## 🧰 HOFs nativas de Python

### `map`: transformar cada elemento

Aplica una función a todos los elementos de un iterable:

```python
numeros = [1, 2, 3]
dobles = list(map(lambda x: x * 2, numeros))

print(dobles)  # [2, 4, 6]
```

### `filter`: conservar los elementos válidos

Evalúa una condición booleana y conserva solo los elementos para los que
devuelve `True`:

```python
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares)  # [2, 4, 6]
```

### `sorted`: ordenar usando una clave

Ordena una colección a partir de una función que extrae la propiedad usada
como criterio:

```python
jugadores = [
    {"nombre": "Ana", "puntos": 120},
    {"nombre": "Luis", "puntos": 180},
]

ranking = sorted(jugadores, key=lambda jugador: jugador["puntos"], reverse=True)
```

- `key` indica qué valor se utilizará para ordenar.
- `reverse=True` ordena de mayor a menor.

## 🔗 Composición y pipelines funcionales

Las HOFs pueden encadenarse para expresar una transformación completa de datos.
En la siguiente expresión:

```python
resultado = list(
    map(transformar, filter(validar, datos))
)
```

la evaluación ocurre de adentro hacia afuera:

1. `filter` conserva los elementos que cumplen `validar`.
2. `map` transforma los elementos restantes.
3. `list` materializa el resultado.

Este estilo permite describir el flujo de datos sin administrar manualmente
listas temporales ni índices.

## 🎮 Ejemplo: ranking de un videojuego

Construyamos un ranking con tres pasos:

1. Filtrar a los jugadores conectados.
2. Calcular su poder real (`puntos * nivel`).
3. Ordenarlos de forma descendente.

```python
jugadores = [
    {"nombre": "Ana", "conectado": True, "puntos": 120, "nivel": 3},
    {"nombre": "Luis", "conectado": False, "puntos": 200, "nivel": 4},
    {"nombre": "Marta", "conectado": True, "puntos": 150, "nivel": 2},
]

conectados = filter(
    lambda jugador: jugador["conectado"],
    jugadores,
)

ranking = sorted(
    map(
        lambda jugador: {
            **jugador,
            "poder": jugador["puntos"] * jugador["nivel"],
        },
        conectados,
    ),
    key=lambda jugador: jugador["poder"],
    reverse=True,
)

for posicion, jugador in enumerate(ranking, start=1):
    print(posicion, jugador["nombre"], jugador["poder"])
```

## ✅ Resumen

- Una HOF recibe funciones o devuelve funciones.
- La abstracción evita repetir la estructura de un proceso.
- `lambda` resulta útil para transformaciones pequeñas.
- `map` transforma, `filter` selecciona y `sorted` ordena.
- La composición permite construir pipelines de datos claros y reutilizables.

> **En una frase:** las funciones de orden superior permiten reutilizar el
> proceso y cambiar únicamente el comportamiento que se aplica a los datos.
