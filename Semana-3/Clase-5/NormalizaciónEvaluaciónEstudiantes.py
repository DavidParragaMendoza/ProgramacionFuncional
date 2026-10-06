estudiantes = [
    ("  juan perez  ", [10, 5, 7, 8]),
    ("ana gomez", [10, 7, 9, 10]),
    (" CARLOS RUIZ ", [10, 5, 10, 10]),
    ("maria lopez", [5, 8, 10, 10]),
]

# Aplicamos map y filter anidados
resultado = list(
    map(
        lambda x: {
            "nombre": x[0].strip().upper(),
            "promedio": round(sum(x[1]) / len(x[1]), 2),
            "estado": "DESTACADO" if sum(x[1]) / len(x[1]) >= 9.0 else "APROBADO"
        },
        filter(
            lambda x: sum(x[1]) / len(x[1]) >= 7.0, 
            estudiantes
        )
    )
)

# Imprimir el resultado para verificar
for alumno in resultado:
    print(alumno)