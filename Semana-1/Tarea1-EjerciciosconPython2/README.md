<div align="center">

# 🧪 Tarea 1 · Ejercicios Prácticos con Python

### Programación Funcional · Semana 1 · Fundamentos, Funciones y NumPy

[![Semana 1](https://img.shields.io/badge/Semana_1-Inicio-3776AB?style=for-the-badge&logo=readme&logoColor=white)](../README.md)
[![Sintaxis y Tipos](https://img.shields.io/badge/Guía_1-Sintaxis_y_Tipos-0078D4?style=for-the-badge)](../3-IntroduccionPythonSintaxisTiposBásicos.md)
[![Estructuras y Flujo](https://img.shields.io/badge/Guía_2-Estructuras_y_Flujo-2EA44F?style=for-the-badge)](../2-EstructurasFlujoFuncionesBibliotecas.md)
[![Tarea 1](https://img.shields.io/badge/Tarea_1-Ejercicios-8250DF?style=for-the-badge)](README.md)

<br>

<img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+">
<img src="https://img.shields.io/badge/Ejercicios-5-2EA44F?style=for-the-badge" alt="5 ejercicios">
<img src="https://img.shields.io/badge/Librería-NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">

**Colección de ejercicios prácticos para afianzar el uso de funciones con Type Hints,**
**estructuras de control condicional, filtrado de listas y cálculo estadístico con NumPy.**

</div>

> [!IMPORTANT]
> Cada ejercicio está resuelto en su propio script `.py` individual con tipado estático (`Type Hints`), entrada/salida de datos y pruebas de consola.

## 🧭 Contenido

- [🎯 Objetivo](#-objetivo)
- [🗂️ Lista de Ejercicios](#️-lista-de-ejercicios)
- [🧠 Detalle y Explicación de los Ejercicios](#-detalle-y-explicación-de-los-ejercicios)
  - [1. Saludo Personalizado](#1-saludo-personalizado)
  - [2. Calculadora de Área de Círculo](#2-calculadora-de-área-de-círculo)
  - [3. Verificador de Calificaciones](#3-verificador-de-calificaciones)
  - [4. Filtrado de Números Pares](#4-filtrado-de-números-pares)
  - [5. Calculadora de Estadísticas con NumPy](#5-calculadora-de-estadísticas-con-numpy)
- [🚀 Cómo Ejecutar los Ejercicios](#-cómo-ejecutar-los-ejercicios)
- [🧭 Navegación entre Guías](#-navegación-entre-guías)
- [📫 Contacto](#-contacto)

---

## 🎯 Objetivo

Poner en práctica las bases de la programación en Python aprendidas durante la Semana 1, priorizando la creación de funciones puras o modulares, la anotación de tipos explícita, la inmutabilidad de datos de entrada y el aprovechamiento de bibliotecas estándar (`math`) y especializadas (`numpy`).

---


## 🧠 Detalle y Explicación de los Ejercicios

### 1. Saludo Personalizado
📁 **Archivo:** [`Ej1-FunciónSaludoPersonalizado.py`](Ej1-FunciónSaludoPersonalizado.py)

Define una función que toma nombre y apellido y genera una bienvenida formateada:

```python
def saludoPersonalizado(nombre: str, apellido: str):
    print(f"Hola, {nombre} {apellido} Bienvenido a Programacion Funcional con Python.")

saludoPersonalizado("Ronald", "Parraga")
saludoPersonalizado("David", "Mendoza")
```

<details>
<summary>💡 Ver explicación del ejercicio</summary>

Demuestra la definición básica de funciones con múltiples argumentos de tipo `str` y el uso de plantillas literales con `f-strings` para componer cadenas de texto limpias.

</details>

---

### 2. Calculadora de Área de Círculo
📁 **Archivo:** [`Ej2-CalculadoraAreaCirculo.py`](Ej2-CalculadoraAreaCirculo.py)

Importa la biblioteca `math` y aplica la fórmula $A = \pi \cdot r^2$:

```python
import math

def calcularAreaCirculo(radio: float) -> float:
    areaCiruculo: float = math.pi * (radio ** 2)
    return areaCiruculo

radio: float = float(input("Ingrese el radio del circulo: "))
area: float = calcularAreaCirculo(radio)
print(f"El área del círculo con radio {radio} es: {area}")
```

<details>
<summary>💡 Ver explicación del ejercicio</summary>

Muestra cómo una función pura recibe un valor numérico flotante, realiza el cómputo apoyándose en la constante matemática de alta precisión `math.pi`, y devuelve un valor resultante con `return` sin alterar variables globales.

</details>

---

### 3. Verificador de Calificaciones
📁 **Archivo:** [`Ej3-RefactorizandoVerificadorCalificaciones.py`](Ej3-RefactorizandoVerificadorCalificaciones.py)

Refactoriza una verificación tradicional en una función de evaluación cualitativa:

```python
def obtenerFeedbackCalificacion(calificacion: float) -> str:
    if calificacion >= 9:
        return "Sobresaliente"
    elif calificacion >= 8:
        return "Notable"
    elif calificacion >= 7:
        return "Bien"
    else:
        return "Insuficiente"

calificacion: float = float(input("Ingrese la calificación: "))
feedback: str = obtenerFeedbackCalificacion(calificacion)
print(f"El feedback para la calificación {calificacion} es: {feedback}")
```

<details>
<summary>💡 Ver explicación del ejercicio</summary>

Ilustra la técnica de retorno temprano (*early return*) con bloques condicionales anidados, categorizando de forma unívoca el rango numérico en una etiqueta textual descriptiva.

</details>

---

### 4. Filtrado de Números Pares
📁 **Archivo:** [`Ej4-FuncionparaEncontrarNumerosPares.py`](Ej4-FuncionparaEncontrarNumerosPares.py)

Filtra elementos pares sin modificar la lista original suministrada:

```python
def encontrarPares(listaNumeros: list[int]) -> list[int]:
    numerosPares: list[int] = []
    for numero in listaNumeros:
        if numero % 2 == 0:
            numerosPares.append(numero)
    return numerosPares

listanumeros: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numerosPares: list[int] = encontrarPares(listanumeros)
print(f"Los números pares de la lista {listanumeros} son: {numerosPares}")
```

<details>
<summary>💡 Ver explicación del ejercicio</summary>

Aplica el concepto fundamental de preservación de inmutabilidad: la lista original `listanumeros` permanece intacta, mientras que la función construye y devuelve una nueva lista independiente con los elementos seleccionados mediante el predicado aritmético `% 2 == 0`.

</details>

---

### 5. Calculadora de Estadísticas con NumPy
📁 **Archivo:** [`Ej5-CalculadoraEstadísticasNumPy.py`](Ej5-CalculadoraEstadísticasNumPy.py)

Aprovecha el poder computacional de arreglos `numpy.ndarray` para devolver un resumen estadístico:

```python
import numpy as np 

def calcularEstadisticasNp(listaNumeros: list[float]) -> dict[str, float]:
    arreglo = np.array(listaNumeros)
    media: float = np.mean(arreglo)
    mediana: float = np.median(arreglo)
    desviacionEstandar: float = np.std(arreglo)

    estadisticas: dict[str, float] = {
        "media": media, 
        "mediana": mediana,
        "desviacion_estandar": desviacionEstandar 
    }
    return estadisticas

listaNumeros: list[float] = [10, 8, 7, 9, 6, 5]
estadisticas = calcularEstadisticasNp(listaNumeros)
print(f"Media: {estadisticas['media']}")
print(f"Mediana: {estadisticas['mediana']}")
print(f"Desviación estándar: {estadisticas['desviacion_estandar']}")
```

<details>
<summary>💡 Ver explicación del ejercicio</summary>

Demuestra la integración con librerías científicas externas. Transforma una lista estándar en un arreglo NumPy para invocar funciones vectorizadas optimizadas (`np.mean`, `np.median`, `np.std`) y empaqueta las métricas calculadas en un diccionario estructurado clave-valor.

</details>

---

## 🚀 Cómo Ejecutar los Ejercicios

1. **Asegúrate de tener el entorno virtual activado con NumPy:**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

2. **Ejecuta el script que desees probar:**
   ```powershell
   python .\Semana-1\Tarea1-EjerciciosconPython2\Ej1-FunciónSaludoPersonalizado.py
   python .\Semana-1\Tarea1-EjerciciosconPython2\Ej2-CalculadoraAreaCirculo.py
   python .\Semana-1\Tarea1-EjerciciosconPython2\Ej3-RefactorizandoVerificadorCalificaciones.py
   python .\Semana-1\Tarea1-EjerciciosconPython2\Ej4-FuncionparaEncontrarNumerosPares.py
   python .\Semana-1\Tarea1-EjerciciosconPython2\Ej5-CalculadoraEstadísticasNumPy.py
   ```

---

## 🧭 Navegación entre Guías

<div align="center">

| ⬅️ Anterior | 🏠 Menú Principal | 📘 Guía de Sintaxis |
| :---: | :---: | :---: |
| [⬅️ 2. Estructuras, Flujo y NumPy](../2-EstructurasFlujoFuncionesBibliotecas.md) | [🏠 Semana 1 (README)](../README.md) | [1. Sintaxis Básica ➡️](../3-IntroduccionPythonSintaxisTiposBásicos.md) |

</div>

---

## 📫 Contacto

- 💼 **LinkedIn:** [David Parraga Mendoza](https://www.linkedin.com/in/davidparragamendoza/)
- 𝕏 **X:** [@DavidParragaMen](https://x.com/DavidParragaMen)

<div align="center">

✨ **Gracias por visitar este proyecto** ✨

</div>
