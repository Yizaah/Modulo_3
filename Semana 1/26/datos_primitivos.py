"""
Características de los datos primitivos en Python:
1. **Inmutabilidad**: No se pueden cambiar una vez creados.
2. **Simplicidad**: Representan valores simples y no tienen métodos asociados.
3. **Eficientes**: Ocupan menos memoria y son más rápidos de procesar.

Numéricos: Int, Float, Complex
Texto: Str
Booleanos: Bool, True y False
"""

#Booleanos
notificaciones_activadas = False
if (notificaciones_activadas):
    print("Notificaciones activadas")

es_fin_de_semana = False
#el if esepra siempre un valor true
if (es_fin_de_semana):
    print("Es fin de semana")
else:
    print("Toca trabajar")

#Numéricos

edad = 29
temperatura = 5

#Cadenas de texto

nombre = "Juan"
mensaje = "Y que pasa realmente"

#None ausencia del valor

resultado = None
print("id de variable resultado:", id(resultado))
#id() devuelve un  identificador unico para un objeto, que representa su direción en memoria.
suma = 1+1
resultado = suma
print("id de variable resultado al modificar:", id(resultado))
print(resultado)
