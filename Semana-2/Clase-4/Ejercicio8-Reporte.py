#Listado de ventas

pedidos: dict[str, float] = [
    {"cliente": "David", "total": 150.0, "pagado": True},
    {"cliente": "Ana", "total": 200.0, "pagado": False},
    {"cliente": "Luis", "total": 50.0, "pagado": True},
    {"cliente": "Maria", "total": 100.0, "pagado": False},
    {"cliente": "Carlos", "total": 75.0, "pagado": True}
]

#listdo de clientes que han pagado
clientesPagados = list(
    filter(lambda pedido: pedido["pagado"] == True, pedidos)
)

print("Clientes que han pagado:")
for pedido in clientesPagados:
    print(f"Cliente: {pedido['cliente']}, Total: {pedido['total']}")


#listado de clientes que han pagado aplicando el iva.

clientesPagadosConIVA = list(
    map(lambda pedido: { "cliente": pedido["cliente"], "total": round(pedido["total"] * 1.15, 2) },
        
        filter(lambda pedido: pedido["pagado"] == True, pedidos))
    )

print("\nClientes que han pagado con IVA:")
print(clientesPagadosConIVA)