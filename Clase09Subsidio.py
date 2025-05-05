
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

quintil = int(input("Buenas. ¿A qué quintil pertenece? 1 a 5: "))
empleabilidad1 = int(input("Responda con 1 para indicar que está empleado o 2 para responder que está desempleado. "))
edad = int(input("Indique su edad en años: "))
subsidio = 0

# Logica para asignar bono
if quintil == 1 or quintil == 2:
    if empleabilidad1 == 1:
        subsidio = 8000
    elif empleabilidad1 == 2:
        subsidio = 10000

if quintil == 3:
    if empleabilidad1 == 1:
        subsidio = 4000
    elif empleabilidad1 == 2:
        subsidio = 6000
    
if quintil == 4 or quintil == 5:
    subsidio = 1500

if edad >= 65:
    subsidio = subsidio + 3000

print()

print("Su bono asignado es ", subsidio)

print()
print("-------------------------------------")
