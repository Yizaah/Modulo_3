# 1. Imprime "Hola, mundo"

print("Hola, mundo")

# 2. Imprime "Hola, Valeria" con el nombre en una variable

nombre = "Valeria"

print("Hola", nombre) # con una coma

print("Hola "+ nombre) # con un +

# 3. Imprimir "Hola 156!" con el número en una variable

numero = 156

print("Hola", numero) # con una coma

print("Hola "+ str(numero)) # con un + -- este debería arrojar un error!, corrígelo con conversión
print("Hola %d" %(numero))

# 4. Imprimir "Me encanta comer tacos y arepas" con las comidas en variables

comida1 = "tacos"

comida2 = "arepas"

print("Me encanta comer {} y {}" .format(comida1, comida2)) # con .format()

print(f"Me encanta comer {comida1} y {comida2}") # con una cadena f

print("My turn!")

# 1. Imprime "Hello, World"

print("Hello, World")

# 2. Imprime "Hola, Yitzhak" con el nombre en una variable

nombre = "Yitzhak"

print("Hola,", nombre ) # con una coma

print("Hola, "+ nombre ) # con un +

# 3. Imprimir "Hola N° 18!" con el número en una variable

numero = 18

print("Hola, N°", numero,) # con una coma

print("Hola, N° "+ str(numero)) # con un + -- este debería arrojar un error!, corrígelo con conversión
                            # corregido con str

# 4. Imprimir "Me encanta comer completos y sopaipillas" con las comidas en variables

comida1 = "completos"

comida2 = "sopaipillas"

print("Me encanta comer {} y {}" .format(comida1, comida2)) # con .format()

print(f"Me encanta comer {comida1} y {comida2}.") # con una cadena f