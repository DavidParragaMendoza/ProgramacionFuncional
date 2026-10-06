# Supongamos una lista de usuarios de una DB
usuarios = [
    {"user": "admin", "activo": True},
    {"user": "invitado", "activo": False},
    {"user": "root", "activo": True}
]

# Usando una función Lambda como argumento
activos = list(filter(lambda u: u["activo"], usuarios))

print(f"Usuarios conectados: {activos}")
