matriz = [ [10, 15, 20], [3, 7, 14] ]

cantantes = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
   "México": ["Ciudad de México", "Guadalajara", "Cancún"],
   "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
   {"latitud": 8.2588997, "longitud": -84.9399704}
]

#1.1 Cambia el valor 3 en matriz por 6.
print("Matriz original", matriz)
matriz[1][0] = 6
print("Matriz modificada", matriz)

#1.2 Cambia el nombre del primer cantante por "Enrique Martin Morales".

print("Cantantes originales", cantantes)
cantantes[0]["nombre"] = "Enrique Martin Morales"
print("Cantantes modificados", cantantes)

#1.3 En el diccionario ciudades, reemplaza "Cancún" por "Monterrey".

print("Ciudades original",ciudades)
ciudades["México"][2] = "Monterrey"
print("Ciudades modificadas",ciudades)

#1.4 En la lista coordenadas, cambia el valor de "latitud" por 9.9355431.

print("Coordenadas originales", coordenadas)
coordenadas[0]["latitud"] = "9.9355431"
print("Coordenadas modificadas", coordenadas)

#2. Recorrer una lista de diccionarios:  Utiliza estructuras de control para iterar la lista cantantes. Muestra el nombre y país de cada cantante. * BONUS: Presenta cada entrada con el siguiente formato: nombre - [Nombre del cantante], pais - [País]
for cantante in cantantes:
   print(f"nombre - [{cantante["nombre"]}], pais - [{cantante["pais"]}]")

#3 Obtener valores específicos desde una lista de diccionarios:  Utilizando la lista cantantes, imprime por separado todos los valores correspondientes a la clave "nombre". Luego, imprime todos los valores correspondientes a la clave "pais".

for cantante in cantantes:
   print({cantante["nombre"]})
for cantante in cantantes:
   print({cantante["pais"]})

#4 Realiza un recorrido del diccionario que imprima lo siguiente: 
#4.1 La cantidad de elementos en cada lista seguida del nombre de la clave en mayúsculas. Cada elemento de la lista correspondiente, en líneas separadas.

costa_rica = {
   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}
for clave, valor in costa_rica.items(): 
   print((len(valor)), clave.upper())
#4.2 Cada elemento de la lista correspondiente, en líneas separadas.
   for i in valor:
        print(i)


