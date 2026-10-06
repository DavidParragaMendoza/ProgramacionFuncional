from functools import reduce

ventas = [15.50, 20.00, 5.20, 100.00]

# Sumar todo el inventario en una sola línea
total_ventas = reduce(lambda acumulado, actual: acumulado + actual, ventas)

print(f"Total en caja: ${total_ventas}")