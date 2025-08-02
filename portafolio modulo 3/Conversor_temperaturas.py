# Imput para que usuario ingrese una T° en grados Celsius
print("Hola!, este es un conversor de temperatura: Celsius a Fahrenheit")
celsius = float(input("Ingresa la temperatura en grados Celsius: "))

# Convierte a Fahrenheit usando la fórmula: F = C * 9/5 + 32
fahrenheit = celsius * 9/5 + 32

# Muestra el resultado
print("La temperatura en Fahrenheit es:", fahrenheit)