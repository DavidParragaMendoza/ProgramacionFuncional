'''
Una tupla en Python es una estructura de datos que permite almacenar una colección múltiple de elementos en una sola variable. Es muy similar a una lista, pero con una diferencia clave: es estrictamente inalterable.
'''


'''
Ejemplo de uso de estructuras de datos en Python
def procesar_mensaje(msg): 
    match msg: 
        case ("login", usuario): 
            return f"Bienvenido, {usuario}" 
        case ("error", codigo): 
            return f"Error detectado: {codigo}" 
        case ("suma", a, b): 
            return a + b 
        case _: 
            return "Mensaje no valido"

# Ejemplos de uso
print(procesar_mensaje(("login", "Juan")))  # Bienvenido, Juan
print(procesar_mensaje(("error", 404)))  # Error detectado: 404
print(procesar_mensaje(("suma", 2, 3)))  # 5
'''

from typing import Any

# Definimos los tipos de tuplas posibles que puede recibir la función
TipoMensaje = (
    tuple[str, str] |          # Para ("login", usuario)
    tuple[str, int] |          # Para ("error", codigo)
    tuple[str, int, int] |     # Para ("suma", a, b)
    tuple[Any, ...]            # Para cualquier otra tupla
)

def procesar_mensaje(msg: TipoMensaje) -> str | int:
    match msg: 
        case ("login", usuario): 
            return f"Bienvenido, {usuario}" 
        case ("error", codigo): 
            return f"Error detectado: {codigo}" 
        case ("suma", a, b): 
            return a + b 
        case _: 
            return "Mensaje no valido"

# Ejemplos de uso
print(procesar_mensaje(("login", "Juan")))  # Bienvenido, Juan
print(procesar_mensaje(("error", 404)))   # Error detectado: 404
print(procesar_mensaje(("suma", 2, 3)))    # 5
print(procesar_mensaje(("otro", "dato", "datos")))  # Mensaje no valido