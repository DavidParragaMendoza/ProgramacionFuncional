'''
Imagina que estás construyendo un sistema de control y recibes un comando de texto. Queremos ejecutar una respuesta diferente según el texto recibido:
'''
def interpretar_comando(comando): 
    match comando: 
        case "iniciar": 
            return "Sistema iniciado" 
        case "detener": 
            return "Sistema detenido" 
        case "estado": 
            return "Consultando estado" 
        case _: 
            return "Comando no reconocido"



comando: str = interpretar_comando("detener")
print(comando)  # Esto imprimirá: Sistema detenido