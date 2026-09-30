
import numpy as np  
# Importamos la librería con el alias 'np' para escribir menos

# 1. Creamos una lista estándar de Python
notas: list[int] = [10, 8, 7, 9]

# 2. La convertimos en un 'Array' (Arreglo) de NumPy
# Esto le da a la lista "superpoderes" matemáticos
notas_np = np.array(notas)

# 3. Usamos funciones predefinidas de NumPy para ahorrar cálculos manuales

# Calcula el promedio automáticamente
media = np.mean(notas_np)        
# Encuentra el valor más alto de la lista
nota_maxima = np.max(notas_np)   

print(f"Notas registradas: {notas_np}")
print(f"El promedio de notas es: {media}")
print(f"La nota más alta fue: {nota_maxima}")