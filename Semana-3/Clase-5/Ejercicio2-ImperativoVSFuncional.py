# MODO IMPERATIVO (El "Cómo")
precios = [100, 200, 300, 400]
impuestos = []
for p in precios:
    impuestos.append(p * 1.15)

# MODO FUNCIONAL CON HOF (El "Qué")
def aplicar_iva(precio):
    return precio * 1.15

precios_con_iva = list(map(aplicar_iva, precios))

'''
precioIva = list(
    map(lambda precio: precio * 1.15, precios)
)
'''