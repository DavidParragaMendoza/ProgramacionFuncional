'''
###  Ejercicio 2: Nivel "Hardcore" 🚀 (Composición y Envolventes / Decoradores)
Las HOFs no solo reciben funciones, ¡también las construyen y retornan!
**Consigna:**
1. **Composición de Funciones:** Escribe una HOF llamada `componer(f, g)` que reciba dos funciones `f` y `g` y devuelva una **NUEVA función**. Esta nueva función, al recibir un valor `x`, debe aplicar `g(f(x))` (es decir, primero ejecuta `f` y al resultado le aplica `g`).
2. **Envolvente / Auditoría:** Escribe una HOF llamada `con_auditoria(funcion)` que reciba una función y retorne una **NUEVA función**. Al ejecutarse la nueva función debe:
  * Imprimir: `f"[LOG] Ejecutando operación con entrada: {x}"`
  * Calcular el resultado llamando a la función original.
  * Imprimir: `f"[LOG] Resultado obtenido: {resultado}"`
  * Retornar el resultado.

**Prueba de fuego:**

1. Define dos funciones normales: `duplicar(x)` (multiplica por 2) y `sumar_diez(x)` (suma 10).
2. Usa `componer` para crear `duplicar_y_sumar_diez`.
3. Envuelve esa nueva función creada con `con_auditoria` para obtener `funcion_auditada`.
4. Ejecuta `funcion_auditada(5)` y observa el flujo completo.
'''

def duplicar(x: int) -> int:
    return x * 2

def sumar_diez(x: int) -> int:
    return x + 10

def componer(f, g):
    def nueva_funcion(x):
        return g(f(x))
    return nueva_funcion

def con_auditoria(funcion):
    def nueva_funcion(x):
        print(f"[LOG] Ejecutando operación con entrada: {x}")
        resultado = funcion(x)
        print(f"[LOG] Resultado obtenido: {resultado}")
        return resultado
    return nueva_funcion

duplicar_y_sumar_diez = componer(duplicar, sumar_diez)
funcion_auditada = con_auditoria(duplicar_y_sumar_diez)

print(funcion_auditada(5))  # Esto imprimirá el resultado final de la operación

