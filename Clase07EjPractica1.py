
# EJERCICIO TIPO EXAMEN - CLASE 07


# Solicitar dos números (a y b) a un usuario.
# "a" debe ser el límite inferior y "b" el límite superior, para que el resultado sea un número aleatorio.
# Sacar un porcentaje del resultado según la respuesta del usuario.
# Solicitar al usuario que sume o reste el porcentaje que colocó a su número aleatorio.

print("----------------------------------")

import math

print("Vamos a sacar un número aleatorio en base a tus respuestas.")
print("Vas a crear un rango de números según tus respuestas.")

print()

a = int(input("Dime el primer número que marque el límite inferior: "))
b = int(input("Ahora dime el segundo número, que marque el límite superior: "))

resultado = a <= range <= b

print()

print(f"Tu número aleatorio es {resultado}.")