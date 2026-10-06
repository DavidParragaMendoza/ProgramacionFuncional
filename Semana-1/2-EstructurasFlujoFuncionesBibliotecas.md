<div align="center">

# 📊 Estructuras de Datos, Flujo, Funciones y NumPy

### Semana 1 · Guía Práctica · Colecciones, Control y Entorno Virtual

[![Semana 1](https://img.shields.io/badge/Semana_1-Inicio-3776AB?style=for-the-badge&logo=readme&logoColor=white)](README.md)
[![Sintaxis y Tipos](https://img.shields.io/badge/Guía_1-Sintaxis_y_Tipos-0078D4?style=for-the-badge)](3-IntroduccionPythonSintaxisTiposBásicos.md)
[![Estructuras y Flujo](https://img.shields.io/badge/Guía_2-Estructuras_y_Flujo-2EA44F?style=for-the-badge)](2-EstructurasFlujoFuncionesBibliotecas.md)
[![Tarea 1](https://img.shields.io/badge/Tarea_1-Ejercicios-8250DF?style=for-the-badge)](Tarea1-EjerciciosconPython2/README.md)

<br>

<img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+">
<img src="https://img.shields.io/badge/NumPy-2.x-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
<img src="https://img.shields.io/badge/Estructuras-List_|_Tuple_|_Dict-2EA44F?style=for-the-badge" alt="Estructuras de datos">

**Guía completa sobre listas, tuplas, diccionarios, flujo de control,**
**modularización mediante funciones y preparación de entornos con NumPy.**

</div>

> [!IMPORTANT]
> Recuerda la regla de inmutabilidad funcional: las **listas** y los **diccionarios** son mutables en Python, mientras que las **tuplas** son inmutables. Elige siempre la estructura según si los datos deben transformarse en copias nuevas o permanecer constantes.

## 🧭 Contenido

- [🎯 Objetivo](#-objetivo)
- [📦 Estructuras de Datos Básicas](#-estructuras-de-datos-básicas)
- [📚 Bibliotecas y Módulos](#-bibliotecas-y-módulos)
- [🔄 Flujo de Control](#-flujo-de-control)
- [🧩 Funciones y Buenas Prácticas](#-funciones-y-buenas-prácticas)
- [🔢 Configuración y Uso de NumPy](#-configuración-y-uso-de-numpy)
- [🧭 Navegación entre Guías](#-navegación-entre-guías)
- [📫 Contacto](#-contacto)

---

## 🎯 Objetivo

Aprender el manejo de colecciones fundamentales en Python (`list`, `tuple`, `dict`), estructurar la lógica mediante bifurcaciones (`if/elif/else`) y bucles (`for`), diseñar funciones puras y reutilizables con tipado estático, y configurar un entorno virtual para trabajar con la biblioteca científica **NumPy**.

---

## 📦 Estructuras de Datos Básicas

- **Listas (`list`)**: Colecciones ordenadas y **mutables** (pueden modificar, añadir o remover sus elementos).
    
  ```python
  planetas: list[str] = ["Mercurio", "Venus", "Tierra"]
  planetas.append("Marte")
  ```
    
- **Tuplas (`tuple`)**: Colecciones ordenadas e **inmutables** (ideales para datos que no deben modificarse, como coordenadas o registros fijos).
    
  ```python
  punto_origen: tuple[int, int, int] = (0, 0, 0)
  ```
    
- **Diccionarios (`dict`)**: Colecciones basadas en pares **clave-valor**, ideales para mapear identidades y atributos.
    
  ```python
  curso: dict[str, any] = {"nombre": "Python", "creditos": 5}
  ```

---

## 📚 Bibliotecas y Módulos

El uso de `import` permite reutilizar código existente de la biblioteca estándar o de terceros:

- **Importar un módulo completo:**
  ```python
  import math  # Biblioteca matemática estándar (pi, sqrt, pow, etc.)
  ```

- **Importar con alias o apodo:**
  ```python
  import numpy as np  # 'np' es el alias canónico para numpy
  ```

- **Traer funciones o clases específicas:**
  ```python
  from os import path  # Módulo específico para rutas del sistema operativo
  ```

---

## 🔄 Flujo de Control

### Condicionales e Indentación
Evaluaciones lógicas con `if`, `elif` y `else`. En Python el alcance de los bloques de código se define por los espacios/sangría y no por llaves `{}`:

```python
temperatura: int = 35

if temperatura > 35:
    print("Es un día caluroso.")
elif temperatura > 20:
    print("El clima es templado.")
else:
    print("Hace frío, ¡a abrigarse!")
```

### Bucles `for`
Utilizados para recorrer elementos de forma secuencial en cualquier colección iterable:

```python
planetas: list[str] = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]

for planeta in planetas:
    print(f"Explorando {planeta}...")
```

---

## 🧩 Funciones y Buenas Prácticas

- **Definición de Funciones:** Se declaran con `def`. Siguiendo las buenas prácticas del curso, especificamos el tipo de los parámetros de entrada y el tipo de retorno con la flecha `->`:
    
  ```python
  def saludar(nombre: str) -> None:
      print(f"¡Hola, {nombre}! Bienvenido/a.")

  saludar("David")
  ```
    
- **Parámetros y Retorno:** Una función recibe datos mediante parámetros y devuelve un nuevo resultado mediante `return`:
    
  ```python
  def calcular_area_rectangulo(base: float, altura: float) -> float:
      area = base * altura
      return area

  area_calculada = calcular_area_rectangulo(10.5, 5.0)
  print(f"El área es: {area_calculada}")
  ```

---

## 🔢 Configuración y Uso de NumPy

NumPy (*Numerical Python*) es la librería fundamental para cálculo científico, vectores y matrices en Python.

### Paso a paso para preparar el entorno:

1. **Abre tu terminal en la carpeta del proyecto:**
   Asegúrate de que PowerShell esté ubicado en la raíz del proyecto.

2. **Crea el entorno virtual (`venv`):**
   ```powershell
   python -m venv venv
   ```

3. **Activa el entorno virtual:**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   > [!TIP]
   > Si PowerShell muestra un error de políticas de ejecución de scripts, ejecuta:
   > ```powershell
   > Set-ExecutionPolicy Unrestricted -Scope CurrentUser
   > ```
   > Pulsa `S` y vuelve a ejecutar el comando de activación.

4. **Instala la biblioteca NumPy:**
   ```powershell
   pip install numpy
   ```

5. **Ejemplo práctico de uso:**
   ```python
   import numpy as np

   # 1. Creamos una lista estándar de Python
   notas: list[int] = [10, 8, 7, 9]

   # 2. La convertimos en un arreglo vectorizado (ndarray)
   notas_np = np.array(notas)

   # 3. Métodos estadísticos optimizados
   media = np.mean(notas_np)        # Promedio
   nota_maxima = np.max(notas_np)   # Valor máximo

   print(f"Notas registradas: {notas_np}")
   print(f"El promedio de notas es: {media}")
   print(f"La nota más alta fue: {nota_maxima}")
   ```

6. **Ejecución y verificación:**
   ```powershell
   python Ejercicio7.py
   ```

   <div align="center">
     <img src="assets/numpy.jpeg" alt="pip install numpy en consola" width="550">
   </div>

---

## 🧭 Navegación entre Guías

<div align="center">

| ⬅️ Anterior | 🏠 Menú Principal | Siguiente ➡️ |
| :---: | :---: | :---: |
| [⬅️ 1. Sintaxis y Tipos Básicos](3-IntroduccionPythonSintaxisTiposBásicos.md) | [🏠 Semana 1 (README)](README.md) | [3. Tarea 1: Ejercicios Prácticos ➡️](Tarea1-EjerciciosconPython2/README.md) |

</div>

---

## 📫 Contacto

- 💼 **LinkedIn:** [David Parraga Mendoza](https://www.linkedin.com/in/davidparragamendoza/)
- 𝕏 **X:** [@DavidParragaMen](https://x.com/DavidParragaMen)

<div align="center">

✨ **Gracias por visitar este proyecto** ✨

</div>