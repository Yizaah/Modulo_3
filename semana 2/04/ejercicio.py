
#variables
cantidad_productos = int(input("Ingrese la cantidad de productos: "))
es_frecuente = input("¿Es cliente frecuente? (S/N): ").upper() == "S"
monto_compra = float(input("Ingrese el monto total de la compra ($): "))
es_dia_promocion = input("¿Es día de promoción especial? (S/N): ").upper()

# Variable para el descuento total
descuento_total = 0

# Condición 1: más de 10 productos → 10%
if cantidad_productos > 10:
    descuento_total += 10

# Condición 2: cliente frecuente → 5%
if es_frecuente:
    descuento_total += 5

# Condición 3: monto superior a $500 → 7%
if monto_compra > 500:
    descuento_total += 7

# Condición 4: día de promoción → 15%
if es_dia_promocion == "S":
    descuento_total += 15

# Límite máximo de descuento
if descuento_total > 30:
    descuento_total = 30

# Mostrar resultado
print(f"Opta a un {descuento_total}% de descuento")

# Salida controlada si no se aplica nada
if descuento_total == 0:
    print("No se aplica ningún descuento.")

# precio a pagar
precio_final = monto_compra - (monto_compra * descuento_total / 100)
print(f"Precio a pagar con descuento: ${precio_final:.2f}")