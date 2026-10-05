'''
7. Tu primera HOF (Higher-Order Function)

Escribe la función aplicar_dos_veces(funcion, valor) que reciba una función y un valor de entrada, devolviendo el resultado de aplicarla dos veces seguidas: f(f(x)).

✔ Salida esperada:
aplicar_dos_veces(lambda x: x + 3, 10) → 16
aplicar_dos_veces(lambda x: x * 2, 5) → 20

💡 Pista: En Python las funciones son objetos: puedes invocar el parámetro directamente como funcion(valor).
'''
def aplicarDosVeces(funcion, valor):
    return funcion(funcion(valor))

print(aplicarDosVeces(lambda x: x + 3, 10)) # → 16
print(aplicarDosVeces(lambda x: x * 2, 5)) # → 20
