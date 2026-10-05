'''
### Ejercicio 1: Pipeline de Transacciones Bancarias (Filtro y Transformación de Diccionarios)

**Contexto:** Tienes un listado de transacciones bancarias representadas como diccionarios:

```python
transacciones = [
    {"id": 101, "tipo": "ingreso", "monto": 500.0, "aplica_impuesto": True},
    {"id": 102, "tipo": "egreso", "monto": 150.0, "aplica_impuesto": False},
    {"id": 103, "tipo": "ingreso", "monto": 100.0, "aplica_impuesto": True},
    {"id": 104, "tipo": "ingreso", "monto": 350.0, "aplica_impuesto": False},
    {"id": 105, "tipo": "egreso", "monto": 800.0, "aplica_impuesto": True},
    {"id": 106, "tipo": "ingreso", "monto": 250.0, "aplica_impuesto": True},
]
```

**Consigna:** Crea **una sola expresión encadenada** con `map`, `filter` y funciones `lambda` que:

1. **Filtre** con `filter`: conserve únicamente las transacciones que sean de tipo `"ingreso"` Y cuyo `monto` sea mayor o igual a `$200.0`.
2. **Transforme** con `map`: aplique un impuesto del  15% (`monto * 0.85`) si `"aplica_impuesto"` es `True`; si es `False`, mantenga el `monto` intacto. 
3. El resultado final debe ser una lista de nuevos diccionarios con la forma: `{"id": 101, "monto_neto": 425.0}`.
'''

transacciones = [
    {"id": 101, "tipo": "ingreso", "monto": 500.0, "aplica_impuesto": True},
    {"id": 102, "tipo": "egreso", "monto": 150.0, "aplica_impuesto": False},
    {"id": 103, "tipo": "ingreso", "monto": 100.0, "aplica_impuesto": True},
    {"id": 104, "tipo": "ingreso", "monto": 350.0, "aplica_impuesto": False},
    {"id": 105, "tipo": "egreso", "monto": 800.0, "aplica_impuesto": True},
    {"id": 106, "tipo": "ingreso", "monto": 250.0, "aplica_impuesto": True},
]

filtro= list(
    filter(lambda transaccion: transaccion["tipo"]=="ingreso" and transaccion["monto"]>=200.0, transacciones)
)


aplicarImpuesto = list(
    map(lambda t: 
        {"id": t["id"], "monto_neto": t["monto"] * 0.85 if t["aplica_impuesto"] else t["monto"]},filtro)
)

print(aplicarImpuesto)