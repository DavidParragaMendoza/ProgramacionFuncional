<div align="center">

# 🟢 Tema 1 · El cambio de paradigma

### Del “cómo” al “qué”

<img src="https://img.shields.io/badge/Enfoque-Declarativo-2EA44F?style=for-the-badge" alt="Enfoque declarativo">
<img src="https://img.shields.io/badge/Python-Transformaciones-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Transformaciones en Python">

**Aprende a describir qué quieres obtener**
**sin controlar manualmente cada paso del recorrido.**

</div>

> [!IMPORTANT]
> El cambio de paradigma no elimina la lógica: cambia la forma de expresarla. En lugar de controlar el recorrido y el estado, declaramos las transformaciones que necesitamos.

## 🧭 Contenido

- [🎯 Idea central](#-idea-central)
- [⚖️ Dos formas de resolver](#️-dos-formas-de-resolver)
- [🔗 Puente hacia los siguientes temas](#-puente-hacia-los-siguientes-temas)
- [📝 Cuestionario](#-cuestionario)

## 🎯 Idea central

El enfoque **imperativo** describe las instrucciones y el orden en que deben ejecutarse. El enfoque **funcional o declarativo** se concentra en el resultado y en las transformaciones que deben aplicarse sobre los datos.

| Enfoque | Pregunta principal | Herramientas frecuentes |
|---|---|---|
| 🔴 Imperativo | ¿Cómo lo hago paso a paso? | `for`, `if`, estado mutable, `.append()` |
| 🟢 Funcional/declarativo | ¿Qué transformación necesito? | `filter`, `map`, composición, funciones |

## ⚖️ Dos formas de resolver

Supongamos que tenemos calificaciones y queremos conservar las aprobadas (`≥ 7`) para sumarles un punto.

### 🔴 Enfoque imperativo · describir el “cómo”

```python
notas = [5, 7, 8, 6, 10]
aprobadas = []

for nota in notas:
    if nota >= 7:
        aprobadas.append(nota + 1)
```

Aquí controlamos manualmente el recorrido, la condición, la lista de salida y la mutación de esa lista.

### 🟢 Enfoque funcional · expresar el “qué”

```python
notas = [5, 7, 8, 6, 10]

aprobadas = list(
    map(lambda nota: nota + 1,
        filter(lambda nota: nota >= 7, notas))
)
```

La solución expresa directamente la cadena de transformación:

```text
notas → filtrar aprobadas → sumar un punto → lista final
```

<details>
<summary>💡 ¿Por qué es una solución declarativa?</summary>

Porque `filter` se encarga de conservar los valores que cumplen la regla y `map` se encarga de transformarlos. Las funciones anónimas (`lambda`) describen las reglas específicas, mientras que el recorrido queda encapsulado en las funciones de orden superior.

</details>

## 🔗 Puente hacia los siguientes temas

Este tema introduce la idea general de **transformar datos**. En el Tema 2 aprenderás a reconocer primero la forma de esos datos con `match / case`; en el Tema 3 reutilizarás funciones para crear transformaciones más flexibles.

📚 Siguiente: [Tema 2 · Pattern Matching estructural](Tema2-PatternMatchingEstructural.md)

## 📝 Cuestionario

[Abrir cuestionario del Tema 1](https://notebook.google.com/notebook/57cefa59-c884-40fc-b912-f1ea5619053e/artifact/55712228-4b87-442b-892f-3b829236106c?utm_source=nlm_web_share&utm_medium=google_oo&utm_campaign=art_share_1&utm_content=&utm_smc=nlm_web_share_google_oo_art_share_1_)

↩️ Volver al [README de la Unidad 1](readme.md)
