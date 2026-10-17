from typing import Optional

def buscar_producto(id: int) -> Optional[str]:
    productos = {1: "laptop", 2: "Mouse"}
    return productos.get(id)


resultado = buscar_producto(2)

if resultado is not None:
    print(resultado.upper())
else:
    print("Estado None, el producto no existe")
