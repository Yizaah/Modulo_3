# Input del usuario
nombre = input("¿Cuál es tu nombre? ")              # string
edad = int(input("¿Cuántos años tienes? "))         # int
estatura = float(input("¿Cuál es tu estatura en metros? "))  # float
estudia = input("¿Estás estudiando actualmente? (si/no): ")  # string

# Convertir respuesta a booleano
estudia_bool = estudia.lower() == "si"

# Resumen de datos
print("\nResumen de tu información:")
print("Nombre:", nombre)
print("Edad:", edad)
print("Estatura:", estatura, "m")
print("¿Estudia actualmente?:", estudia_bool)