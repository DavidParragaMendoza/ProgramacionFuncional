''''
Consigna
Si tienes una lista de precios, ¿cómo describirías verbalmente una solución para obtener solo los mayores a 20 y luego aplicarles un descuento del 10%?
'''

precios: list[float] = [10.0, 25.0, 30.0, 15.0, 50.0]

listaFinal: list[float] = list(
    map(lambda precio: precio * 0.99,
        filter(lambda precio: precio >= 20, precios))
)

print(listaFinal)