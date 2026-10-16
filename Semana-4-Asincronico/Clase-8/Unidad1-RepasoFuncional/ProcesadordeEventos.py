'''
**Consigna:**
Escribe una función **`procesar_evento(evento)`** utilizando **`match / case`** que reciba distintas tuplas y retorne las siguientes respuestas:

1. **Tupla de pedido:** **`("pedido", id_pedido, monto)`**
    - Si el `monto` es mayor a 100 (usa una guarda **`if`**), devuelve: **`"Pedido prioritario #{id_pedido} por ${monto}"`**.
    - De lo contrario, devuelve: **`"Pedido estándar #{id_pedido}"`**.
2. **Tupla de usuario:** **`("usuario", nombre)`**
    - Devuelve: **`"Bienvenido/a {nombre}"`**.
3. **Tupla de error:** **`("error", codigo)`**
    - Devuelve: **`"Alerta: Error {codigo}"`**.
4. **Cualquier otro formato:**
    - Devuelve: **`"Evento no reconocido"`**.

'''
from typing import Any

evento = (
    tuple[str, int, int] |          # Para ("pedido", idPedido, monto)
    tuple[str, int] |               # Para ("error", codigo)
    tuple[str, str] |     # Para Usuario ("usuario", nombre)
    tuple[Any, ...]            # Para cualquier otra tupla
)

def procesarEvento(evento: evento) -> str:
    match evento:
        case ("pedido", idPedido, monto) if monto > 100:
            return f"Pedido prioritario #{idPedido} por ${monto}"
        case ("pedido", idPedido, monto):
            return f"Pedido estándar #{idPedido}"
        case("usuario", nombre):
            return f"Bienvenido/a {nombre}"
        case("error", codigo):
            return f"Alerta: Error {codigo}"
        case _:
            return "Evento no reconocido"


print(procesarEvento(("pedido", 1, 222)))
print(procesarEvento(("pedido", 2, 50)))
print(procesarEvento(("usuario", "David")))
print(procesarEvento(("error", 404)))