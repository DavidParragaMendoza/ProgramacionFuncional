# 📚 Unidad 2: Patrones Funcionales Esenciales (HOFs, Lambdas, Closures y Estado)

## 1. Lógica Declarativa vs. Imperativa

El **paradigma imperativo** se centra en el *"cómo"*. Le decimos a la computadora paso a paso qué hacer, utilizando estructuras de control de flujo como bucles `for` o `while`, y modificando el estado de las variables constantemente.

El **paradigma declarativo** (donde entra la Programación Funcional) se centra en el *"qué"*. Describimos el resultado que queremos obtener aplicando transformaciones a los datos, delegando el control de flujo a funciones integradas.

*   **Herramientas clave:** En lugar de iterar con `for`, en Python usamos funciones como `map()` (para transformar cada elemento de una colección), `filter()` (para seleccionar elementos) y `sum()` o `len()` (para reducir o agregar datos).

## 2. Funciones Lambda - Funciones Anónimas

Las funciones lambda son funciones muy breves que se escriben en una sola línea. Son ideales para operaciones sencillas que solo se usarán en un momento y lugar específico del código, por lo que no necesitan un nombre formal definido con `def`.

*   **Estructura:** `lambda parametro: expresion`
*   **Ejemplo conceptual:** Una lambda para obtener el doble de un número sería `lambda x: x * 2`. No necesitan la palabra `return`, ya que devuelven el resultado de la expresión automáticamente.

## 3. Funciones de Orden Superior - HOFs

Una Función de Orden Superior (HOF por sus siglas en inglés) tiene una característica especial: puede recibir otra función como argumento (como parámetro) o puede devolver una función como resultado.

Nos permiten abstraer el comportamiento general (como recorrer una lista) y dejar que la función que pasamos como parámetro decida el comportamiento específico (como qué cálculo matemático aplicar).

*   **Ejemplo conceptual:** La función nativa `map(funcion_a_aplicar, lista_de_datos)` es una HOF porque recibe `funcion_a_aplicar` como parámetro.

## 4. Closures 

Un closure ocurre cuando definimos una función dentro de otra función (función anidada), y esta función interna es capaz de "recordar" y acceder a las variables del entorno donde fue creada (el entorno de la función externa), incluso después de que la función externa haya terminado de ejecutarse.

*   Es como si la función interna guardara en una "mochila" las variables de su función padre para poder usarlas en el futuro.

## 5. Estado Encapsulado y `nonlocal`

En programación funcional pura se evitan las variables globales y los objetos (POO). Sin embargo, a veces necesitamos guardar un registro o un historial (un "estado"). Usamos los **closures** para esto.

Al crear variables en la función externa, estas quedan "protegidas" o encapsuladas. Para que la función interna pueda no solo leer, sino **modificar** esas variables protegidas, utilizamos la palabra reservada `nonlocal`. 

*   **¿Qué hace `nonlocal`?** Le dice a Python: *"Esta variable que voy a modificar no es una variable local de mi función interna, ni tampoco es global. Búscala en la función padre que me envolvió"*. Así logramos persistencia de datos de forma segura y aislada.