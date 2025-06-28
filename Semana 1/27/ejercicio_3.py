"""
Define las variables con los siguientes datos:
Precio original de un pantalón: $4599.
Precio original de unos zapatos: $7999.
Porcentaje de descuento para ropa: 20%.
Porcentaje de descuento para calzado: 15%.
Calcula el precio final para cada producto aplicando su respectivo descuento.
Pista: El precio final se calcula como precio_original * (1 - descuento / 100).
Muestra los precios finales en la consola. 
Bonus:
Calcula el ahorro total sumando la cantidad que te ahorraste en cada producto.
Muestra el ahorro total en la consola con el siguiente formato: ¡Ahorraste $ahorro_total en total!
"""

precio_original_pantalon = 4599
precio_original_zapatos = 7999

descuento_ropa = 20
descuento_zapatos = 15

precio_final_ropa = precio_original_pantalon * (1 - descuento_ropa/100)
precio_final_zapatos = precio_original_zapatos * (1 - descuento_zapatos/100)

print(f"El pantalon cuesta $ {precio_final_ropa} (antes ${precio_original_pantalon})")
print(f"Los zapatos cuestan $ {precio_final_zapatos} (antes ${precio_original_zapatos})")

ahorro_zapatos = precio_original_zapatos - precio_final_zapatos
ahorro_ropa = precio_original_pantalon - precio_final_ropa
ahorro_total = ahorro_zapatos + ahorro_ropa
print(f"Ahorraste un total de ${ahorro_total}") 
