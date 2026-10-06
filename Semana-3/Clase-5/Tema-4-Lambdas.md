# **Funciones Anónimas (`lambda`)**

## **¿Qué es una función** **lambda** **?**

Es una función anónima (sin nombre) y concisa, diseñada para operaciones simples y de un solo uso. Se define de forma directa (inline) en la misma línea donde se necesita, evitando la redundancia de crear una función completa con `def` cuando no se volverá a reutilizar.

## **Sintaxis en Python:**

```python
lambda argumentos: expresion
```

- **lambda**: Palabra clave que inicia la expresión.
- **argumentos**: Lista de parámetros de entrada separados por comas.
- **expresion**: Una única instrucción cuyo resultado se evalúa y se **retorna automáticamente** sin necesidad de escribir `return`.

## **Limitación fundamental:**

En Python, el cuerpo de una `lambda` solo puede ser una **única expresión**. No puede contener asignaciones de variables, bucles (`for`, `while`) ni bloques multilìnea estructurados.

## **Criterio de uso (** **def** **vs.** **lambda** **):**

- **Usar** **lambda** **:** Cuando la regla es breve, local, se usará una sola vez y aporta claridad al pasarse como argumento a una HOF (como `map` o `filter`).
- **Usar** **def** **:** Cuando la función involucra una lógica más extensa, requiere reutilización en varias partes del programa o merece un nombre explícito para facilitar la lectura.

---

### Ejercicio 1: Pipeline de Transacciones Bancarias (Filtro y Transformación de Diccionarios)

**Contexto:** Tienes un listado de transacciones bancarias representadas como diccionarios:

```python
transacciones = [
    {"id": 101, "tipo": "ingreso", "monto": 500.0, "aplica_impuesto": True},
    {"id": 102, "tipo": "egreso", "monto": 150.0, "aplica_impuesto": False},
    {"id": 103, "tipo": "ingreso", "monto": 100.0, "aplica_impuesto": True},
    {"id": 104, "tipo": "ingreso", "monto": 350.0, "aplica_impuesto": False},
    {"id": 105, "tipo": "egreso", "monto": 800.0, "aplica_impuesto": True},
    {"id": 106, "tipo": "ingreso", "monto": 250.0, "aplica_impuesto": True},
]
```

**Consigna:** Crea **una sola expresión encadenada** con `map`, `filter` y funciones `lambda`6 que:

1. **Filtre** con `filter`: conserve únicamente las transacciones que sean de tipo `"ingreso"` Y cuyo `monto` sea mayor o igual a `$200.0`.
2. **Transforme** con `map`: aplique un impuesto del  15% (`monto * 0.85`) si `"aplica_impuesto"` es `True`; si es `False`, mantenga el `monto` intacto. 
3. El resultado final debe ser una lista de nuevos diccionarios con la forma: `{"id": 101, "monto_neto": 425.0}`.

### Código:

```python
filtro= list(
    filter(lambda transaccion: transaccion["tipo"]=="ingreso" and transaccion["monto"]>=200.0, transacciones)
)

aplicarImpuesto = list(
    map(lambda t: 
        {"id": t["id"], "monto_neto": t["monto"] * 0.85 if t["aplica_impuesto"] else t["monto"]},filtro)
)

print(aplicarImpuesto)
```

### Ejercicio 2 - Normalización y Evaluación de Estudiantes:

**Contexto:** Tienes una lista de tuplas con estudiantes y sus calificaciones parciales:

```python
estudiantes = [
    ("  juan perez  ", [4, 5, 7, 8]),
    ("ana gomez", [6, 7, 9]),
    (" CARLOS RUIZ ", [4, 5, 10]),
    ("maria lopez", [5, 8]),
]
```

**Consigna:** Utiliza **map y filter anidados con lambda** para:

1. **Filtrar** a los estudiantes cuyo **promedio de notas** sea mayor o igual a `7.5` (calcula el promedio dentro de la `lambda` usando `sum(notas) / len(notas)`).
2. **Transformar** la tupla de los aprobados a un nuevo diccionario con el formato:
    - Nombre limpio: sin espacios extras a los lados (`.strip()`) y en mayúsculas (`.upper()`).
    - Promedio redondeado a 2 decimales (`round(..., 2)`).
    - Estado: `"DESTACADO"` si el promedio es ≥ 9.0 , o `"APROBADO"` de lo contrario (usa un operador ternario `if/else` dentro de la `lambda`).

