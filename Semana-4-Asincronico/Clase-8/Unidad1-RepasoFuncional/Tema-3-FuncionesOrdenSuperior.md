<div align="center">

# 🔵 Tema 3 · Funciones de orden superior

### HOFs · Lambdas · `map` · `filter` · Composición

<img src="https://img.shields.io/badge/Python-HOFs-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Funciones de orden superior en Python">
<img src="https://img.shields.io/badge/Transformaciones-Reutilizables-8250DF?style=for-the-badge" alt="Transformaciones reutilizables">

**Convierte las funciones en piezas reutilizables**
**para construir soluciones pequeñas y componibles.**

</div>

> [!IMPORTANT]
> Una función de orden superior puede recibir otra función como argumento, devolver una función como resultado o hacer ambas cosas.

## 🧭 Contenido

- [🎯 ¿Qué es una HOF?](#-qué-es-una-hof)
- [🧠 Principios fundamentales](#-principios-fundamentales)
- [🔄 `map` y `filter`](#-map-y-filter)
- [📝 Ejercicios](#-ejercicios)
- [🔗 Conexión con la unidad](#-conexión-con-la-unidad)

## 🎯 ¿Qué es una HOF?

Una **Higher-Order Function** o función de orden superior es una función que trabaja con otras funciones como si fueran valores comunes.

```python
def aplicar_dos_veces(funcion, valor):
    return funcion(funcion(valor))


def duplicar(numero):
    return numero * 2


print(aplicar_dos_veces(duplicar, 3))
# 12
```

## 🧠 Principios fundamentales

| Principio | Explicación |
|---|---|
| 🧱 Ciudadanos de primer orden | Una función se puede asignar, guardar, pasar y devolver |
| 🧩 Abstracción | Se separa el mecanismo general de la regla específica |
| 🔗 Composición declarativa | Varias transformaciones se encadenan en un flujo |

> [!TIP]
> El intérprete evalúa las llamadas anidadas de adentro hacia afuera, igual que la resolución de paréntesis en matemáticas.

## 🔄 `map` y `filter`

`map` y `filter` son HOFs nativas para recorrer colecciones:

| Función | Responsabilidad | Regla recibida |
|---|---|---|
| `filter` | Decide qué elementos conservar | Predicado que devuelve `True` o `False` |
| `map` | Transforma cada elemento | Función que devuelve un nuevo valor |

```python
notas = [5, 7, 8, 6, 10]

aprobadas = filter(lambda nota: nota >= 7, notas)
ajustadas = map(lambda nota: nota + 1, aprobadas)

print(list(ajustadas))
# [8, 9, 11]
```

La HOF mantiene la estructura del recorrido y la `lambda` define la regla concreta:

```text
filter + lambda → selecciona
map + lambda    → transforma
```

## 📝 Ejercicios

### 🟢 Ejercicio 1 · Reimplementando `map`

Escribe `transformar_coleccion(funcion_transformadora, lista)` para devolver una lista nueva, sin usar `map` ni mutar la lista original.

```python
def triplicar(numero: int) -> int:
    return numero * 3


def enmarcar(texto: str) -> str:
    return f"[{texto}]"


def transformar_coleccion(funcion, lista) -> list:
    resultado = []
    for valor in lista:
        resultado.append(funcion(valor))
    return resultado


print(transformar_coleccion(triplicar, [1, 2, 3, 4, 5]))
print(transformar_coleccion(enmarcar, ["Hola", "Mundo", "Python"]))
```

### 🟣 Ejercicio 2 · Composición y envolventes

```python
def duplicar(numero: int) -> int:
    return numero * 2


def sumar_diez(numero: int) -> int:
    return numero + 10


def componer(f, g):
    def nueva_funcion(valor):
        return g(f(valor))
    return nueva_funcion


def con_auditoria(funcion):
    def nueva_funcion(valor):
        print(f"[LOG] Ejecutando operación con entrada: {valor}")
        resultado = funcion(valor)
        print(f"[LOG] Resultado obtenido: {resultado}")
        return resultado
    return nueva_funcion


duplicar_y_sumar_diez = componer(duplicar, sumar_diez)
funcion_auditada = con_auditoria(duplicar_y_sumar_diez)

print(funcion_auditada(5))
```

<details>
<summary>💡 ¿Qué ocurre en el segundo ejercicio?</summary>

`componer` crea una función nueva que ejecuta `f` y después `g`. Luego, `con_auditoria` envuelve esa composición para registrar la entrada y el resultado sin modificar la lógica original.

</details>

## 🔗 Conexión con la unidad

El Tema 1 propone expresar transformaciones; el Tema 2 enseña a reconocer la forma de los datos; este tema completa el flujo al inyectar reglas reutilizables mediante funciones.

📚 Volver al [README de la Unidad 1](readme.md)

## 📝 Cuestionario

[Abrir cuestionario del Tema 3](https://notebook.google.com/notebook/57cefa59-c884-40fc-b912-f1ea5619053e/artifact/6a26e468-4e28-4417-ae7c-cb9d52d62607?utm_source=nlm_web_share&utm_medium=google_oo&utm_campaign=art_share_1&utm_content=&utm_smc=nlm_web_share_google_oo_art_share_1_)
