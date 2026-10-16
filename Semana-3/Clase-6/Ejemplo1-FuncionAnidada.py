def externa():
    print("Esta es la función externa.")

    def interna():
        print("Esta es la función interna.")

    return interna  

print("Llamando a la función externa:")
print(externa()) 