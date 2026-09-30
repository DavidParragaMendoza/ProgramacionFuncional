# Ejercicio 5: Calculadora de IMC
# Enunciado: Crear variables para peso (kg) y altura (m). 
# Calcular el IMC usando la fórmula: peso / (altura^2). Imprimir el resultado.
# -----------------------------------------------------------------------------

peso:float=float(input("Escribra su peso: "))
altura:float=float(input("Escriba su altura: "))

#calculando el IMC
imc = peso / (altura ** 2)

print("--------------------------")
print(f" El IMC es: {imc}" )