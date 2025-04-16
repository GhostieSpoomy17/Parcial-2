
# Realizar un menú que presente las siguientes opciones:
# 1. Un saludo. (Al presionar 1)
# 2. Una despedida (Al presionar 2)
# 3. Una edad.
# 4. Opción de salida. (Si es que no se coloca ningún dato válido)

bienvenida = ""

print()
print("Bienvenido al menú. Seleccione una opción pulsando 1, 2 o 3:")
print()

print("1. Saludar.")
print("2. Despedirse.")
print("3. Decir edad.")

print(bienvenida)
print()

seleccion = input(" ")

if seleccion == "1":
    print("¡Hola!")
elif seleccion == "2":
    print("¡Que te vaya bien!")
elif seleccion == "3":
    print("Qué mayorcito.")
else:
    print("Selección inválida. Reintente.")
