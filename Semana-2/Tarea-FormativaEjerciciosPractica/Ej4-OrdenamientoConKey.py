'''
4. Ordenamiento con key
Ordena nombres = ["Ana", "Sebastián", "Luz", "Cristóbal"] de la palabra más corta a la más larga. 
Si empatan en longitud, define el orden alfabéticamente.

💡 Pista: Usa una tupla para desempatar: key=lambda n: (len, n).

'''

#lista de nombres
nombres:list[str] = ["Ana", "Sebastián", "Zebastián", "Luz", "Cristóbal", "kristóbal"]

#ordenar la lista
nombresOrdenados = sorted(nombres, key=lambda n: (len(n), n))

#mostrar el resultado
print(nombresOrdenados)
