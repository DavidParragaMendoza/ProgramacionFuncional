'''
2- Transformación pura con map
De la lista ["hola", "programación", "sol", "universidad"], obtén una lista con la longitud numérica de cada palabra.

💡 Pista: Puedes pasar directamente la función len a map. Recuerda envolver todo con list(...).

'''

#lista de palabras
listaPalabras:list[str] = ["hola", "programación", "sol", "universidad"]

#obtener la longitud de cada palabra
longitudPalabras = list(
    map(len, listaPalabras))

#mostrar el resultado
print(longitudPalabras)