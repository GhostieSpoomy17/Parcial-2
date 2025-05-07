# EJERCICIO TIPO EXAMEN - CLASE 11 - ADIVINANZA


# Desarrolla un programa en Python que permita ingresar dos números enteros que indiquen un rango numérico. El primer valor debe ser menor que el segundo.
# El programa generará un número aleatorio dentro de ese rango. Luego, el usuario intentará adivinar el número generado en tres intentos.

# Si el usuario adivina en el primer intento, el programa mostrará el mensaje: "Felicitaciones, adivinaste en el primer intento."
# Sino acierta en el primer intento, el programa indicará si el número es mayor o menor que el intento del usuario.
# En el segundo intento, si el usuario no acierta, se volverá a indicar si el número es mayor o menor.
# Si el usuario no acierta en el tercer intento, el programa mostrará el mensaje: "Perdiste, el número era [número]."


import random

print()
print("-----------------------------")

print("Usted va a dar números según se le indique para recibir un número aleatorio y un porcentaje. Al tener todos estos datos,")
print("va a decidir si realizar una suma o una resta de su número aleatorio y su porcentaje.")

print()

while True:
    limInf = int(input("Ingrese Limite inferior: "))
    limSup = int(input("Ingrese Limite superior: "))

    if limInf > limSup:
        print()
        print("Limite inferior no puede ser mayor que limite superior.")

    else:
        break
               
aleatorio = random.randint(limInf, limSup)

print()

# 1.0 INICIO DEL JUEGO.
resultado = int(input("¿Cuál es el resultado del número aleatorio generado en su rango? ")) # Primer intento.
if resultado != aleatorio and resultado < aleatorio:

# 2.0 RUTA SI LA RESPUESTA DEL PRIMER INTENTO ES MENOR AL RESULTADO.
    # 2.1
    resultado = int(input("Incorrecto. Su respuesta es menor que el resultado. Intente una vez más: ")) # Primer intento incorrecto. -> Segundo intento.
    if resultado != aleatorio and resultado < aleatorio:
        resultado = int(input("Incorrecto. Nueva pista: Su respuesta es menor que el resultado. Intente una vez más: ")) # Segundo intento incorrecto. -> Tercer intento.

        if resultado != aleatorio:
            print("Suficientes intentos. Perdió el juego.") # Tercer intento incorrecto.

        else:
            print("¡Felicidades! Logró salvarse al último intento.") # Tercer intento correcto.

    elif resultado != aleatorio and resultado > aleatorio:
        resultado = int(input("Incorrecto. Nueva pista: Su respuesta es mayor que el resultado. Intente una vez más: ")) # Segundo intento incorrecto. -> Tercer intento.

    else:
        print("¡Felicidades! Acertó al segundo intento.") # Segundo intento correcto.


elif resultado != aleatorio and resultado > aleatorio:
    resultado = int(input("Incorrecto. Nueva pista: Su respuesta es mayor que el resultado. Intente una vez más: ")) # Primer intento incorrecto. -> Segundo intento.

    if resultado != aleatorio and resultado > aleatorio:
        resultado = int(input("Incorrecto. Nueva pista: Su respuesta es mayor que el resultado. Intente una vez más: ")) # Segundo intento incorrecto. -> Tercer intento.

        if resultado != aleatorio:
            print("Suficientes intentos. Perdió el juego.") # Tercer intento incorrecto.

        else:
            print("¡Felicidades! Logró salvarse al último intento.") # Tercer intento correcto.

    else:
        print("¡Felicidades! Acertó al segundo intento.") # Segundo intento correcto.


else:
    print("¡Muy buena! ¡Acertó a la primera!") # Primer intento correcto.

    
print("-----------------------------")
print()
