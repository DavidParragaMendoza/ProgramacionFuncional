'''
9. HOF con lógica de negocio
Crea calcular_total(precios, regla), donde regla sea una función de ajuste. Pruébala en dos casos:

Sin descuento: lambda p: p
Descuento del 20% sólo si el precio supera los $100.
✔ Salida esperada:
calcular_total([50, 120, 300], lambda p: p) → 470
calcular_total([50, 120, 300], lambda p: p * 0.8 if p > 100 else p) → 386.0
💡 Pista: Combina sum(...) directamente sobre el map.
'''

def calcularTotal(precios, regla) -> float:
    return sum(map(regla, precios))

print(calcularTotal([50, 120, 300], lambda p: p))

print(calcularTotal([50, 120, 300], 
                    lambda p: 
                        p * 0.8 if p > 100 else p))