```python
estudiantes = [
    ("  juan perez  ", [10, 5, 7, 8]),
    ("ana gomez", [10, 7, 9, 10]),
    (" CARLOS RUIZ ", [10, 5, 10, 10]),
    ("maria lopez", [5, 8, 10, 10]),
]

# Aplicamos map y filter anidados
resultado = list(
    map(
        lambda x: {
            "nombre": x[0].strip().upper(),
            "promedio": round(sum(x[1]) / len(x[1]), 2),
            "estado": "DESTACADO" if sum(x[1]) / len(x[1]) >= 9.0 else "APROBADO"
        },
        filter(
            lambda x: sum(x[1]) / len(x[1]) >= 7.0, 
            estudiantes
        )
    )
)

# Imprimir el resultado para verificar
for alumno in resultado:
    print(alumno)
```

---

# **Reducción de Colecciones (`functools.reduce`)**

## **¿Qué es** **reduce** **?**

A diferencia de `map` y `filter` (que devuelven nuevas colecciones), `reduce` es una HOF cuyo objetivo es consumir una colección completa y **producir un único valor acumulado** como una suma, un producto o un valor máximo.

## La Sintaxis General

Para usar reduce en Python, primero debemos importarla desde el módulo functools:

```python
from functools import reduce 
resultado = reduce(funcion_combinadora, iterable, valor_inicial)
```

## Sus 3 componentes principales:

- **`funcion_combinadora:`** Es una función que siempre debe recibir 2 parámetros:
    - **`acumulador:`** Guarda el resultado parcial acumulado hasta el momento.
    - **`elemento_actual:`** Es el valor individual que se está leyendo de la lista en ese turno.
- **`iterable:`** La lista o secuencia de datos que vas a procesar.
- **`valor_inicial`** (opcional pero recomendado): El valor con el que arranca el acumulador antes de leer el primer elemento.

## **Consideración de legibilidad:**

En Python 3, `reduce` se movió al módulo `functools` para promover su uso deliberado, ya que para acumulaciones complejas un bucle `for` tradicional suele resultar más legible. Se recomienda reservar `reduce` para acumulaciones simples y bien conocidas.

---

### **Ejercicio 3: Agrupador Frecuencial / Group By Funcional (Acumulando en un Diccionario)**

**Contexto:** Tienes un historial de ventas registradas por categoría de producto:

```python
ventas_categoria = [
    "electrónica", "ropa", "electrónica", "hogar",
    "ropa", "electrónica", "alimentos", "hogar", "alimentos"
]
```

**Consigna:** Utiliza `functools.reduce` con una expresión `lambda` para construir un **diccionario de frecuencias** que cuente cuántas veces se repite cada categoría:

- **Valor inicial del acumulador:** Un diccionario vacío `{}`.
- **Requisito funcional:** La `lambda` debe tomar el diccionario acumulador y la categoría actual `(acc, cat)`, retornando un nuevo diccionario actualizado con el conteo (puedes usar la sintaxis `{**acc, cat: acc.get(cat, 0) + 1}`).

### Código:

```python
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
```

---

### **🏋️ Ejercicio 4: Aplanado de Matriz 2D con Filtro de Pares (FlatMap Manual con `reduce`)**

**Contexto:** Tienes un conjunto de datos estructurado en una lista de listas (matriz 2D):

```python
matriz = [
    [4, 6, 11, 12],
    [9, 10, 13, 14],
    [3, 5, 15, 16]
]
```

**Consigna:** Usa `reduce` con una `lambda`para **aplanar (flatten)** la matriz a una única lista de una sola dimensión que contenga **únicamente los números pares**:

- **Valor inicial:** Una lista vacía `[].`
- **Operación:** La `lambda` recibe `(acc, sublista)` y debe concatenar al acumulador `acc` solo los números pares encontrados en `sublista` (puedes apoyarte en un `filter` con `lambda` o una lista comprimida dentro de la propia `lambda` del `reduce`).

### Código:

```python
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
```

# Cuestionario:

[Cuestionario](https://notebook.google.com/notebook/57cefa59-c884-40fc-b912-f1ea5619053e/artifact/1fc0a376-d60d-4ccb-87d6-b647c2a06e68?utm_source=nlm_web_share&utm_medium=google_oo&utm_campaign=art_share_1&utm_content=&utm_smc=nlm_web_share_google_oo_art_share_1_)