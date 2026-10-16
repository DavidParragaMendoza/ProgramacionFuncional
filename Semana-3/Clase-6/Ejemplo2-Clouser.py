'''
Definición
Un closure es una función que conserva acceso a variables de su entorno exterior
incluso después de que la función exterior haya terminado.
'''
def saludar(nombre):
    def mensaje():
        return f"Hola, {nombre}"
    return mensaje

saludo_ana = saludar("Ana")
print(saludo_ana())
