
def log(func):
    def envoltura(*args):
        print(f"----------- EJECUTANDO [{func.__name__}] ----------------")
        return func(*args)
    return envoltura

@log
def iniciarSesion(usuario):
    print(f"Sesión iniciada por {usuario}")

iniciarSesion("Pepe Pecas")
