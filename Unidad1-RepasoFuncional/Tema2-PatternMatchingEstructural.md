<div align="center">

# 🟠 Tema 2 · Pattern Matching estructural

### Dando vida a los tipos y a la forma de los datos

<img src="https://img.shields.io/badge/Python-match%20%2F%20case-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python match case">
<img src="https://img.shields.io/badge/Patrones-Estructurales-F9A03C?style=for-the-badge" alt="Patrones estructurales">

**Reconoce valores, tipos y estructuras**
**sin encadenar condicionales difíciles de leer.**

</div>

> [!IMPORTANT]
> El Pattern Matching Estructural no evalúa únicamente el tipo. También puede analizar el valor, la forma del dato, sus partes internas y condiciones adicionales.

## 🧭 Contenido

- [🎯 ¿Qué evalúa?](#-qué-evalúa)
- [🧩 Patrones disponibles](#-patrones-disponibles)
- [💡 Ejemplo](#-ejemplo)
- [📝 Ejercicio práctico](#-ejercicio-práctico)
- [🔗 Conexión con la unidad](#-conexión-con-la-unidad)

## 🎯 ¿Qué evalúa?

En Python, `match / case` es similar a un `switch`, pero permite comparar la estructura completa de un dato:

| Patrón | Ejemplo | Qué permite hacer |
|---|---|---|
| Literal | `case "iniciar"` | Comparar un valor exacto |
| Tupla o lista | `case ("login", usuario)` | Desempaquetar valores |
| Clase | `case Circulo(radio)` | Reconocer tipos y atributos |
| Guarda | `case Rectangulo(a, h) if a == h` | Añadir una condición |
| Comodín | `case _` | Cubrir cualquier otro caso |

> [!TIP]
> Si lo que cambia es la forma del dato recibido, `match / case` puede reemplazar cadenas de `if`, `elif`, `isinstance()` y `len()`.

## 🧩 Patrones disponibles

- **Valores simples:** `case "iniciar"` o `case "detener"`.
- **Estructuras:** `case ("login", usuario)` o `case ("pago", monto)`.
- **Tipos y clases:** `case Circulo(radio)` o `case Rectangulo(ancho, alto)`.
- **Guardas:** `case Rectangulo(a, h) if a == h`.

## 💡 Ejemplo

```python
def procesar_pedido(pedido):
    match pedido:
        case ("descuento", porcentaje):
            return f"Aplicando {porcentaje}% de descuento"
        case Circulo(radio):
            return 3.1416 * (radio ** 2)
        case _:
            return "Formato no reconocido"
```

La función puede reaccionar de forma distinta según la estructura recibida y extraer los valores internos directamente.

## 📝 Ejercicio práctico · Procesador de eventos

Escribe una función `procesar_evento(evento)` usando `match / case` con las siguientes reglas:

| Entrada | Condición | Resultado |
|---|---|---|
| `("pedido", id_pedido, monto)` | `monto > 100` | `"Pedido prioritario #{id_pedido} por ${monto}"` |
| `("pedido", id_pedido, monto)` | Cualquier otro monto | `"Pedido estándar #{id_pedido}"` |
| `("usuario", nombre)` | Siempre | `"Bienvenido/a {nombre}"` |
| `("error", codigo)` | Siempre | `"Alerta: Error {codigo}"` |
| Otro formato | Siempre | `"Evento no reconocido"` |

### Plantilla de inicio

```python
from typing import Any


def procesar_evento(evento: tuple[Any, ...]) -> str:
    match evento:
        case ("pedido", id_pedido, monto) if monto > 100:
            return f"Pedido prioritario #{id_pedido} por ${monto}"
        case ("pedido", id_pedido, monto):
            return f"Pedido estándar #{id_pedido}"
        case ("usuario", nombre):
            return f"Bienvenido/a {nombre}"
        case ("error", codigo):
            return f"Alerta: Error {codigo}"
        case _:
            return "Evento no reconocido"


print(procesar_evento(("pedido", 1, 222)))
print(procesar_evento(("pedido", 2, 50)))
print(procesar_evento(("usuario", "David")))
print(procesar_evento(("error", 404)))
```

## 🔗 Conexión con la unidad

El Tema 1 enseña a pensar en transformaciones. Este tema añade la primera etapa del flujo: **reconocer y descomponer el dato**. En el Tema 3 usarás funciones de orden superior para procesar los casos reconocidos.

📚 Siguiente: [Tema 3 · Funciones de orden superior](Tema-3-FuncionesOrdenSuperior.md)

## 📝 Cuestionario

[Abrir cuestionario del Tema 2](https://notebook.google.com/notebook/57cefa59-c884-40fc-b912-f1ea5619053e/artifact/5d544a7b-8af9-4909-bd0e-5b0fab8196b8?utm_source=nlm_web_share&utm_medium=google_oo&utm_campaign=art_share_1&utm_content=&utm_smc=nlm_web_share_google_oo_art_share_1_)

↩️ Volver al [README de la Unidad 1](readme.md)
