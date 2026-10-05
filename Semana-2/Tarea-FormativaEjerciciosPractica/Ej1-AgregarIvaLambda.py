'''
1. Calentamiento: De def a lambda
Dada la función existente:

def agregar_iva(precio):
    return precio * 1.16

Reescríbela como lambda asignada a agregar_iva_lambda.
Úsala junto a map para procesar la lista [100, 250, 40].

💡 Pista: La lambda devuelve el valor automáticamente: lambda precio: ... (sin palabra clave return).
'''

#lista de precios
listaPrecios:list[int] = [100, 250, 40]

#creacion de la funcion lambda
agregarIvaLambda = list(
    map(lambda precio: round(precio *1.16, 2), listaPrecios)
)

#mostrar el resultado
print(agregarIvaLambda)

