import random

print('¡Bienvenido a Python!')

print('Este es un bucle que imprime 10 veces')
for num in range(1, 11):
    print(f'num es: {num}')

semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
dia = random.choice(semana)

print(f'Hoy es: {dia}')

if dia == 'Lunes':
    print('¡Comenzamos la semana con toda la actitud!')
if(dia == 'Viernes'):
    print('¡Listos para un fin de semana!')
if(dia == 'Miércoles'):
    print('¡Mitad de semana, ya casi es viernes!')
if(dia == 'Jueves'):
    print('¡Casi es viernes, ánimo!')
if(dia == 'Martes'):
    print('¡El día mas lejos del próximo Lunes!')
else:
    print('¡Descansa we')