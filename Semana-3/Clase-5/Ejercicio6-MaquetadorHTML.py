
def generadorEtiquetas(etiqueta):
    return lambda texto: f"<{etiqueta}>{texto}</{etiqueta}>"

h1 = generadorEtiquetas("h1")
negrita = generadorEtiquetas("b")

print(h1("Titulo de la página"))
print(negrita("texto importante"))
