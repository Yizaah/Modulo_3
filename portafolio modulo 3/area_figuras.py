import math

def area_cuadrado(lado):
    return lado * lado

def area_rectangulo(base, altura):
    return base * altura

def area_circulo(radio):
    return math.pi * math.pow(radio, 2)  # Usamos math.pi y math.pow

# Menú
print("Calculadora de áreas:")
print("1. Cuadrado")
print("2. Rectángulo")
print("3. Círculo")

opcion = input("Elige una opción (1-3): ")

if opcion == "1":
    lado = float(input("Ingresa el lado del cuadrado: "))
    print("Área del cuadrado:", area_cuadrado(lado))

elif opcion == "2":
    base = float(input("Ingresa la base: "))
    altura = float(input("Ingresa la altura: "))
    print("Área del rectángulo:", area_rectangulo(base, altura))

elif opcion == "3":
    radio = float(input("Ingresa el radio: "))
    print("Área del círculo:", area_circulo(radio))

else:
    print("Opción no válida.")