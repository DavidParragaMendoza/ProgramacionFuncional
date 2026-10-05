#El ranking del videoJuego

# Imaginen que trabajan en el equipo del servidor de un juego online. El servidor les devuelve esta lista de jugadores, y el disenador del juego pide: mostrar el ranking de los jugadores conectados, calculando su poder real como puntos x nivel, del más fuerte al más débil

jugadores = [
    {"nombre": "Shadow99", "puntos": 2450, "nivel": 12, "conectado": True},
    {"nombre": "xXProXx", "puntos": 3200, "nivel": 18, "conectado": True},          
    {"nombre": "Luna", "puntos": 4200, "nivel": 16, "conectado": True},
    {"nombre": "Kaito", "puntos": 5100, "nivel": 20, "conectado": False},
    {"nombre": "Aria", "puntos": 3800, "nivel": 15, "conectado": True},
    {"nombre": "Leo", "puntos": 1200, "nivel": 8, "conectado": True},
]
'''
#lista de los jugadores
listaJugadores = list(
    filter(lambda jugador: jugador["conectado"] ==True, jugadores)
)
print("Jugadores conectados:")
for jugador in listaJugadores:
    print(f"Nombre: {jugador['nombre']}")

#calulando su poder real
listaPoderReal = list(
    map(lambda jugador: { "nombre": jugador["nombre"], "poder_real": jugador["puntos"] * jugador["nivel"]}, listaJugadores)
)
print("Poder real de los jugadores:")
for jugador in listaPoderReal:
    print(f"Nombre: {jugador['nombre']}, Poder Real: {jugador['poder_real']}")
'''


ranking = sorted(
    map(lambda jugador: { "nombre": jugador["nombre"], "poder_real": jugador["puntos"] * jugador["nivel"]}, 
        filter(lambda jugador: jugador["conectado"] ==True, jugadores)),
    key=lambda jugador: jugador["poder_real"], reverse=True

)
print("Ranking de jugadores conectados:")
for jugador in ranking:
    print(f"Nombre: {jugador['nombre']}, Poder Real: {jugador['poder_real']}")