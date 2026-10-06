<div align="center">

# ⚡ Semana 2 · Modelado Seguro y Abstracción Funcional

### Programación Funcional · Pattern Matching · HOFs · Lambdas · Pipelines

[![Semana 2](https://img.shields.io/badge/Semana_2-Inicio-3776AB?style=for-the-badge&logo=readme&logoColor=white)](README.md)
[![Clase 3](https://img.shields.io/badge/Clase_3-Pattern_Matching-0078D4?style=for-the-badge)](Clase-3/README.md)
[![Clase 4](https://img.shields.io/badge/Clase_4-HOFs_&_Lambdas-2EA44F?style=for-the-badge)](Clase-4/README.md)
[![Tarea Formativa](https://img.shields.io/badge/Tarea_Formativa-Ejercicios-8250DF?style=for-the-badge)](Tarea-FormativaEjerciciosPractica/README.md)

<br>

<img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+">
<img src="https://img.shields.io/badge/Clases-2-2EA44F?style=for-the-badge" alt="2 Clases">
<img src="https://img.shields.io/badge/Práctica-10_Ejercicios-8250DF?style=for-the-badge" alt="10 Ejercicios">

**Explora el diseño de datos robustos sin estados inválidos mediante Pattern Matching,**
**y la composición de pipelines expresivos con Funciones de Orden Superior y Lambdas.**

</div>

> [!IMPORTANT]
> Durante esta semana se profundiza en dos pilares del paradigma funcional: modelar estructuras algebraicas seguras (haciendo lo ilegal irrepresentable) y separar la infraestructura de iteración de la lógica específica mediante funciones de orden superior.

## 🧭 Contenido

- [🎯 Objetivos de la Semana](#-objetivos-de-la-semana)
- [🗂️ Ruta de Aprendizaje de la Semana](#️-ruta-de-aprendizaje-de-la-semana)
- [🧩 Conceptos Clave](#-conceptos-clave)
- [🧭 Navegación entre Módulos](#-navegación-entre-módulos)
- [📫 Contacto](#-contacto)

---

## 🎯 Objetivos de la Semana

1. **Evitar el "problema del billón de dólares":** Modelar datos con tipos producto y tipos suma para eliminar los estados inválidos y los errores por referencias nulas (`NoneType`).
2. **Dominar el Pattern Matching Estructural:** Usar la sintaxis `match / case` de Python para inspeccionar datos por su forma y desestructurar atributos de forma segura.
3. **Abstraer la repetición con HOFs:** Comprender cómo pasar y retornar funciones para desacoplar el algoritmo de control de la lógica particular.
4. **Construir Pipelines Declarativos:** Encadenar `filter`, `map` y `sorted` para procesar flujos de datos sin listas auxiliares ni mutación.

---

## 🗂️ Ruta de Aprendizaje de la Semana

| Módulo | Enfoque Central | Temas Destacados | Enlace |
|:---:|---|---|:---:|
| 🧩 **Clase 3** | **Pattern Matching Estructural** | Tipos suma/producto, `dataclass(frozen=True)`, desestructuración con `match/case` | [Ver Clase 3 ➔](Clase-3/README.md) |
| ⚙️ **Clase 4** | **HOFs y Funciones Lambda** | Funciones de primera clase, sintaxis `lambda`, `map`, `filter`, `sorted` y pipelines | [Ver Clase 4 ➔](Clase-4/README.md) |
| 🧪 **Tarea Formativa** | **Práctica y Consolidación** | 10 ejercicios prácticos: migraciones lambda, encadenamientos y HOFs artesanales | [Ver Tarea ➔](Tarea-FormativaEjerciciosPractica/README.md) |

---

## 🧩 Conceptos Clave

```
                                  ┌────────────────────────┐
                                  │   Semana 2: Enfoque    │
                                  └───────────┬────────────┘
                                              │
                     ┌────────────────────────┴────────────────────────┐
                     ▼                                                 ▼
        ┌─────────────────────────┐                       ┌─────────────────────────┐
        │  Modelado Seguro        │                       │  Abstracción Funcional  │
        │  (Clase 3)              │                       │  (Clase 4)              │
        ├─────────────────────────┤                       ├─────────────────────────┤
        │ • Tipos Producto (Y)    │                       │ • HOFs (map / filter)   │
        │ • Tipos Suma (O)        │                       │ • Expresiones Lambda    │
        │ • match / case          │                       │ • Pipelines declarativos│
        └─────────────────────────┘                       └─────────────────────────┘
```

- **Hacer lo ilegal irrepresentable:** Diseñar modelos de datos en los que un estado inconsistente simplemente no compile ni pueda instanciarse.
- **Transparencia en el flujo de datos:** Reemplazar acumuladores mutables y bucles anidados por transformaciones encadenadas puras.
- **Inyección de comportamiento:** Tratar a las funciones como valores de primera clase que pueden ser enviados como argumentos para dinamizar cualquier proceso.

---

## 🧭 Navegación entre Módulos

<div align="center">

| 🧩 Clase 3 | ⚙️ Clase 4 | 🧪 Tarea Formativa |
| :---: | :---: | :---: |
| [Pattern Matching Estructural](Clase-3/README.md) | [HOFs y Lambdas](Clase-4/README.md) | [10 Ejercicios Prácticos](Tarea-FormativaEjerciciosPractica/README.md) |

</div>

---

## 📫 Contacto

- 💼 **LinkedIn:** [David Parraga Mendoza](https://www.linkedin.com/in/davidparragamendoza/)
- 𝕏 **X:** [@DavidParragaMen](https://x.com/DavidParragaMen)

<div align="center">

✨ **Gracias por visitar este proyecto** ✨

</div>
