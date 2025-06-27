#Las conversiones son como disfraces int(), str(), etc.

entero_a_decimal = float(123)

decimal_a_entero = int(22.5)

entero_a_complejo = complex(35)

print(entero_a_decimal) #Imprime: 123.0

print(decimal_a_entero) #Imprime: 22

print(entero_a_complejo) #Imprime: (35+0j)


#
edad = 28
edad_txt= str(edad)
print(f"Tengo {edad_txt}")

#de str a int (texto a numero)
puntaje = "70"
bonus = float(puntaje) *1.1
print("Tu puntaje final es:", + bonus)

#de float a int. Ojo que aqui se pierde y funciona como trunc
peso = 2.9
peso_entero = int(peso)
print(peso_entero)

#booleano

print(bool(0))
print(bool("Hola"))
print(bool(-1))