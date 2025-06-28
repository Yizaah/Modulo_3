"""
Ejercicio: Calculadora de Autonomía de Viaje
Objetivo: Crear un script que calcule cuántos kilómetros puede recorrer un auto con un presupuesto determinado para bencina.
Instrucciones:
Define las siguientes variables con los datos proporcionados:
Rendimiento del auto: 12.5 kilómetros por litro.
Precio de la bencina: $1200 por litro.
Presupuesto disponible: $15000.
Realiza los cálculos necesarios:
Calcula cuántos litros de bencina se pueden comprar con el presupuesto.
Calcula la distancia total que se puede recorrer con esos litros.
Muestra el resultado en la consola con el siguiente formato: Con $presupuesto puedes recorrer km_recorridos km!
"""
presupuesto = 15000
precio_bencina = 1200 #por litro
rendimiento = 12.5 #kilometros por litro

litros_comprados = presupuesto / precio_bencina
print (f"Compramos {litros_comprados} litros de bencina")
distancia_recorrida = litros_comprados * rendimiento
print (f"Nos alcanza para andar{distancia_recorrida} KM")