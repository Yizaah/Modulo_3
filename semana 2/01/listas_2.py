#manipular listas

cajonera = ["pantalones", "camisetas", "calcetines"]

camisetas = cajonera[1]
cajonera[1] = "sueters" #cambiamos el valor del cajon del indice 1, 
print(cajonera)

# Ahora si queremos agregar, se hace al final.
cajonera.append(camisetas)
print(cajonera)

#insertar en un posición especifica, aludiendo al indice donde lo quiero.
cajonera.insert(1, "vestidos")
cajonera.insert(7, "vestidos")
cajonera.insert(2, "vestidos")
cajonera.insert(3, "vestidos")
print(cajonera)

#remove. elimina la primera ocurrencia de un valor.
cajonera.remove("vestidos")
print(cajonera)

#pop borra el ultimo elemento, viene con un -1 por defecto

cajonera.pop()
print(cajonera)

cajonera.pop(1)
print(cajonera)

lista_compras = ['botas', 'bufanda', 'guantes']
cajonera.append(lista_compras) #agrega lista
print(cajonera)
print(lista_compras[2])
print(cajonera[5]) #la lista entera es solo un elemento
print(type(lista_compras[2])) #tipo de dato dentro de la lista
cajonera[5].remove("guantes") # accedo a la lista como 1 elemento de la cajonera, y desde ahi elimino los guantes
print(cajonera)

cajonera[5].insert(1,"paraguas")
print(cajonera)