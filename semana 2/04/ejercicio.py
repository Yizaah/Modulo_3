#variables
cantidad_productos = int(input("Ingrese la cantidad de productos: "))
compras_previas = int(input("¿Cuántas compras ha realizado anteriormente?: "))
es_frecuente = compras_previas > 5
monto_compra = float(input("Ingrese el monto total de la compra ($): "))
es_dia_promocion = input("¿Es día de promoción especial? (SI/NO): ").upper() == "SI"

# Variable para el descuento total
descuento_total = 0

# Condición 1: Si el cliente compra más de 10 productos, obtiene un descuento del 10%.
if cantidad_productos > 10:
    descuento_total += 10

# Condición 2: Si el cliente es frecuente (más de 5 compras previas), se aplica un 5% adicional.
if es_frecuente:
    descuento_total += 5

# Condición 3: Si la compra supera los 500 dólares, se otorga un descuento adicional del 7S%.
if monto_compra > 500:
    descuento_total += 7

# Condición 4: En días de promoción especial, se aplica un 15% adicional.
if es_dia_promocion:
    descuento_total += 15

# Ningún cliente puede obtener un descuento mayor al 30% en total.
if descuento_total > 30:
    descuento_total = 30

# Mostrar resultado
if descuento_total > 0:
    print(f"Opta a un {descuento_total}% de descuento")
else:
    print("No se aplica ningún descuento.")

# precio a pagar
precio_final = monto_compra - (monto_compra * descuento_total / 100)
print(f"Precio a pagar: ${precio_final:.2f}")