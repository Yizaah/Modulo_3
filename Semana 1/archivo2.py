"""
Ingresar numero por teclado y mostrar si es par o impar.
"""
numero = int(input("Ingrese un numero: "))
print("El numero ingresado:", numero)
operacion = numero % 2 
print("El resultado de la operacion es:", operacion)
if operacion == 0:
    print("El numero es par")
if operacion == 1:
    print("El numero es impar")