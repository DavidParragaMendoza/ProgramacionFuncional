'''
Idea
Podemos encadenar HOFs para expresar una transformacion mas completa sobre los datos.

sintaxis de la composicion de HOFs
map(funcion, filter(funcion, iterable))
¿Que se ejecutara primero el map o el filter?
se ejecutara primero el filter, ya que es el que esta mas adentro de la expresion.

Es exactamente el mismo principio que usas en matemáticas al resolver una ecuación como 2 * (3 + 5): tienes que resolver primero el paréntesis más interno para saber qué número vas a multiplicar por el 2.
'''

notas = [5,8,9,6,10]

resultado = list(
    map(lambda n: n + 1,
        filter(lambda n: n >= 7, notas))
)

print(resultado)