"""
Ejercicio: Calculadora de Ganancias Netas de una Frutería
Objetivo: Escribir un script en Python para calcular la ganancia neta de una frutería, considerando ingresos y costos.
Instrucciones:
1. Define las variables para los precios, costos y cantidades vendidas:
    - Precios de Venta: Manzanas: $950/kg, Naranjas: $1300/kg.
    - Costos de Compra: Manzanas: $600/kg, Naranjas: $850/kg.
    - Cantidades Vendidas: Manzanas: 10 kg, Naranjas: 15 kg.
    - Costos Fijos del día: $5000.
2. Calcula los ingresos totales por la venta de ambas frutas.
3. Calcula los costos totales (costo de la fruta + costos fijos).
4. Calcula la ganancia neta (ingresos - costos).
5. Muestra un resumen detallado en la consola.
"""

precio_manzana = 950
precio_naranja = 1300
kilos_manzana_vendidos = 10
kilos_naranja_vendidos = 15

costo_manzana = 600 * (kilos_manzana_vendidos)
costo_naranja = 850 * (kilos_naranja_vendidos)
costo_fijo = 5000

ganancia_manzana = precio_manzana * kilos_manzana_vendidos
ganancia_naranja = precio_naranja * kilos_naranja_vendidos
ganancia_bruta = ganancia_naranja + ganancia_manzana
costo_total = costo_fijo + costo_naranja + costo_manzana

ganancia_neta = (f"Entre lo que ganamos y lo que invertimos, sacamos {ganancia_bruta - costo_total}")

print(f"ganaste {ganancia_neta} en total! Wen trabajo")

