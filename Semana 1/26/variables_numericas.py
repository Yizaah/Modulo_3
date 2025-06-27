import math

#Ejemplo 1: Calcular el área de unt triángulo

base = 6.6
altura = 8.2

area=(base * altura)/2
area= round(area)
print(area)


distancia_norte= 30
distancia_este= 40

distancia_directa= math.hypot(distancia_norte,distancia_este)
print("la distancia recorrida por el árbitro es:", distancia_directa)


#math.ceil para redondear hacia arriba. math.floor para redondear hacia abajo. trunk corta los decimales al que uno le dice. 

velocidad = 6.3 # MB/s
tiempo = 60 #segundos
mb_descargados = math.floor(velocidad * tiempo)
print (f"descargaste {mb_descargados} MB en {tiempo} segundos ({velocidad*tiempo}).")

