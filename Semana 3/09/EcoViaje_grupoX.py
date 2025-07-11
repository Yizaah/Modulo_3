# Lista de excursiones con nombre y cupos disponibles
excursiones = [
    {"nombre": "Parque Nacional Torres del Paine", "cupos": 3, "reservas": []},
    {"nombre": "Parque Nacional Conguillío", "cupos": 1, "reservas": []},
    {"nombre": "Reserva Nacional Ñuble", "cupos": 8, "reservas": []},
    {"nombre": "Reserva Nacional Malalcahuello", "cupos": 3, "reservas": []}
]

# Función para mostrar excursiones y cupos disponibles
def mostrar_excursiones():
    print("\nExcursiones disponibles:")
    for i, excursion in enumerate(excursiones, start=1):
        print(f"{i}. {excursion['nombre']} - Cupos disponibles: {excursion['cupos']}")

# Función para mostrar las reservas realizadas
def mostrar_reservas():
    print("\nReservas actuales:")
    for excursion in excursiones:
        print(f"- {excursion['nombre']}: {', '.join(excursion['reservas']) if excursion['reservas'] else 'Sin reservas'}")

# Ciclo principal para reservas
while True:
    mostrar_excursiones()
    nombre = input("\nIngresa tu nombre (o 'salir' para terminar): ")
    
    if nombre.lower() == "salir":
        print("Programa finalizado.")
        break

    try:
        opcion = int(input("Ingresa el número de la excursión que deseas reservar: "))
        if opcion < 1 or opcion > len(excursiones):
            print("Número inválido. Intenta de nuevo.")
            continue
    except ValueError:
        print("Debes ingresar un número válido.")
        continue

    seleccion = excursiones[opcion - 1]

    if seleccion["cupos"] == 0:
        print("Lo sentimos, esta excursión ya no tiene cupos.")
        continue

    # Guardar la reserva
    seleccion["reservas"].append(nombre)
    seleccion["cupos"] -= 1
    print(f"\n Reserva confirmada para {nombre} en '{seleccion['nombre']}'")

    # Mostrar reservas actuales
    mostrar_reservas()