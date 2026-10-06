
<div align="center">

# ⚡ Semana 3 · Clase 5 · Funciones Anónimas

### Programación Funcional · HOFs · Lambdas

[![README](https://img.shields.io/badge/Clase_5-README-3776AB?style=for-the-badge&logo=readme&logoColor=white)](README.md)
[![Tema 4](https://img.shields.io/badge/Tema_4-Lambdas-2EA44F?style=for-the-badge)](Tema-4-Lambdas.md)

</div>

---

# 01. Conectar con las HOF del tema anterior

Una **HOF (Función de Orden Superior)** es aquella que puede recibir otra función como argumento, devolver una función como resultado, o ambas cosas. Los principales motivos de uso son:

- **`Separar lo general de lo específico:`** La HOF mantiene fija la estructura general (por ejemplo, el mecanismo de iterar o procesar una colección), mientras que la función que recibe por parámetro define la regla concreta que se ejecuta sobre cada elemento.
- **`Evitar duplicar código de recorrido:`** En lugar de escribir bucles `for` repetidos para cada nueva operación sobre una lista (como duplicar valores, elevarlos al cuadrado o filtrarlos), mantienes el patrón en una sola HOF y solo varías la acción recibida.
- **`Expresar transformaciones declarativas:`** Permite enfocar el código en **qué** transformación deseamos lograr sobre los datos en lugar de gestionar explícitamente el control de flujo paso a paso.

# 02. Entender qué es una lambda:

## Pregunta:

Si una función que voy a pasar como argumento solo se usará una vez, ¿vale la pena declararla con nombre o puedo describirla justo en el momento en que la necesito?

> Cuando una regla es breve y solo se usará en un punto específico como argumento de una HOF, no tiene sentido ensuciar el código creando una función con def.
> 

**`Lambda`**: Es una función anónima y breve que se expresa como una sola expresión

# 03. Distinguir def y lambda

- **La comparación** **def** **vs.** **lambda** **:**
    
    **`def:`** Ideal para lógica extensa, con varias líneas, reutilizable y que requiera nombre o documentación.
    
    ```python
    def cuadrado(x):
    	return x ** 2
    ```
    
- **`lambda:`** Diseñada para acciones directas de una sola expresión, anónimas y de alcance local.
    
    ```python
    cuadrado = lambda x: x ** 2
    ```
    

# 04. Construir la idea de HOF universal

## Pregunta:

```python
def duplicar(lista):
return [x * 2 for x in lista]

def elevar_cuadrado(lista) :
return [x ** 2 for x in lista]
```

**Si el patrón es el mismo, ¿por qué repetir la estructura?**

> 
> 
> 
> Si el recorrido de la lista es un simple `for` de una línea, crear una HOF manual puede parecer redundante a simple vista.
> 
> **Cuando la estructura del recorrido involucra 100 líneas de lógica**, duplicar toda esa estructura solo para cambiar una pequeña operación al final sería un desastre de mantenimiento.
> 

---

```python
def hof_universal (datos, operacion):
resultado = []
for elemento in datos:
resultado.append (operacion(elemento))
return resultado

print(hof_universal([1, 2, 3], lambda x: x * 2))
print(hof_universal([1, 2, 3], lambda x: x ** 2))
```

El recorrido repetitivo de la colección se queda fijo en la HOF, mientras que la regla específica de transformación se le delega a la `lambda`. Esa `hof_universal` es exactamente lo que Python ya trae construido internamente bajo el nombre de `map`.

# 05. Aplicar map, filter y reduce:

## Criterio práctico: cuándo usar lambda

**Conviene usar lambda si**

- La función es breve
- Se usará una sola vez
- Aporta claridad local

**Conviene usar def si**

- La lógica crece
- La función merece nombre propio
- Se reutilizará en varios lugares
