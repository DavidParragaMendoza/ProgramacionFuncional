
def configurar_notificacion(canal):
    def enviar(mensaje):
        #closure
        print(f"[{canal.upper()}] Enviando: {mensaje}")
    return enviar

# Creamos funciones especializadas usando una HOF
notificar_email = configurar_notificacion("email")
notificar_sms = configurar_notificacion("sms")

notificar_email("Tu código de seguridad es 1234")
notificar_sms("Tu pedido ha llegado")