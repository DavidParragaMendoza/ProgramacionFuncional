<div align="center">

# 🧪 Tarea Formativa · Ejercicios de Práctica con HOFs y Lambdas

### Programación Funcional · Semana 2 · Abstracción, Transformación y Pipelines

[![Semana 2](https://img.shields.io/badge/Semana_2-Inicio-3776AB?style=for-the-badge&logo=readme&logoColor=white)](../README.md)
[![Clase 3](https://img.shields.io/badge/Clase_3-Pattern_Matching-0078D4?style=for-the-badge)](../Clase-3/README.md)
[![Clase 4](https://img.shields.io/badge/Clase_4-HOFs_&_Lambdas-2EA44F?style=for-the-badge)](../Clase-4/README.md)
[![Tarea Formativa](https://img.shields.io/badge/Tarea_Formativa-Ejercicios-8250DF?style=for-the-badge)](README.md)

<br>

<img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+">
<img src="https://img.shields.io/badge/Ejercicios-10-2EA44F?style=for-the-badge" alt="10 ejercicios">
<img src="https://img.shields.io/badge/Enfoque-HOFs_%26_Pipelines-8250DF?style=for-the-badge" alt="HOFs y Pipelines">

**Taller práctico para consolidar la transición del pensamiento imperativo**
**al declarativo mediante funciones anónimas, HOFs nativas y composición.**

</div>

> [!IMPORTANT]
> Esta tarea formativa está compuesta por 10 mini-programas diseñados en dificultad progresiva: desde la reescritura de funciones tradicionales a `lambda`, hasta el diseño de pipelines completos para colecciones estructuradas y la reimplementación de HOFs artesanales.

## 🧭 Contenido

- [🎯 Resumen de la Tarea](#-resumen-de-la-tarea)
- [🗂️ Ejes Temáticos Evaluados](#️-ejes-temáticos-evaluados)
- [📋 Lista General de Ejercicios](#-lista-general-de-ejercicios)
- [🚀 Cómo Ejecutar los Ejercicios](#-cómo-ejecutar-los-ejercicios)
- [🧭 Navegación entre Clases](#-navegación-entre-clases)
- [📫 Contacto](#-contacto)

---

## 🎯 Resumen de la Tarea

El propósito de esta práctica es dominar el uso de funciones de orden superior (**HOFs**) y funciones anónimas (**`lambda`**) en Python para procesar datos de forma puramente declarativa.

A través de estos ejercicios se trabaja con:
1. **Transición sintáctica:** Reemplazar funciones `def` pequeñas por expresiones anónimas directas.
2. **Procesamiento de datos con HOFs estándar:** Emplear `map`, `filter` y `sorted` para transformar, filtrar y ordenar colecciones sin bucles `for` manuales.
3. **Composición de pipelines funcionales:** Conectar operaciones en cadena (`filter` ➔ `map` ➔ `sorted`) para resolver problemas de lógica de negocio en una única expresión declarativa.
4. **Diseño de HOFs personalizadas:** Construir funciones capaces de recibir o devolver otras funciones, abstrayendo bucles y condiciones (incluyendo la reimplementación desde cero del comportamiento de `filter`).
5. **Procesamiento de estructuras complejas:** Manejo de listas de diccionarios, cálculo de estadísticas embebidas y ordenamiento multinivel con tuplas de clave.

---

## 🗂️ Ejes Temáticos Evaluados

| Eje Temático | Conceptos Aplicados |
| :--- | :--- |
| 🟢 **Fundamentos de Lambdas** | Creación de funciones anónimas en una sola línea sin `return` explícito. |
| 🟠 **HOFs Nativas** | Filtrado con predicados booleanos (`filter`), transformación masiva (`map`) y ordenamiento con clave personalizada (`sorted`). |
| 🔵 **Pipelines de Transformación** | Encadenamiento de operaciones de adentro hacia afuera sobre listas de números y diccionarios reales. |
| 🟣 **Abstracción y Arquitectura** | Creación de funciones de orden superior propias y desacoplamiento de la lógica de negocio. |

---

## 📋 Lista General de Ejercicios

Los 10 scripts independientes que conforman la tarea son:

- [`Ej1-AgregarIvaLambda.py`](Ej1-AgregarIvaLambda.py) — Calentamiento: migración de función tradicional a expresión `lambda` con `map`.
- [`Ej2-Transformacion.py`](Ej2-Transformacion.py) — Transformación de cadenas y colecciones mediante funciones anónimas.
- [`Ej3-MayorDeEdad.py`](Ej3-MayorDeEdad.py) — Filtrado condicional basado en predicados booleanos.
- [`Ej4-OrdenamientoConKey.py`](Ej4-OrdenamientoConKey.py) — Ordenación de colecciones especificando funciones `key` con lambda.
- [`Ej5-Pipeline.py`](Ej5-Pipeline.py) — Pipeline funcional encadenado: filtrado, bonificación y ordenamiento descendente.
- [`Ej6-DiccionariosPipelinesReales.py`](Ej6-DiccionariosPipelinesReales.py) — Procesamiento de datos tabulares y colecciones de diccionarios.
- [`Ej7-HOF.py`](Ej7-HOF.py) — Definición de una función de orden superior personalizada que inyecta comportamiento.
- [`Ej8-ReimplementandoFilter.py`](Ej8-ReimplementandoFilter.py) — Reconstrucción artesanal de la abstracción de `filter` sin usar la función nativa.
- [`Ej9-HOFLogicaNegocio.py`](Ej9-HOFLogicaNegocio.py) — Desacoplamiento de reglas de negocio dinámicas mediante HOFs.
- [`Ej10-GenerarReportes.py`](Ej10-GenerarReportes.py) — Reto integrador backend: filtrado activo, promedios, ordenamiento con desempate y búsqueda óptima con `max()`.

---

## 🚀 Cómo Ejecutar los Ejercicios

Todos los archivos son autónomos y muestran sus resultados mediante `print()` en la consola:

```powershell
python .\Semana-2\Tarea-FormativaEjerciciosPractica\Ej1-AgregarIvaLambda.py
python .\Semana-2\Tarea-FormativaEjerciciosPractica\Ej5-Pipeline.py
python .\Semana-2\Tarea-FormativaEjerciciosPractica\Ej10-GenerarReportes.py
```

---

## 🧭 Navegación entre Clases

<div align="center">

| ⬅️ Anterior | 🏠 Menú de Semana 2 | 📘 Ir a Pattern Matching |
| :---: | :---: | :---: |
| [⬅️ Clase 4: HOFs y Lambdas](../Clase-4/README.md) | [🏠 Semana 2 (README)](../README.md) | [Clase 3: Pattern Matching ➡️](../Clase-3/README.md) |

</div>

---

## 📫 Contacto

- 💼 **LinkedIn:** [David Parraga Mendoza](https://www.linkedin.com/in/davidparragamendoza/)
- 𝕏 **X:** [@DavidParragaMen](https://x.com/DavidParragaMen)

<div align="center">

✨ **Gracias por visitar este proyecto** ✨

</div>
