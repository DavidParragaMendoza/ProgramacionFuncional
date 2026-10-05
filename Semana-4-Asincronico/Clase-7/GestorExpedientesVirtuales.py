from typing import Callable, List, Tuple

# Constante que define el criterio de aprobación
NOTA_MINIMA: float = 7.0


#Función de Orden Superior (HOF). 
#Simplemente recibe una nota y una regla (función lambda) para decidir si pasa o no.

def validarNota(nota: float, criterio: Callable[[float], bool]) -> bool:
    return criterio(nota)

#Crea un espacio seguro (Closure) para el estudiante. 
#Guarda los datos en su propia "burbuja" para no usar variables globales.

def crearExpediente(nombreEstudiante: str) -> Callable[[str, float, int], str]:
    # Nuestro estado encapsulado: una lista de tuplas para el historial y un contador
    registrosAprobados: List[Tuple[str, float, int]] = []
    totalCreditos: int = 0

    def gestorExpediente(materia: str, nota: float, creditos: int) -> str:
        # Permite actualizar las variables que están en la burbuja exterior
        nonlocal registrosAprobados, totalCreditos

        # Usamos la HOF pasándole nuestra regla lambda (nota mayor o igual a 7.0)
        esAprobado: bool = validarNota(nota, lambda n: n >= NOTA_MINIMA)

        if not esAprobado:
            return "Registro rechazado por validación de nota."

        # Guardamos el nuevo registro y sumamos los créditos
        registrosAprobados = registrosAprobados + [(materia, nota, creditos)]
        totalCreditos = totalCreditos + creditos

        # Extraemos solo las notas de los registros usando map() y calculamos el promedio
        sumaNotas: float = sum(map(lambda registro: registro[1], registrosAprobados))
        promedio: float = sumaNotas / len(registrosAprobados)

        return f"Estudiante: {nombreEstudiante} | Promedio: {promedio:.1f} | Créditos: {totalCreditos}"

    # Devolvemos la función interna configurada y lista para usarse
    return gestorExpediente

# ------------------------------------------
# Pruebas de Ejecución Esperada
#-------------------------------------------

# Inicialización
gestor = crearExpediente("David Mendoza")

# Caso 1: Nota insuficiente (Rechazo)
print(gestor("Desenvomiento de Sistema Corporativos", 6.9, 3)) 
# Salida: Registro rechazado por validación de nota.

# Caso 2: Primer registro exitoso
print(gestor("Teste de SOftware", 9.5, 3)) 
# Salida: Estudiante: David Mendoza | Promedio: 9.5 | Créditos: 3

# Caso 3: Segundo registro (Persistencia de créditos: 3 + 3 = 6)
print(gestor("Gerencia de Proyectos", 10.0, 3)) 
# Salida: Estudiante: David Mendoza | Promedio: 9.8 | Créditos: 6

print(gestor("Base de Datos 2", 10.0, 3)) 
# Salida: Estudiante: David Mendoza | Promedio: 9.8 | Créditos: 9

print(gestor("Programacion Funcional", 10.0, 3)) 
# Salida: Estudiante: David Mendoza | Promedio: 9.9 | Créditos: 12