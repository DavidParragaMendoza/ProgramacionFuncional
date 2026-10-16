<div align="center">

# 🧭 Unidad 1 · Repaso Funcional

### Python · Paradigma declarativo · Pattern Matching · HOFs

<img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10 o superior">
<img src="https://img.shields.io/badge/Temas-3-2EA44F?style=for-the-badge" alt="3 temas">
<img src="https://img.shields.io/badge/Enfoque-Funcional-8250DF?style=for-the-badge" alt="Enfoque funcional">

**Una ruta de repaso para pasar del “cómo” al “qué”,**
**entender la forma de los datos y transformarlos con funciones reutilizables.**

</div>

> [!IMPORTANT]
> Los tres temas forman una secuencia: primero cambia tu forma de pensar, después reconoce las estructuras y finalmente compón transformaciones con funciones.

## 🧭 Contenido

- [🎯 Objetivo](#-objetivo)
- [🗂️ Ruta de aprendizaje](#️-ruta-de-aprendizaje)
- [🔗 Conexión entre temas](#-conexión-entre-temas)
- [🧩 Conceptos clave](#-conceptos-clave)
- [✅ Cómo estudiar](#-cómo-estudiar)

## 🎯 Objetivo

Esta unidad presenta los fundamentos necesarios para expresar soluciones funcionales en Python. El recorrido comienza con la diferencia entre el enfoque imperativo y el declarativo, continúa con el análisis de estructuras mediante `match / case` y termina con funciones de orden superior como `filter`, `map` y la composición.

> [!TIP]
> No memorices cada herramienta por separado. Pregúntate siempre: **¿qué forma tienen mis datos y qué transformación quiero expresar sobre ellos?**

## 🗂️ Ruta de aprendizaje

| Tema | Concepto central | Resultado esperado |
|:---:|---|---|
| 🟢 **1** | [Cambio de paradigma](Tema1-ElCambiodeParadigma.md) | Expresar el **qué** en lugar de describir cada paso |
| 🟠 **2** | [Pattern Matching estructural](Tema2-PatternMatchingEstructural.md) | Reconocer valores, tipos y estructuras |
| 🔵 **3** | [Funciones de orden superior](Tema-3-FuncionesOrdenSuperior.md) | Encadenar reglas y transformaciones reutilizables |

## 🔗 Conexión entre temas

Los contenidos se aplican como un pequeño pipeline funcional:

```text
1. Cambiar el enfoque
        ↓
2. Reconocer la estructura del dato
        ↓
3. Filtrar y transformar con funciones
```

Un ejemplo completo puede reconocer pedidos con `match`, conservar los prioritarios mediante `filter` y generar un resumen con `map`:

```python
def es_pedido_prioritario(evento):
    match evento:
        case ("pedido", _, monto) if monto > 100:
            return True
        case _:
            return False


def resumir_pedido(evento):
    match evento:
        case ("pedido", id_pedido, monto):
            return f"Pedido #{id_pedido}: ${monto}"
        case _:
            return "Evento no reconocido"


eventos = [
    ("pedido", 1, 220),
    ("usuario", "David"),
    ("pedido", 2, 50),
]

resumenes = list(
    map(resumir_pedido, filter(es_pedido_prioritario, eventos))
)

print(resumenes)
# ['Pedido #1: $220']
```

<details>
<summary>💡 ¿Qué demuestra este ejemplo?</summary>

`match / case` identifica la forma del evento; `filter` selecciona los datos que cumplen una regla; y `map` transforma los datos seleccionados. El resultado es una solución declarativa que no necesita índices, listas auxiliares ni mutaciones explícitas.

</details>

## 🧩 Conceptos clave

| Concepto | Papel en la unidad |
|---|---|
| Paradigma declarativo | Expresar el resultado o la transformación deseada |
| `match / case` | Reconocer formas, tipos y valores |
| Función de orden superior | Recibir o devolver otras funciones |
| `filter` | Seleccionar elementos según una regla |
| `map` | Transformar cada elemento |
| `lambda` | Definir reglas breves y anónimas |
| Composición | Encadenar transformaciones en un flujo |

## ✅ Cómo estudiar

1. Lee el [Tema 1](Tema1-ElCambiodeParadigma.md) y compara ambos paradigmas.
2. Practica el [Tema 2](Tema2-PatternMatchingEstructural.md) con eventos de distintas formas.
3. Resuelve los ejercicios del [Tema 3](Tema-3-FuncionesOrdenSuperior.md).
4. Modifica el ejemplo integrador y agrega nuevos tipos de eventos.
5. Completa el cuestionario incluido al final de cada tema.

> [!NOTE]
> Esta carpeta es una guía de repaso. Los archivos `.py` asociados contienen ejemplos prácticos para ejecutar y experimentar.
