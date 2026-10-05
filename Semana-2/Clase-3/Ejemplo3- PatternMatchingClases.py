from dataclasses import dataclass

# 1. Definimos los Tipos Producto (las estructuras de datos)
@dataclass(frozen=True)
class Circulo:
    radio: float

@dataclass(frozen=True)
class Rectangulo:
    ancho: float
    alto: float

# 2. Definimos el Tipo Suma (la figura es Circulo 0 Rectangulo)
FormaGeometrica = Circulo | Rectangulo

# 3. Funcion de calculo usando Pattern Matching
def calcular_area(forma: FormaGeometrica) -> float:
    match forma:
        case Circulo(r):
            # Reconoce si es Circulo y guarda su radio en 'r'
            return 3.1416 * (r ** 2)
        case Rectangulo(a, h):
            # Reconoce si es Rectangulo y guarda su ancho en 'a' y alto en 'h'
            return a * h
        case Rectangulo(a, h) if a == h:
            # Reconoce si es un cuadrado (Rectangulo con ancho igual a alto)
            return f"Es un cuadrado de {a}x{h}"


# 4. Ejemplos de uso
circulo = Circulo(radio=5)
rectangulo = Rectangulo(ancho=4, alto=6)

# 4. Ejemplos de uso 
circulo = Circulo(radio=5.0) 
rectangulo = Rectangulo(ancho=4.0, alto=6.0) 
print(calcular_area(circulo)) # Salida: 78.54 
print(calcular_area(rectangulo)) # Salida: 24