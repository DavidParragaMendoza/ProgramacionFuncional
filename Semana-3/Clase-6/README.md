<div align="center">

# ⚡ Semana 3 · Clase 6

### Tema 2 · Closures y Estado Encapsulado

[![Clase 5](https://img.shields.io/badge/Anterior-Clase_5-3776AB?style=for-the-badge)](../Clase-5/README.md)
[![Clase 6](https://img.shields.io/badge/Clase_6-Closures-2EA44F?style=for-the-badge)](README.md)
[![Clase 7](https://img.shields.io/badge/Siguiente-Clase_7-8250DF?style=for-the-badge)](../../Semana-4-Asincronico/Clase-7/README.md)

<br>

<img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+">
<img src="https://img.shields.io/badge/Concepto-Closures-2EA44F?style=for-the-badge" alt="Closures">
<img src="https://img.shields.io/badge/Interfaz-Tkinter-8250DF?style=for-the-badge" alt="Tkinter">

**Comprender cómo una función puede conservar su entorno y proteger su estado interno**
**mediante closures, funciones anidadas y la palabra reservada `nonlocal`.**

</div>

> [!IMPORTANT]
> Esta clase conecta las **HOFs y lambdas** de la clase anterior con una aplicación práctica: un carrito de pedidos para restaurante con estado encapsulado.

## 🧭 Contenido

- [🎯 Objetivo](#-objetivo)
- [🔗 Relación con la clase anterior](#-relación-con-la-clase-anterior)
- [🧠 Funciones anidadas y entorno léxico](#02-entender-las-funciones-anidadas-y-el-entorno-léxico)
- [🔒 Concepto de closure](#03-el-concepto-fundamental-de-closure)
- [`nonlocal` y estado encapsulado](#04-modificar-el-estado-encapsulado-con-nonlocal)
- [🧪 Casos prácticos](#06-casos-prácticos-y-modelos-de-uso-vistos-en-clase)
- [🖥️ Aplicación práctica](#️-aplicación-práctica)
- [▶️ Instalación y ejecución](#️-instalación-y-ejecución)
- [✅ Criterio práctico](#07-criterio-práctico-cuándo-y-por-qué-usar-closures)

---

## 🎯 Objetivo

Aprender a crear funciones que mantengan acceso a su entorno de origen y utilicen ese contexto para encapsular información. Al finalizar, se podrá distinguir entre una variable local, global y `nonlocal`, además de aplicar closures en un programa interactivo.

## 🔗 Relación con la clase anterior

En la [Clase 5](../Clase-5/README.md) se estudiaron las **lambdas** y las **HOFs (Funciones de Orden Superior)**, capaces de recibir funciones como parámetros o retornar nuevas funciones.

En esta clase se profundiza en una de esas capacidades: cuando una HOF retorna una función, esa función puede conservar el acceso a las variables del contexto donde fue creada, aunque la función exterior ya haya finalizado.

### Pregunta clave

> ¿Puede una función retornada conservar el acceso a las variables del entorno donde nació, incluso después de que la función exterior haya terminado?

---

## 02. Entender las Funciones Anidadas y el Entorno Léxico

Para dar respuesta a esta interrogante, analizamos dos conceptos fundamentales de la estructura de ejecución en Python:

- **`Función Anidada:`** Es una función definida en el cuerpo interno de otra función (`def interna()` dentro de `def externa()`).
- **`Entorno Léxico (Lexical Scope):`** Es el contexto y alcance específico en el que fue definida una función. En este entorno existen variables y parámetros visibles que la función interna puede observar desde su creación.

```python
def externa():
    # Entorno léxico de la función externa
    def interna():
        print("Ejecutando función interna")
    return interna
```

---

## 03. El Concepto Fundamental de Closure

Un **Closure** (o clausura) es una función interna que conserva "memoria" o acceso a las variables del entorno exterior donde fue creada, incluso después de que la función contenedora (padre) haya concluido su ejecución.

### Ejemplo Básico: Generador de Mensajes
```python
def saludar(nombre):
    # La función 'mensaje' no recibe 'nombre', pero lo 'recuerda' de su entorno padre
    def mensaje():
        return f"Hola, {nombre}"
    return mensaje

# Creación de la clausura
saludar_ana = saludar("Ana")

# La función externa 'saludar' ya finalizó, pero 'saludar_ana' mantiene la memoria del parámetro "Ana"
print(saludar_ana())  # Salida: Hola, Ana
```

- **`Función exterior:`** Aporta el contexto y las variables del entorno léxico.
- **`Función interior:`** Conserva el acceso a dicho contexto y mantiene el estado encapsulado.

---

## 04. Modificar el Estado Encapsulado con `nonlocal`

Por defecto, en Python una función interna puede **leer** variables de su entorno exterior. No obstante, si intenta **reasignar o modificar** una variable del scope envolvente, Python interpretará que se trata de una nueva variable local. Para poder modificar el estado del scope padre, utilizamos la palabra reservada **`nonlocal`**.

### La palabra clave `nonlocal`:
Indica explícitamente a Python que la variable pertenece al ámbito de la función envolvente (padre) y no al ámbito local de la función interna ni al global.

### Ejemplo: El Patrón Contador
```python
def crear_contador():
    contador = 0  # Estado privado encapsulado

    def incrementar():
        nonlocal contador  # Permite modificar la variable del entorno padre
        contador += 1
        return contador

    return incrementar

# Instanciación del closure
mi_contador = crear_contador()

print(mi_contador())  # 1
print(mi_contador())  # 2
print(mi_contador())  # 3
```

---

## 05. Distinguir Variables Locales, Globales y `nonlocal`

| Ámbito | Declaración | Comportamiento y Alcance |
| :--- | :--- | :--- |
| **`Global`** | `global variable` | Vive a nivel de módulo. Es accesible desde cualquier punto, pero susceptible a modificaciones imprevistas en programas complejos. |
| **`Local`** | `variable = valor` | Existe únicamente dentro de la función actual. Se destruye al finalizar la llamada. |
| **`Nonlocal`** | `nonlocal variable` | Pertenece al entorno envolvente de la función padre (Closure). Otorga un **estado privado y protegido**, inaccesible directamente desde fuera del closure. |

---

## 06. Casos Prácticos y Modelos de Uso Vistos en Clase

### A. Generador de Multiplicadores (Fijación de Parámetros)
Permite construir funciones especializadas sin necesidad de volver a pasar el factor de multiplicación en llamadas posteriores:

```python
def generador_multiplicador(factor):
    def multiplicar(valor):
        return valor * factor  # Recuerda el factor asignado en la creación
    return multiplicar

por_dos = generador_multiplicador(2)
por_tres = generador_multiplicador(3)

print(por_dos(5))   # 10
print(por_tres(5))  # 15
```

### B. Rate Limiter (Limitador de Peticiones e Independencia de Estados)
Muestra cómo **cada instancia de closure administra un estado privado completamente independiente**:

```python
def crear_limitador(max_intentos):
    intentos = 0
    def limitar(usuario):
        nonlocal intentos
        if intentos < max_intentos:
            intentos += 1
            return f"Petición aceptada para {usuario} (Intento {intentos})"
        return f"Petición denegada para {usuario}: límite alcanzado"
    return limitar

# Instancias independientes
limite_a = crear_limitador(3)
limite_b = crear_limitador(3)

# limite_a puede agotar sus 3 intentos sin alterar el contador de limite_b
```

### C. Estado Complejo Encapsulado: Cuenta Bancaria (Diccionario de Interfaz)
Un closure puede ofrecer **múltiples operaciones** sobre un mismo estado encapsulado mediante un diccionario que mapea nombres de acciones a funciones internas:

```python
def crear_cuenta_bancaria(saldo_inicial):
    saldo = saldo_inicial

    def depositar(monto):
        nonlocal saldo
        saldo += monto
        return f"Depósito realizado. Saldo actual: {saldo}"

    def retirar(monto):
        nonlocal saldo
        if monto <= saldo:
            saldo -= monto
            return f"Retiro realizado. Saldo actual: {saldo}"
        return "Fondos insuficientes"

    def consultar():
        return f"Saldo actual: {saldo}"

    # Exposición de interfaz mediante diccionario
    return {
        "depositar": depositar,
        "retirar": retirar,
        "consultar": consultar
    }

cuenta = crear_cuenta_bancaria(100)
print(cuenta["consultar"]())     # Saldo actual: 100
print(cuenta["depositar"](50))   # Depósito realizado. Saldo actual: 150
print(cuenta["retirar"](30))     # Retiro realizado. Saldo actual: 120
print(cuenta["retirar"](200))    # Fondos insuficientes
```

### D. Memoria Caché / Memoización
Uso de closures con un diccionario privado para almacenar resultados de operaciones costosas (como elevaciones al cuadrado) y evitar recálculos redundantes:

```python
def crear_calculadora_cache():
    cache = {}  # Estado de caché privado y persistente
    def elevar_al_cuadrado(numero):
        if numero in cache:
            print(f"Obteniendo del caché para {numero}...")
            return cache[numero]
        print(f"Calculando cuadrado de {numero}...")
        resultado = numero ** 2
        cache[numero] = resultado
        return resultado
    return elevar_al_cuadrado
```

---

## 🖥️ Aplicación práctica

El archivo [`clouse_ttk.py`](clouse_ttk.py) integra los conceptos de la clase en una interfaz gráfica de pedidos para restaurante:

- `crear_carrito()` encapsula los productos del pedido y expone solo las operaciones necesarias.
- `crear_calculadora_envio()` conserva el costo fijo de envío y aplica envío gratuito desde los `$20`.
- `procesar_menu()` funciona como HOF y recibe filtros definidos mediante lambdas.
- `AppRestaurante` utiliza `ttkbootstrap` para mostrar el menú, el carrito y los totales.

## ▶️ Instalación y ejecución

Instala la dependencia externa con:

```bash
python -m pip install ttkbootstrap
```

Después, ejecuta desde esta carpeta:

```bash
python clouse_ttk.py
```

Los módulos `typing` y `tkinter` pertenecen a la biblioteca estándar de Python.

## 07. Criterio Práctico: ¿Cuándo y Por Qué Usar Closures?

**Conviene usar un Closure cuando:**
- Requieres **proteger y mantener un estado interno** sin exponerlo a modificaciones globales indeseadas ni requerir la sobrecarga de una clase completa orientada a objetos.
- Deseas **aislar el contexto** entre múltiples ejecuciones o configuraciones de un sistema (como contadores, autenticadores o limitadores de peticiones).
- Buscas exponer un conjunto de funciones estrechamente ligadas a un mismo dato persistente utilizando diccionarios o tuplas de funciones.
