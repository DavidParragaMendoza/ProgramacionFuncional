# Ejercicio 4: División y Resto
# Enunciado: Declarar 'total_estudiantes' (28) y 'tamanio_grupo' (5). 
# Calcular grupos completos (división entera) y estudiantes sobrantes (módulo).
# -----------------------------------------------------------------------------

totalEstudiantes:int = int(input("Digite el numero de estudiantes: "))
numeroIntegrantes:int = int(input("Digite el numero de integrantes del grupo: "))

grupos:int = totalEstudiantes//numeroIntegrantes 
print(f"grupos: {grupos}")

sobrante:int= totalEstudiantes%numeroIntegrantes
print(f"sobrante: {sobrante}")
if sobrante >0 :
    grupos = grupos+1
print(f"grupos: {grupos}")