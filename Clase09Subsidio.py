
# EJERCICIO TIPO EXAMEN - CLASE 09 - SUBSIDIO:


# Desarrolle un programa en Python que permita calcular el subsidio de gas según el quintil de ingreso al que pertenece la familia del solicitante y sus condiciones laborales.

# Condiciones socioeconómicas:
# 1 = Menos Ingreso
# 5 = Mayor Ingreso

# Condiciones laborales:
# 1. Se considera si la persona está empleada o desempleada.

# 1. Quintil: 1 o 2, Laboral: Desempleado, Subsidio: 10.000
# 2. Quintil: 1 o 2, Laboral: Empleado, Subsidio: 8.000
# 3. Quintil: 3, Laboral: Desempleado, Subsidio: 6.000
# 4. Quintil: 3, Laboral: Empleado, Subsidio: 4.000
# 5. Quintil: 4 o 5, Laboral: Cualquiera, Subsidio: 1.500

# Bonos adicionales:
# 1. Si la persona pertenece al quintil 1 o 2, recibe un bono de 2.000.
# 2. Si tiene más de 65 años, recibe un bono de 3.000.


print("-------------------------------------")
print()

quintil = int(input("Buenas. ¿A qué quintil pertenece? "))

if quintil == 1 or 2:
    print()
    print("Entendido. Está usted empleado o desempleado?")
    empleabilidad1 = int(input("Responda con 1 para indicar que está empleado o 2 para responder que está desempleado. "))
    if empleabilidad1 == 1:
        print()
        print("Su subsidio es de 8.000.")
    elif empleabilidad1 == 2:
        print()
        print("Su subsidio es de 10.000.")

if quintil == 3:
    print()
    print("Entendido. Está usted empleado o desempleado?")
    empleabilidad2 = int(input("Responda con 1 para indicar que está empleado o 2 para responder que está desempleado. "))
    if empleabilidad2 == 1:
        print()
        print("Su subsidio es de 4.000.")
    elif empleabilidad2 == 2:
        print()
        print("Su subsidio es de 6.000.")

if quintil == 4 or 5:
    print()
    print("Si usted se encuentra en el quintil 4 o 5, su subsidio será de 1.500 independiente")
    print("de si está empleado o desempleado.")
