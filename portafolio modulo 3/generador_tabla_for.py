numero = int(input("Número para ver su tabla de multiplicar: "))

print(f"\nApréndete la tabla del {numero}:")

for i in range(1, 11):  # del 1 al 10
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")