# Ejercicio 3: Conversor de Moneda Simple
# Enunciado: Crear variable 'dolares' y 'tasa_conversion_eur'. 
# Calcular el equivalente en euros e imprimir ambos valores.
# -----------------------------------------------------------------------------

dolar: float = 11
tasa_conversion_euro: float = 0.88
tasa_conversion_real: float = 5.19

euros: float = dolar * tasa_conversion_euro
reales: float = dolar * tasa_conversion_real
print("--------------------------")
print(f"Cantidad Dolar: {dolar}")
print(f"En Euros: {euros}")
print(f"En Reales: {reales}")
