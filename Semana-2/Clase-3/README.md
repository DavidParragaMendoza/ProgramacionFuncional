<div align="center">

# 🧩 Pattern Matching Estructural

### Semana 2 · Clase 3 · Tipos Producto, Tipos Suma y Extracción de Datos

[![Semana 2](https://img.shields.io/badge/Semana_2-Inicio-3776AB?style=for-the-badge&logo=readme&logoColor=white)](../README.md)
[![Clase 3](https://img.shields.io/badge/Clase_3-Pattern_Matching-0078D4?style=for-the-badge)](README.md)
[![Clase 4](https://img.shields.io/badge/Clase_4-HOFs_&_Lambdas-2EA44F?style=for-the-badge)](../Clase-4/README.md)
[![Tarea Formativa](https://img.shields.io/badge/Tarea_Formativa-Ejercicios-8250DF?style=for-the-badge)](../Tarea-FormativaEjerciciosPractica/README.md)

<br>

<img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+">
<img src="https://img.shields.io/badge/match_/_case-Estructural-2EA44F?style=for-the-badge" alt="Pattern Matching">
<img src="https://img.shields.io/badge/Tipos-Suma_&_Producto-8250DF?style=for-the-badge" alt="Tipos Suma y Producto">

**Modelado seguro y expresivo: prevención de estados inválidos,**
**estructuración de tipos algebraicos y desestructuración con match/case en Python.**

</div>

> [!IMPORTANT]
> La regla de oro en el modelado funcional es **hacer lo ilegal irrepresentable**: diseña las estructuras de datos de manera que sea imposible construir un estado defectuoso o inconsistente.

## 📌 En esta clase

- El problema de los estados inválidos y el uso excesivo de `None`.
- Tipos producto: datos que existen juntos (**Y**).
- Tipos suma: alternativas mutuamente excluyentes (**O**).
- Pattern matching estructural para procesar datos por su forma.
- Pattern matching aplicado a clases inmutables.

## 🧭 Contenido

- [💥 El problema del billón de dólares](#-el-problema-del-billón-de-dólares)
- [🛡️ La solución funcional](#️-la-solución-funcional)
- [🧱 Tipos producto y tipos suma](#-tipos-producto-y-tipos-suma)
- [🔎 Pattern matching estructural](#-pattern-matching-estructural)
- [🌐 Ejemplo: respuesta de un servidor](#-ejemplo-respuesta-de-un-servidor)
- [📐 Pattern matching con clases](#-pattern-matching-con-clases)
- [✅ Resumen](#-resumen)
- [🧭 Navegación entre Clases](#-navegación-entre-clases)
- [📫 Contacto](#-contacto)

---

## 💥 El problema del billón de dólares

En la programación tradicional solemos crear estructuras generales donde algunos campos pueden quedar vacíos (`None`). Después, cada parte del programa debe protegerse con comprobaciones como `if dato is not None:`.

El problema aparece cuando olvidamos una de esas comprobaciones:

```python
respuesta = {
    "exito": False,
    "usuario": None,
    "error": "Conexión fallida",
}

# El diseño permite leer un usuario que no existe.
print(respuesta["usuario"].upper())
# AttributeError: 'NoneType' object has no attribute 'upper'
```

La estructura permite representar una respuesta fallida que, al mismo tiempo, contiene un usuario inexistente. El error no se descubre hasta la ejecución.

> [!TIP]
> **Idea clave:** un buen diseño de tipos debe impedir que los estados inválidos puedan construirse en memoria desde el inicio.

---

## 🛡️ La solución funcional

La programación funcional busca **hacer lo ilegal irrepresentable**. Para ello, la arquitectura de datos se diseña con:

- **Tipos producto**, que agrupan datos que deben existir juntos.
- **Tipos suma**, que representan una opción entre varias alternativas.
- **Pattern matching**, que permite procesar cada alternativa de forma explícita.

Así, el tipo de cada dato comunica qué estados son válidos y guía al programador hacia un código más seguro.

---

## 🧱 Tipos producto y tipos suma

### Tipo producto: la relación «Y»

Un tipo producto agrupa varios campos que deben existir al mismo tiempo:

| Ejemplo | Datos requeridos |
| :--- | :--- |
| `Usuario` | ID **y** nombre **y** correo |
| `Coordenada` | Latitud **y** longitud |
| `Rectangulo` | Ancho **y** alto |

Si falta uno de los campos, la estructura está incompleta.

### Tipo suma: la relación «O»

Un tipo suma representa una alternativa entre varias posibilidades mutuamente excluyentes:

| Ejemplo | Alternativas |
| :--- | :--- |
| Respuesta de un servidor | `Exito` **o** `Error` |
| Figura geométrica | `Circulo` **o** `Rectangulo` **o** `Triangulo` |

Una respuesta no puede ser un éxito y un error al mismo tiempo. Cada variante contiene únicamente la información que necesita.

---

## 🔎 Pattern matching estructural

Normalmente, para procesar datos complejos escribimos cadenas de `if/elif` que comprueban tipos, longitudes o contenidos.

El **pattern matching estructural** (`match / case`) permite tomar decisiones evaluando directamente la forma del dato. Además de comprobar si el patrón coincide, puede extraer sus valores automáticamente.

Por ejemplo:

> Si recibimos una tupla de dos elementos cuya primera posición es `"login"`, podemos reconocerla y extraer el nombre desde la segunda posición.

Esto permite describir **qué forma esperamos** en lugar de escribir paso a paso cómo inspeccionar el dato.

---

## 🌐 Ejemplo: respuesta de un servidor

La respuesta de una consulta puede ser un éxito o un error. En lugar de usar campos opcionales, definimos dos estructuras válidas:

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Exito:
    usuario: str

@dataclass(frozen=True)
class Error:
    codigo: int

# Tipo suma: el resultado es un Exito o un Error, nunca None.
Resultado = Exito | Error
```

Ahora podemos procesar cada variante con total seguridad:

```python
def procesar_respuesta(res: Resultado) -> None:
    match res:
        case Exito(usuario):
            print(f"Usuario obtenido: {usuario.upper()}")
        case Error(codigo):
            print(f"Error detectado. Código: {codigo}")
```

### ¿Por qué este diseño es más seguro?

1. **Los estados inválidos no se pueden crear:** un `Exito` siempre requiere un usuario y un `Error` siempre requiere un código.
2. **Desaparecen los `None` sueltos:** cada variante guarda solo los datos que necesita.
3. **El patrón documenta la lógica:** cada `case` representa una posibilidad concreta del tipo suma.
4. **Los datos se extraen automáticamente:** no es necesario acceder a campos que podrían no existir.

---

## 📐 Pattern matching con clases

### 1. Importación e inmutabilidad

```python
from dataclasses import dataclass
```

`dataclass` pertenece a la biblioteca estándar de Python y evita escribir manualmente métodos repetitivos como `__init__`. Usaremos `frozen=True` para crear objetos inmutables, una práctica alineada con la programación funcional: una vez creado un objeto, sus datos no cambian.

### 2. Definición de `Circulo`

```python
@dataclass(frozen=True)
class Circulo:
    radio: float
```

- `class Circulo` define la estructura de un círculo.
- `radio: float` declara su único dato obligatorio.
- `frozen=True` impide modificar el radio después de crear el objeto.

### 3. Definición de `Rectangulo`

```python
@dataclass(frozen=True)
class Rectangulo:
    ancho: float
    alto: float
```

El rectángulo requiere **ancho y alto**. Ambos atributos forman un tipo producto.

### 4. Creación del tipo suma

```python
FormaGeometrica = Circulo | Rectangulo
```

El alias indica que una `FormaGeometrica` solo puede ser un `Circulo` o un `Rectangulo`.

### 5. Cálculo del área con `match`

```python
def calcular_area(forma: FormaGeometrica) -> float:
    match forma:
        case Circulo(radio):
            return 3.1416 * (radio ** 2)
        case Rectangulo(ancho, alto):
            return ancho * alto
```

| Patrón | Qué ocurre |
| :--- | :--- |
| `case Circulo(radio)` | Comprueba la clase y extrae su radio. |
| `case Rectangulo(ancho, alto)` | Comprueba la clase y extrae sus dos medidas. |
| `return ...` | Calcula y devuelve el área correspondiente. |

El `match` hace que la función sea fácil de leer: cada forma tiene una rama propia y los datos se reciben ya separados en variables útiles.

---

## ✅ Resumen

- **Tipos producto:** representan datos que deben existir juntos (**Y**).
- **Tipos suma:** representan alternativas válidas (**O**).
- **Pattern matching:** reconoce la forma de un dato y extrae su contenido.
- **Inmutabilidad:** evita cambios inesperados después de crear una estructura.
- **Diseño funcional:** reduce comprobaciones defensivas y evita estados inválidos desde el origen.

> **En una frase:** los tipos definen las formas válidas y el pattern matching permite procesarlas de manera segura y expresiva.

---

## 🧭 Navegación entre Clases

<div align="center">

| ⬅️ Anterior | 🏠 Menú de Semana 2 | Siguiente ➡️ |
| :---: | :---: | :---: |
| [🏠 Semana 2 (README)](../README.md) | [📚 Menú Principal](../README.md) | [Clase 4: HOFs y Lambdas ➡️](../Clase-4/README.md) |

</div>

---

## 📫 Contacto

- 💼 **LinkedIn:** [David Parraga Mendoza](https://www.linkedin.com/in/davidparragamendoza/)
- 𝕏 **X:** [@DavidParragaMen](https://x.com/DavidParragaMen)

<div align="center">

✨ **Gracias por visitar este proyecto** ✨

</div>
