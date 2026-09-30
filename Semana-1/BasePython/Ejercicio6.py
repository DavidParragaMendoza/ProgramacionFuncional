# --- CONCEPTO: DICCIONARIOS (dict) ---
# Estructura: { "clave": valor, "clave2": valor2 }

estudiante: dict[str, str] = {
    "nombre": "Ronald",
    "edad": "25",
    "altura": "1.75"
}

estudiante["nombre"] ="David Parraga"
estudiante["identificacion"] = "123456789"
# Para obtener un dato, usamos su "etiqueta" entre corchetes []
print(f"nombre:  {estudiante["nombre"]}")
print(f"identificacion: {estudiante["identificacion"]}")

















