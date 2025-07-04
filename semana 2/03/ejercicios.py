# set con los días de la semana
dias = {"lunes", "martes", "miércoles", "jueves", "viernes", "sábado"}
dias.add("domingo")

# Eliminar un día cualquiera
dias.discard("lunes")  # No da error si no existe, el remove da error si no existe.

print(dias)
print("lunes" in dias)

lista1 = [1, 2, 3, 4, 5, 5]
lista2 = [4, 5, 6, 7, 8]

set1 = set(lista1)
set2 = set(lista2)

print(set1 & set2)
print(set1 ^ set2)

# Alimentos favoritos de un grupo de estudiantes
estudiantes = {"pizza", "hamburguesa", "sushi", "tacos", "ensalada"}

# Alimentos favoritos de un grupo de deportistas
deportistas = {"pollo", "ensalada", "sushi", "batidos", "huevos"}

# 1. Alimentos comunes en ambos grupos (intersección)
comunes = estudiantes & deportistas
print("Comunes:", comunes)

# 2. Alimentos únicos de los estudiantes (diferencia)
solo_estudiantes = estudiantes - deportistas
print("Solo estudiantes:", solo_estudiantes)

# 3. Alimentos únicos de los deportistas (diferencia)
solo_deportistas = deportistas - estudiantes
print("Solo deportistas:", solo_deportistas)