cajonera = ["pantalones", "camisetas", "calcetines"]

print(cajonera[0]) #Pantalones
print(cajonera[1]) #Camisetas
print(cajonera[2]) #Calcetines

camisetas = cajonera[1]

cajonera[1] = "sueters" #cambiamos el valor del cajon del indice 1, 

print(cajonera)

# Ahora si queremos agregar, se hace al final.

cajonera.append(camisetas)
print(cajonera)


