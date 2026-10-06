# 1. Las funciones pueden guardarse en variables
def saludar(nombre):
    return f"Hola, {nombre}"

mifuncion = saludar
print(mifuncion("Clase"))

# 2. DEFINICIÓN DE HOF:
# Una función es de Orden Superior si:
#   A) Recibe una función como argumento
#   B) Devuelve una función como resultado

def ejecutor(funcion_a_ejecutar, valor):
    return funcion_a_ejecutar(valor)

print(ejecutor(saludar, "Ingenieros"))
