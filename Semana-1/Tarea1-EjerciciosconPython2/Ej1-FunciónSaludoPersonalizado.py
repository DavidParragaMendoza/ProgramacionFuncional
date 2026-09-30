'''
Ejercicio 1: Función de Saludo Personalizado
Crea una función saludo_personalizado(nombre: str) que imprima un saludo.

Llama a la función dos veces con nombres diferentes.
'''

def saludoPersonalizado(nombre: str, apellido: str):
    print(f"Hola, {nombre} {apellido} Bienvenido a Programacion Funcional con Python.")

saludoPersonalizado("Ronald", "Parraga")
saludoPersonalizado("David", "Mendoza")
