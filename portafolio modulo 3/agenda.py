# Agenda de contactos simple en diccionario
agenda = {}

# Agregar tres contactos
for i in range(3):
    nombre = input(f"Ingrese el nombre del contacto {i + 1}: ")
    telefono = input(f"Ingrese el número de teléfono de {nombre}: ")
    agenda[nombre] = telefono  # clave: nombre, valor: teléfono

# Mostrar los contactos guardados
print("\nAgenda de contactos:")
for nombre, telefono in agenda.items():
    print(f"{nombre}: {telefono}")