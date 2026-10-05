'''
Microactividad
Pattern Matching Estructural
Si recibes datos como ("pago", 45), (üsuario", .Ana") y ("salir").

'''

def interpretar_comando(comando):
    match comando:
        case ("pago", monto):
            return f"Procesando pago de {monto}"
        case ("üsuario", nombre):
            return f"Bienvenido, {nombre}"
        case ("salir",):
            return "Saliendo del sistema"
        case _:
            return "Comando no reconocido"

comando: str = interpretar_comando(("üsuario", ".ana"))
print(comando)  # Esto imprimirá: Bienvenido, Anañ

comando: str = interpretar_comando(("pago", 45))
print(comando)  # Esto imprimirá: Procesando pago de 45

comando: str = interpretar_comando(("salir",))
print(comando)  # Esto imprimirá: Saliendo del sistema