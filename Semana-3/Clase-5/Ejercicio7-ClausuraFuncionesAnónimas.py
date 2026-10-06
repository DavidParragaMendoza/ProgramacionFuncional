# Fábrica de multiplicadores

def fabMultiplicador(multi):
    return lambda x: x * multi

por2 = fabMultiplicador(2)
por3 = fabMultiplicador(3)

print(por2(2))
print(por2(4))
print(por2(6))

