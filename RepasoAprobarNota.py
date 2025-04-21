
# REPASO - CLASE 06 - DECISIÓN PARA VER SI UN ALUMNO APRUEBA O NO:


print(" ")

nota = float(input("Ingresa tu calificación: "))

print(" ")

if nota < 4.0:
    print("Reprobaste.")
elif nota <= 7.0:
    print("¡Felicidades! Aprobaste el curso.")
else:
    print("La nota máxima en Chile es un 7.0, dime tu nota real.")

print(" ")