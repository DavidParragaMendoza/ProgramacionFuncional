# **Problema del billón de dólares**

**¿Por qué ocurre el error tradicionalmente?**

En la programación tradicional, solemos crear estructuras generales donde algunos campos se dejan vacíos (`None`), y luego nos vemos obligados a hacer **programación defensiva** plagada de controles como `if dato is not None:` para evitar fallos. Si olvidas un solo `if`, el programa colapsa inesperadamente en ejecución.

---

### La solución funcional: "Hacer lo ilegal, irrepresentable"

<aside>
💡

Diseñamos la arquitectura usando **Tipos Suma** y **Tipos Producto** para que una combinación inválida de datos sea **mecánicamente imposible de crear**.

</aside>

---

### Ejemplo: La respuesta de un servidor

Imagina que le pides la información de un usuario a una base de datos. La respuesta puede salir bien o fallar por un error de conexión.

#### ❌ La forma tradicional (causante del error `NoneType`):

```python
# Usamos un solo diccionario o clase donde todo puede ser None
respuesta = {"exito": False, "usuario": None, "error": "Conexión fallida"}

# Si te confías en otra parte del código y lees el usuario directamente:
print(respuesta["usuario"].upper())
# ¡BOOM! AttributeError: 'NoneType' object has no attribute 'upper'
```

Aquí el diseño de datos permitió que existiera una respuesta fallida pero manteniendo la variable `usuario` apuntando a `None`.

---

### Concepto 2: Los bloques de construcción (Tipos Producto y Tipos Suma)

Para modelar la información de forma segura, nos apoyamos en dos bloques de construcción esenciales:

1. **Tipos Producto (La relación "Y"):**
    - Agrupa varios campos de datos que **deben existir todos al mismo tiempo**.
    - Ejemplo cotidiano: Un **`Usuario`** tiene un ID **Y** un Nombre **Y** un Correo. Una coordenada geográfica necesita Latitud **Y** Longitud. Si falta alguno, la estructura está incompleta.
2. **Tipos Suma (La relación "O"):**
    - Define una estructura que representa **una opción de entre varias alternativas mutuamente excluyentes**.
    - *Ejemplo cotidiano:* La respuesta de un servidor de red puede ser un **`Éxito`** **O** un **`Error,`** no puede ser ambas a la vez. Una figura geométrica puede ser un **`Círculo`** **O** un **`Rectángulo` O** un **`Triángulo`**.

---

### Concepto 3: Pattern Matching Estructural (Evaluar por la "forma")

Normalmente, para procesar datos complejos, escribimos largas cadenas de `if/elif` comprobando manualmente tipos, longitudes o contenidos.

El **Pattern Matching Estructural** nos permite tomar decisiones evaluando directamente la **forma física o patrón del dato**. 

En lugar de hacer múltiples preguntas imperativas, declaramos la estructura esperada por ejemplo: 

<aside>
💡

Si es una tupla de dos elementos con la palabra “login” y un nombre y el sistema desempaca y extrae la información automáticamente si la forma coincide.

</aside>

---

### Resumen en una frase

- **Tipos como Arquitectura:** Definen qué formas de datos **tienen permitido existir** en el sistema.
- **Pattern Matching:** Reconoce la **forma** del dato recibido y **desarma su contenido** para procesarlo directamente.

---

#### ✅ La forma funcional (Tipos Suma + Pattern Matching):

Modelamos la respuesta expresando que solo existen dos formas cerradas y válidas:

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Exito:
    usuario: str  # Si es Éxito, OBLIGATORIAMENTE lleva el nombre del usuario

@dataclass(frozen=True)
class Error:
    codigo: int   # Si es Error, OBLIGATORIAMENTE lleva el código numérico

# Tipo Suma: La respuesta es un Exito O un Error (nunca ambos, nunca None)
Resultado = Exito | Error
```

Al procesar este resultado con **Pattern Matching**, la estructura te guía de forma segura:

```python
def procesar_respuesta(res: Resultado):
    match res:
        case Exito(usuario):
            # Aquí es IMPOSIBLE que 'usuario' sea None, la estructura lo garantiza
            print(f"Usuario obtenido: {usuario.upper()}")
        case Error(codigo):
            # Aquí ni siquiera existe la variable 'usuario', no hay riesgo de error
            print(f"Error detectado código: {codigo}")
```

---

### ¿Por qué esto resuelve el problema?

1. **Estados ilegales imposibles:** No puedes crear un **`Exito`** sin usuario ni un **`Error`** con datos corruptos.
2. **Desaparecen los `None` sueltos:** Cada variante (`Exito` o `Error`) almacena **únicamente** la información que requiere.
3. **El código es seguro por construcción:** En el bloque `case Error`, el lenguaje ni siquiera te permite intentar leer un nombre de usuario porque sabe que esa propiedad no existe en esa forma.

---