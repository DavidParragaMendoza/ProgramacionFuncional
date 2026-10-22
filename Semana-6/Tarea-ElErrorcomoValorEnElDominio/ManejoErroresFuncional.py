from dataclasses import dataclass
from typing import Any, Callable

# Constantes de mensajes del dominio en MAYÚSCULAS
MENSAJE_EXITO: str = "OK"
MENSAJE_ERROR_CERO: str = "No podemos dividir para 0"
    

@dataclass
class Response:
    status: bool
    data: Any = None
    message: str = ""

    # REQUISITO 1: Functor que transforma 'data' de forma segura si el estado es exitoso
    def map(self, func: Callable[[Any], Any]) -> 'Response':
        if not self.status:
            return self
        return Response(True, func(self.data), self.message)

    # REQUISITO 2: Bifurcación declarativa final según el estado del contenedor
    def match(self, onSuccess: Callable[[Any], None], onFailure: Callable[[str], None]) -> None:
        if self.status:
            onSuccess(self.data)
        else:
            onFailure(self.message)


# Función pura que modela el error como un valor legítimo del dominio
def dividir(valorA: float, valorB: float) -> Response:
    if valorB == 0:
        return Response(False, None, MENSAJE_ERROR_CERO)
    return Response(True, valorA / valorB, MENSAJE_EXITO)


# --- ZONA DE PRUEBA Y CONSUMO DECLARATIVO ---
# REQUISITO 3: Flujo continuo sin sentencias 'if/else' en el consumo

# Ejemplo 1: Transformación segura multiplicando el resultado por 100 (.map)
RESULTADO_TRANSFORMADO: Response = dividir(10.0, 2.0).map(lambda x: x * 100)
print(f"Resultado final mapeado: {RESULTADO_TRANSFORMADO}")

# Demostración obligatoria de la rúbrica: Comportamiento seguro de .map ante división para 0
RESULTADO_SEGURO_FALLIDO: Response = dividir(5.0, 0.0).map(lambda x: x + 10)
print(f"Mapeo seguro sin excepción: {RESULTADO_SEGURO_FALLIDO}")

# Ejemplo 2: Bifurcación declarativa final del flujo (.match)
dividir(2.0, 0.0).match(
    onSuccess=lambda data: print(f"Éxito en el sistema: {data}"),
    onFailure=lambda msg: print(f"Fallo controlado: {msg}")
)