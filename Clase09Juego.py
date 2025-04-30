
# EJERCICIO TIPO EXAMEN - CLASE 09 - ADIVINANZA:


# Desarrolla un programa en Python que permita generar un número aleatorio dentro de un rango definido por el usuario y ajustarlo dividiéndolo entre 4.
# Luego, el usuario debe adivinar el número en un máximo de intentos de 3.

# CONDICIONES DEL JUEGO:

# 1. INGRESO DE DATOS:
# a) El usuario ingresa 2 números enteros que representan el rango numérico.
# b) El primer número debe ser menor al segundo.

# 2. GENERACIÓN DE NÚMEROS ALEATORIOS:
# a) Se elige un número aleatorio dentro del rango ingresado.
# b) El número se ajusta dividiéndolo entre 4 y redondeándolo al múltiplo de 4 más cercano.

# 3. INTENTOS DEL USUARIO:
# a) Primer intento: Si el usuario acierta, se muestra un mensaje de felicitación.
# b) Segundo intento: Si el usuario falla, se le indica si su número es mayor o menor al resultado.
# c) Tercer intento: Si no acierta nuevamente, se le da otra pista.
# d) Resultado final: Si no acierta en los 3 intentos, el programa muestra un mensaje de derrota. Se señala el número correcto.


import random

print("--------------------------------")
print()

print("Este juego consiste en acertar el número del resultado que será aleatorio dependiendo")
print("de su respuesta. Usted necesita ingresar dos números que sirvan como límites")
print("y se generará ese número aleatorio.")

print()

print("Ese nuevo número se dividirá entre 4 y se redondeará al múltiple de 4 más cercano.")
print("Si usted acierta el número que dió como resultado, se ganará un premio.")
print("Solo se permiten 3 intentos. Buena suerte.")

print()

while True:
    limInf = int(input("Ingrese límite inferior: "))
    limSup = int(input("Ingrese límite superior: "))
    if limInf > limSup:
        print()
        print("Limite inferior no puede ser mayor que limite superior.")
        print()
    else:
        break

print()
        
aleatorio = random.randint(limInf, limSup)
print ("Su número aleatorio es:", aleatorio)

print()

division4 = aleatorio / 4
redondeo = int(round(division4, 4))

while True:
    resultado = int(input("Realice el cálculo. ¿Cuál es el resultado? "))
    if resultado == redondeo:
        print("¡Felicidades! Acertaste a la primera, te ganaste el premio.")
    else:
        print("Incorrecto. Te daré una pista.")
        if resultado < redondeo:
            print("El resultado es mayor que su respuesta.")
        else:
            print("El resultado es menor a su respuesta.")
            if resultado != redondeo:
