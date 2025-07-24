"""


e sean múltiplos de multiplo. Por ejemplo: si numInicial = 3, numFinal = 10, y multiplo = 2, el bucle debería de imprimir 4, 6, 8, 10 (en líneas sucesivas).
 

i=0
while i < 101:
    print(i)
    i += 1

for p in range(2, 501, 2):
    print(p)

a=1
for a in range (1,101):

    if a % 10 == 0:
        print("baby")
    elif a % 5 == 0:
        print("ice ice")
    else:
        print(a)
    

b =0
suma_total = 0
for b in range (0, 500000, 2):
    suma_total += b
    print(suma_total)

for c in range (2024, 0, -3):w
    print(c)
"""
numInicial = 3
numFinal = 10
multiplo = 2

for x in range(numInicial, numFinal):
    if x % multiplo == 0:
        print(x)