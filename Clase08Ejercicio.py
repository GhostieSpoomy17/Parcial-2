
# EJERCICIO TIPO EXAMEN - CLASE 08:


# Necesitamos generar un programa en Python que permita generar números aleatorios 
# dentro de un rango definido por el usuario y ajustarlos dividiéndolos entre 4.

# Luego el usuario, debe dar otro número para dividirlo nuevamente entre un máximo de 3 intentos.

# Condiciones del juego:

# Ingreso de datos.
# A: El usuario ingresa dos números ENTEROS, que representan el rango numérico.
# B: El primer número debe ser inferior al segundo número.

# Generación del número aleatorio.
# A: Se dará un número aleatorio dentro del rango ingresado
# B: El número se ajusta dividiéndolo entre 4 y redondeándolo al múltiple de 4 más cercano.

# Intentos del usuario.
# A: Si el usuario acierta, se muestra el mensaje "Felicitaciones, adivinaste al primer intento."
# B: Segundo intento. Si el usuario no acierta, se le indicará si el número es mayor o menor.
# C: Tercer y último intento. Si no acierta, se le devuelve a dar una pista.
# D: Resultado final. Si no acierta en los 3 intentos, el programa muestra el mensaje "Perdiste. El número es incorrecto."



import random


print()

print("-----------------------------")

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
        print("¡Felicidades! Acertaste a la primera, te ganasta el premio.")
    else:
        print("Incorrecto. Te daré una pista.")
        if resultado < redondeo:
            print("El resultado es mayor que su respuesta.")
        else:
            print("El resultado es menor a su respuesta.")