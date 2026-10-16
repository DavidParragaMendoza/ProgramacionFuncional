<div align="center">

# 🧭 Semana 4 · Clase 8

### Unidad 1 · Repaso de Programación Funcional

[![Clase 7](https://img.shields.io/badge/Anterior-Clase_7-3776AB?style=for-the-badge)](../Clase-7/README.md)
[![Clase 8](https://img.shields.io/badge/Clase_8-Repaso-2EA44F?style=for-the-badge)](README.md)
[![Unidad 1](https://img.shields.io/badge/Unidad_1-Fundamentos-8250DF?style=for-the-badge)](Unidad1-RepasoFuncional/readme.md)

<br>

<img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10 o superior">
<img src="https://img.shields.io/badge/Temas-3-2EA44F?style=for-the-badge" alt="3 temas">
<img src="https://img.shields.io/badge/Ejercicios-3-8250DF?style=for-the-badge" alt="3 ejercicios">

**Un repaso práctico para expresar transformaciones,**
**reconocer estructuras y componer funciones reutilizables.**

</div>

> [!IMPORTANT]
> La clase conecta tres ideas fundamentales: cambiar del enfoque imperativo al declarativo, reconocer la forma de los datos con `match / case` y transformar colecciones mediante funciones de orden superior.

## 🧭 Contenido

- [🎯 Objetivo](#-objetivo)
- [🗂️ Ruta de aprendizaje](#️-ruta-de-aprendizaje)
- [💡 Conexión entre temas](#-conexión-entre-temas)
- [🧪 Ejercicios prácticos](#-ejercicios-prácticos)
- [▶️ Ejecución](#️-ejecución)
- [📚 Material de estudio](#-material-de-estudio)

## 🎯 Objetivo

Repasar los fundamentos de la programación funcional en Python mediante una ruta progresiva:

1. Expresar **qué** transformación se necesita, en lugar de describir cada paso.
2. Reconocer la forma y el contenido de los datos con **Pattern Matching**.
3. Utilizar **HOFs**, lambdas, `map`, `filter` y composición para crear soluciones flexibles.

## 🗂️ Ruta de aprendizaje

| Tema | Concepto central | Aplicación |
|:---:|---|---|
| 🟢 **1** | [El cambio de paradigma](Unidad1-RepasoFuncional/Tema1-ElCambiodeParadigma.md) | Pasar del enfoque imperativo al declarativo |
| 🟠 **2** | [Pattern Matching estructural](Unidad1-RepasoFuncional/Tema2-PatternMatchingEstructural.md) | Analizar tipos, valores y estructuras |
| 🔵 **3** | [Funciones de orden superior](Unidad1-RepasoFuncional/Tema-3-FuncionesOrdenSuperior.md) | Encadenar reglas y transformaciones |

## 💡 Conexión entre temas

Los tres temas se pueden aplicar como un pipeline funcional:

```text
Cambiar el enfoque
        ↓
Reconocer la estructura del dato
        ↓
Filtrar y transformar con funciones
        ↓
Componer una solución reutilizable
```

Por ejemplo, un programa puede reconocer eventos con `match / case`, conservar los eventos prioritarios usando `filter` y generar un resumen con `map`.

## 🧪 Ejercicios prácticos

### 🟢 Ejercicio 1 · Reimplementando `map`

En [ReimplementandoMap.py](Unidad1-RepasoFuncional/ReimplementandoMap.py) se construye una HOF que recibe una función transformadora y una lista. El ejercicio aplica la función a cada elemento sin utilizar directamente `map` ni modificar la lista original.

### 🟠 Ejercicio 2 · Procesador de eventos

En [ProcesadordeEventos.py](Unidad1-RepasoFuncional/ProcesadordeEventos.py) se utiliza `match / case` para procesar pedidos, usuarios, errores y formatos no reconocidos.

El programa incluye una guarda para distinguir entre pedidos prioritarios y pedidos estándar:

```python
case ("pedido", id_pedido, monto) if monto > 100:
    return f"Pedido prioritario #{id_pedido} por ${monto}"
```

### 🔵 Ejercicio 3 · Composición y auditoría

En [ComposiciónyEnvolvente.py](Unidad1-RepasoFuncional/ComposiciónyEnvolvente.py) se crean nuevas funciones a partir de otras:

- `componer(f, g)` combina dos funciones en el orden `g(f(x))`.
- `con_auditoria(funcion)` envuelve una función y registra la entrada y el resultado.

Este ejercicio relaciona HOFs, closures y envolventes.

## ▶️ Ejecución

Desde la carpeta `Clase-8`, ejecuta cualquiera de los ejercicios:

```bash
python Unidad1-RepasoFuncional/ReimplementandoMap.py
python Unidad1-RepasoFuncional/ProcesadordeEventos.py
python Unidad1-RepasoFuncional/ComposiciónyEnvolvente.py
```

Los ejercicios utilizan únicamente la biblioteca estándar de Python, por lo que no requieren instalar paquetes externos.

## 📚 Material de estudio

La carpeta [Unidad1-RepasoFuncional](Unidad1-RepasoFuncional/readme.md) contiene el repaso completo, ejemplos explicativos y cuestionarios de la unidad.

> [!TIP]
> Estudia los temas en orden y modifica los ejercicios con nuevos datos, reglas y tipos de eventos para comprobar cómo se comportan las transformaciones funcionales.

## 📫 Contacto

- 💼 **LinkedIn:** [David Parraga Mendoza](https://www.linkedin.com/in/davidparragamendoza/)
- 𝕏 **X:** [@DavidParragaMen](https://x.com/DavidParragaMen)
