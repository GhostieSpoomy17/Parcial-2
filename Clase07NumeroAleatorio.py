# EJERCICIO TIPO EXAMEN - CLASE 07:


import random

print()

print("-----------------------------")

print("Usted va a dar números según se le indique para recibir un número aleatorio y un porcentaje. Al tener todos estos datos,")
print("va a decidir si realizar una suma o una resta de su número aleatorio y su porcentaje.")

print()

def main():
    while True:
        limInf = int(input("Ingrese Limite inferior: "))
        limSup = int(input("Ingrese Limite superior: "))
        if limInf > limSup:
            print()
            print("Limite inferior no puede ser mayor que limite superior.")
        else:
            break
            
    print()
        
    aleatorio = random.randint(limInf, limSup)
    print ("Su número aleatorio es: ", aleatorio)

    print()

    porcentaje = int(input("Ingrese un porcentaje: "))

    print()

    while True:
        operacion = int(input("Ingrese 1 si quiere sumar ese porcentaje o 2 si quiere restarlo: "))

        if operacion == 1 or operacion == 2:
            break
        else:
            print()
            print("Operacion solo puede ser 1 o 2")

    if operacion == 1:
        valorNuevo = aleatorio + aleatorio * porcentaje/100
    else:
        valorNuevo = aleatorio - aleatorio * porcentaje/100

    print()
        
    print("El nuevo valor es ", valorNuevo)
    
if __name__ == "__main__":
    main()

print("-----------------------------")
