#1. Actualizar valores en diccionarios y listas

matriz = [ [10, 15, 20], [3, 7, 14] ]

cantantes1 = [
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

#1.1 Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]

print("Matriz original", matriz)
matriz[1][0] = 6
print("Matriz modificada", matriz)

#1.2 Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”

print("Cantantes originales", cantantes1)
cantantes1[0]["nombre"] = "Enrique Martin Morales"
print("Cantantes modificados", cantantes1)

#1.3 En ciudades, cambia “Cancún” por “Monterrey”

print("Ciudades originales", ciudades)
ciudades["México"][2] = "Monterrey"
print("Ciudades modificadas", ciudades)

#1.4 En las coordenadas, cambia el valor de “latitud” por 9.9355431

print("Coordenadas viejas", coordenadas)
coordenadas[0]["latitud"] = 9.9355431
print("Nuevas coordenadas", coordenadas)


#2. Iterar a través de una lista de diccionarios Crea la función iterarDiccionario(lista) que reciba una lista de diccionarios y recorra cada diccionario de la lista e imprima cada llave y el valor correspondiente. Por ejemplo:

cantantes2 = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]
#Imprime "nombre": "Ricky Martin", "pais": "Puerto Rico" (está bien si lo imprime en líneas separadas)
#BONUS: Que aparezcan en este formato:
"""
nombre - Ricky Martin, pais - Puerto Rico
nombre - Chayanne, pais - Puerto Rico
nombre - José José, pais - México
nombre - Juan Luis Guerra, pais - República Dominicana
"""
def iterarDiccionario(cantantes2):
    for cantante in cantantes2:
        print(f'\nnombre - "{cantante["nombre"]}", pais - "{cantante["pais"]}"')
iterarDiccionario(cantantes2)

#3 Obtener valores de una lista de diccionarios Crea la función iterarDiccionario2(llave, lista) que reciba una cadena con el nombre de una llave y una lista de diccionarios. 
# La función debe imprimir el valor almacenado para esa clave de cada diccionario que se encuentra en la lista. 
# Por ejemplo, iterarDiccionario2(“nombre”, cantantes) debe de imprimir:
"""
Ricky Martin
Chayanne
José José
Juan Luis Guerra
Otro ejemplo: iterarDiccionario2(“pais”, cantantes) debe de imprimir:
Puerto Rico
Puerto Rico
México
República Dominicana
"""
def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        print (f'\n{diccionario[llave]}')
iterarDiccionario2("nombre", cantantes2)
iterarDiccionario2("pais", cantantes2)



# 4. Iterar a través de un diccionario con valores de lista Crea una función imprimirInformacion(diccionario) que reciba un diccionario en donde los valores son listas.
#  La función debe imprimir el nombre de cada clave junto con el tamaño de su lista y seguido de esto los valores de la lista para esa clave. Por ejemplo:

costa_rica = {
   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

#imprime:
"""
4 CIUDADES
San José
Limón
Cartago
Puntarenas

5 COMIDAS
gallo pinto
casado
tamales
chifrijo
olla de carne
"""
def imprimirInformacion(diccionario):
    for clave in diccionario:
        print(f"{len(diccionario[clave])} {clave.upper()}")
        for valor in diccionario[clave]:
            print(valor)
        print()

imprimirInformacion(costa_rica)