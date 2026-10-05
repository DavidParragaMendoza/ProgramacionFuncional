#Primer Funcion de Orden Superior (HOF)

'''
Abstracción del patrón
Si el recorrido es el mismo, podemos pasarlo a una sola función y variar solo la transformación.
'''

def transformarLista(lista, funcion) ->list:
    resultado = []
    for valor in lista:
        resultado.append(funcion(valor))
    return resultado

print(transformarLista([1,2,3,4], lambda x: x * 2))
#salida [2, 4, 6, 8]
print(transformarLista([1,2,3,4], lambda x: x ** 2))
#salida [1, 4, 9, 16]