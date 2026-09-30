'''
Operaciones Aritméticas Básicas
Python puede funcionar como una potente calculadora.
'''

# Suma
suma: int = 10 + 5 # Resultado: 15
# Resta
resta: int = 20 - 7 # Resultado: 13
# Multiplicación
multiplicacion: float = 2.5 * 4 # Resultado: 10.0
# División
division: float = 10 / 3 # Resultado: 3.333...
# División Entera
division_entera: int = 10 // 3 # Resultado: 3
# Módulo (resto de la división)
resto: int = 10 % 3 # Resultado: 1
# Potencia
potencia: int = 2 ** 3 # Resultado: 8

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("División Entera:", division_entera)
print("Módulo:", resto)
print("Potencia:", potencia)


planetas: list[str] = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]

for planeta in planetas:
    print(f"Explorando {planeta}...")
    print("")


def calcular_area_rectangulo(base: float, altura: float) -> float:
    area = base * altura
    return area

area_calculada = calcular_area_rectangulo(10.5, 5)
print(f"El área es: {area_calculada}")