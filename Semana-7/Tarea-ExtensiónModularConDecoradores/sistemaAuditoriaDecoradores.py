# Sistema de Auditoría y Control de Roles
# Tema 3.3: Decoradores y Metaprogramación Funcional
from functools import wraps
import sys

# Evita errores de consola en Windows al imprimir emojis
sys.stdout.reconfigure(encoding="utf-8")

# Constante global del sistema
ROL_ADMIN = "administrador"


# 1. DECORADOR SIMPLE: AUDITORÍA DE LOGS
def auditarEjecucion(func):
    """
    Decorador que registra en consola el nombre de la función que se ejecuta.
    Conserva los metadatos de la función origen mediante functools.wraps.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Registro de auditoría antes de ejecutar la lógica
        print(f"[AUDITORÍA] Ejecutando la función: {func.__name__} con argumentos {args}")
        resultado = func(*args, **kwargs)
        return resultado
    return wrapper


# 2. DECORADOR CON PARÁMETROS: RESTRICCIÓN DE ROLES
def requerirRol(rolPermitido: str):
    """
    Decorador con parámetros que valida si el rol del usuario coincide
    con el permitido. El rol viaja dentro de los kwargs del cliente.
    """
    def decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Extraemos el rol del usuario invocador desde los kwargs
            rolUsuario = kwargs.get('rolUsuario', 'invitado')

            if rolUsuario != rolPermitido:
                print(f"[SEGURIDAD] Acceso denegado. Se requiere rol: '{rolPermitido}'. Usuario actual es '{rolUsuario}'.")
                return None

            # El rol coincide: se da paso a la función original
            return func(*args, **kwargs)
        return wrapper
    return decorador


# APLICACIÓN DE MÚLTIPLES DECORADORES
# La auditoría queda arriba para registrar también los accesos denegados
@auditarEjecucion
@requerirRol(ROL_ADMIN)
def crearUsuario(nombreUsuario: str, rolUsuario: str):
    print(f"[Negocio] Éxito: El usuario '{nombreUsuario}' ha sido guardado en la base de datos.")
    return True


# CASOS DE PRUEBA
print("--- CASO 1: Intento de ejecución con rol no autorizado ---")
crearUsuario("Anthony Pachay", rolUsuario="docente")

print("\n--- CASO 2: Ejecución con privilegios válidos ---")
crearUsuario("Carlos Patiño", rolUsuario="administrador")

# Verificación de preservación de metadatos con functools.wraps
print("\n--- VERIFICACIÓN DE METADATOS ---")
print(f"Nombre de la función decorada: {crearUsuario.__name__}")
