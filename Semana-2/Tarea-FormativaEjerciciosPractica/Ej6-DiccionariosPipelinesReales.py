'''
6. Diccionarios en pipelines reales

productos = [
    {"nombre": "Teclado", "precio": 450,  "stock": 5},
    {"nombre": "Mouse",   "precio": 200,  "stock": 0},
    {"nombre": "Monitor", "precio": 3200, "stock": 3},
    {"nombre": "Cable",   "precio": 80,   "stock": 12},
]
Obtén una lista con únicamente los nombres de los productos con stock disponible (stock > 0) y precio inferior a $500, ordenados del más barato al más caro.

💡 Pista: Filtra verificando p["stock"] y p["precio"], ordena por precio y termina con un map que extraiga p["nombre"].
'''

productos = [
    {"nombre": "Teclado", "precio": 450,  "stock": 5},
    {"nombre": "Mouse",   "precio": 200,  "stock": 0},
    {"nombre": "Monitor", "precio": 3200, "stock": 3},
    {"nombre": "Cable",   "precio": 80,   "stock": 12},
]

#lista nombre producots disponibles 

productosDisponibles = list(
    map(lambda nombreProducto: nombreProducto["nombre"],
        sorted(
            filter(lambda producto: producto["stock"] > 0 and producto["precio"] < 500,productos),
            key=lambda producto: producto["precio"], reverse=False)
        )
)

print("Productos disponibles con stock y precio menor a $500:")
print(productosDisponibles)
