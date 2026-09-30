# 📓 Apuntes de Clase: Programación Funcional
**Tema:** Cambio de paradigma: Del "Cómo" al "Qué" 🚀
**Lenguaje Principal:** Python 🐍 (Java ☕ como puente conceptual)

---

## 🔄 1. El Cambio de Paradigma: Imperativo vs. Declarativo

La forma en que pensamos al programar define el paradigma. La transición principal aquí es dejar de pensar en los **pasos manuales** y empezar a enfocarnos en las **transformaciones de datos**.

| Característica | 🛠️ Enfoque Imperativo (El "Cómo") | 🎯 Enfoque Declarativo / Funcional (El "Qué") |
| :--- | :--- | :--- |
| **Foco** | Detallar paso a paso las instrucciones. | Describir el resultado esperado o el destino. |
| **Control** | Explícito (bucles `for`, `while`, condicionales `if`). | Implícito (el lenguaje maneja los detalles). |
| **Estado** | Mutable (las variables cambian de valor constantemente). | Inmutable (se crean nuevos datos, menos mutación). |
| **Analogía** | Dar direcciones exactas de cada cuadra para llegar a un lugar. | Dar la dirección final y dejar que el GPS encuentre la ruta. |

---

## 🏛️ 2. Los 3 Pilares de la Programación Funcional (PF)

Para que el código declarativo sea seguro y predecible, se basa en tres reglas de oro:

### A) Funciones Puras 🧪
Son como recetas matemáticas exactas. Cumplen dos reglas estrictas:
1. **Mismos inputs = Mismo output:** Siempre devuelven lo mismo si les pasas los mismos argumentos.
2. **Cero Efectos Secundarios (Side Effects):** No modifican nada fuera de su propio ámbito (no alteran variables globales, no escriben archivos, etc.).

```python
# ✅ FUNCIÓN PURA: Predecible y aislada
def sumar(a, b):
    return a + b

# ❌ FUNCIÓN IMPURA: Depende de un estado externo
descuento_global = 0.10
def calcular_precio(precio):
    return precio * (1 - descuento_global)
```

### B) Inmutabilidad 🧱
Una vez creado un dato, **NO** se puede cambiar. Si necesitas modificarlo, creas una *copia* con el nuevo valor.
*   **Python:** Listas (Mutables) vs. Tuplas (Inmutables).
*   **Java:** `String` (Inmutable) vs. `StringBuilder` (Mutable).

```python
mi_tupla = (1, 2, 3)
# mi_tupla.append(4) -> ERROR 🚫
nueva_tupla = mi_tupla + (4,) # ✅ Correcto: Se crea una nueva
```

### C) Transparencia Referencial 🔍
Gracias a las funciones puras, puedes reemplazar cualquier llamada a una función por su resultado sin que el programa se rompa.
> *Ejemplo:* Si `sumar(2,3)` siempre es `5`, puedes cambiar el código directamente a `5` y nada fallará. Esto hace el código súper fácil de optimizar.

---

## ⚡ 3. ¿Por qué importa esto hoy?
Antes, los procesadores solo se hacían más rápidos. Hoy, tienen **más núcleos (multi-core)**. 
*   **El problema imperativo:** Muchos núcleos intentando modificar la misma variable causan *race conditions* (condiciones de carrera) y requieren bloqueos complejos.
*   **La solución funcional:** Si los datos son **inmutables** y las funciones son **puras**, no hay nada que bloquear ni sincronizar. ¡El procesamiento en paralelo es seguro y nativo!

---
