<div align="center">

# 🗂️ Gestor de Expedientes Virtuales

### Python · HOFs · Closures · Estado encapsulado

<img src="https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.14">
<img src="https://img.shields.io/badge/Proyecto-1-2EA44F?style=for-the-badge" alt="1 proyecto">
<img src="https://img.shields.io/badge/Conceptos-5-8250DF?style=for-the-badge" alt="5 conceptos funcionales">

**Un expediente académico que conserva su estado, valida calificaciones**
**y calcula el progreso del estudiante mediante programación funcional.**

</div>

> [!IMPORTANT]
> El gestor rechaza notas inferiores a `7.0` y solo acumula los registros aprobados.

## 🧭 Contenido

- [🎯 Objetivo](#-objetivo)
- [🧠 Conceptos aplicados](#-conceptos-aplicados)
- [⚙️ Funcionamiento](#️-funcionamiento)
- [▶️ Ejecución](#️-ejecución)
- [📫 Contacto](#-contacto)

## 🎯 Objetivo

Este ejercicio integra varios conceptos de programación funcional en un caso práctico: un gestor de expedientes académicos. Cada estudiante obtiene su propio gestor configurado con un nombre y puede registrar materias aprobadas sin exponer directamente el historial ni el total de créditos.

La implementación principal está en [`GestorExpedientesVirtuales.py`](GestorExpedientesVirtuales.py).

## 🧠 Conceptos aplicados

| Concepto | Aplicación |
|:---:|---|
| 🧩 **HOF** | `validarNota` recibe una función criterio para decidir si una calificación es válida. |
| 🔐 **Closure** | `crearExpediente` devuelve un gestor que conserva los datos del estudiante. |
| 🏠 **Estado encapsulado** | El historial y los créditos permanecen dentro del closure. |
| 🔁 **`nonlocal`** | Permite actualizar el estado privado entre llamadas. |
| 🧮 **`map`** | Extrae las notas registradas para calcular el promedio acumulado. |

## ⚙️ Funcionamiento

1. Se crea un expediente para un estudiante mediante `crearExpediente`.
2. Cada materia se valida con una lambda que exige una nota mínima de `7.0`.
3. Las materias aprobadas se agregan al historial y acumulan sus créditos.
4. El gestor calcula el promedio de las notas aprobadas y devuelve un resumen.

## ▶️ Ejecución

Desde esta carpeta, ejecuta:

```bash
python GestorExpedientesVirtuales.py
```

### Salida esperada

```text
Registro rechazado por validación de nota.
Estudiante: David Mendoza | Promedio: 9.5 | Créditos: 4
Estudiante: David Mendoza | Promedio: 9.8 | Créditos: 7
```

## 📫 Contacto

- 💼 **LinkedIn:** [David Parraga Mendoza](https://www.linkedin.com/in/davidparragamendoza/)
- 𝕏 **X:** [@DavidParragaMen](https://x.com/DavidParragaMen)

