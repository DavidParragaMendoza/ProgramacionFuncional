<div align="center">

# 🚀 Introducción a la Programación Funcional

### Semana 1 · Del "Cómo" al "Qué" · Paradigma Declarativo

[![Semana 1](https://img.shields.io/badge/Semana_1-Inicio-3776AB?style=for-the-badge&logo=readme&logoColor=white)](README.md)
[![Sintaxis y Tipos](https://img.shields.io/badge/Guía_1-Sintaxis_y_Tipos-0078D4?style=for-the-badge)](3-IntroduccionPythonSintaxisTiposBásicos.md)
[![Estructuras y Flujo](https://img.shields.io/badge/Guía_2-Estructuras_y_Flujo-2EA44F?style=for-the-badge)](2-EstructurasFlujoFuncionesBibliotecas.md)
[![Tarea 1](https://img.shields.io/badge/Tarea_1-Ejercicios-8250DF?style=for-the-badge)](Tarea1-EjerciciosconPython2/README.md)

<br>

<img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+">
<img src="https://img.shields.io/badge/Paradigma-Declarativo-2EA44F?style=for-the-badge" alt="Paradigma Declarativo">
<img src="https://img.shields.io/badge/Pilares-3-8250DF?style=for-the-badge" alt="3 Pilares">

**Del "Cómo" al "Qué": Fundamentos conceptuales, cambio de paradigma**
**y principios clave de la programación funcional en Python.**

</div>

> [!IMPORTANT]
> La transición principal consiste en dejar de pensar en los **pasos e instrucciones manuales** (enfoque imperativo) y comenzar a enfocarse en las **transformaciones de datos** (enfoque declarativo).

## 🧭 Contenido

- [🎯 Objetivo](#-objetivo)
- [🔄 1. El Cambio de Paradigma: Imperativo vs. Declarativo](#-1-el-cambio-de-paradigma-imperativo-vs-declarativo)
- [🏛️ 2. Los 3 Pilares de la Programación Funcional (PF)](#️-2-los-3-pilares-de-la-programación-funcional-pf)
  - [A) Funciones Puras 🧪](#a-funciones-puras-)
  - [B) Inmutabilidad 🧱](#b-inmutabilidad-)
  - [C) Transparencia Referencial 🔍](#c-transparencia-referencial-)
- [⚡ 3. ¿Por qué importa esto hoy?](#-3-por-qué-importa-esto-hoy)
- [📂 Material complementario de la semana](#-material-complementario-de-la-semana)
- [🧭 Navegación entre Guías](#-navegación-entre-guías)
- [📫 Contacto](#-contacto)

---

## 🎯 Objetivo

Comprender las bases teóricas y prácticas de la programación funcional frente al enfoque tradicional imperativo, estableciendo a **Python** como lenguaje principal y a **Java** como puente conceptual para analizar el manejo de estado, mutabilidad y paralelismo seguro.

---

## 🔄 1. El Cambio de Paradigma: Imperativo vs. Declarativo

La forma en que pensamos al programar define el paradigma. La transición principal aquí es dejar de pensar en los **pasos manuales** y empezar a enfocarnos en las **transformaciones de datos**.

| Característica | 🛠️ Enfoque Imperativo (El "Cómo") | 🎯 Enfoque Declarativo / Funcional (El "Qué") |
| :--- | :--- | :--- |
| **Foco** | Detallar paso a paso las instrucciones. | Describir el resultado esperado o el destino. |
| **Control** | Explícito (bucles `for`, `while`, condicionales `if`). | Implícito (el lenguaje maneja los detalles). |
| **Estado** | Mutable (las variables cambian de valor constantemente). | Inmutable (se crean nuevos datos, menos mutación). |
| **Analogía** | Dar direcciones exactas de cada cuadra para llegar a un lugar. | Dar la dirección final y dejar que el GPS encuentre la ruta. |

---

## 🏛️ 2. Los 3 Pilares de la Programación Funcional (PF)

Para que el código declarativo sea seguro y predecible, se basa en tres reglas de oro:

### A) Funciones Puras 🧪

Son como recetas matemáticas exactas. Cumplen dos reglas estrictas:
1. **Mismos inputs = Mismo output:** Siempre devuelven lo mismo si les pasas los mismos argumentos.
2. **Cero Efectos Secundarios (Side Effects):** No modifican nada fuera de su propio ámbito (no alteran variables globales, no escriben archivos, etc.).

```python
# ✅ FUNCIÓN PURA: Predecible y aislada
def sumar(a, b):
    return a + b

# ❌ FUNCIÓN IMPURA: Depende de un estado externo
descuento_global = 0.10
def calcular_precio(precio):
    return precio * (1 - descuento_global)
```

### B) Inmutabilidad 🧱

Una vez creado un dato, **NO** se puede cambiar. Si necesitas modificarlo, creas una *copia* con el nuevo valor.
* **Python:** Listas (Mutables) vs. Tuplas (Inmutables).
* **Java:** `String` (Inmutable) vs. `StringBuilder` (Mutable).

```python
mi_tupla = (1, 2, 3)
# mi_tupla.append(4) -> ERROR 🚫
nueva_tupla = mi_tupla + (4,) # ✅ Correcto: Se crea una nueva
```

### C) Transparencia Referencial 🔍

Gracias a las funciones puras, puedes reemplazar cualquier llamada a una función por su resultado sin que el programa se rompa.

> [!TIP]
> **Ejemplo:** Si `sumar(2, 3)` siempre resulta en `5`, puedes reemplazar directamente esa llamada por `5` en cualquier parte de tu código y nada fallará. Esto hace que el código sea predecible y muy fácil de optimizar o probar.

---

## ⚡ 3. ¿Por qué importa esto hoy?

Antes, los procesadores solo se hacían más rápidos en un único núcleo. Hoy, la evolución del hardware se basa en tener **múltiples núcleos (multi-core)**.

* **El problema imperativo:** Muchos hilos de ejecución intentando modificar la misma variable causan *race conditions* (condiciones de carrera) y requieren bloqueos (*locks*) complejos y propensos a errores.
* **La solución funcional:** Si los datos son **inmutables** y las funciones son **puras**, no hay estado compartido que bloquear ni sincronizar. ¡El procesamiento concurrente y en paralelo es seguro y nativo!

---


## 🧭 Navegación entre Guías

<div align="center">

| 🏠 Inicio | 📘 Guía 1: Sintaxis y Tipos | 📗 Guía 2: Estructuras y Flujo | 🧪 Tarea 1: Práctica |
| :---: | :---: | :---: | :---: |
| [Semana 1](README.md) | [1. Sintaxis Básica](3-IntroduccionPythonSintaxisTiposBásicos.md) | [2. Estructuras & NumPy](2-EstructurasFlujoFuncionesBibliotecas.md) | [Tarea 1](Tarea1-EjerciciosconPython2/README.md) |

</div>

---

## 📫 Contacto

- 💼 **LinkedIn:** [David Parraga Mendoza](https://www.linkedin.com/in/davidparragamendoza/)
- 𝕏 **X:** [@DavidParragaMen](https://x.com/DavidParragaMen)

<div align="center">

✨ **Gracias por visitar este proyecto** ✨

</div>
