"""Crea un programa que permita ingresar varios estudiantes con sus nombres y notas. Por cada uno:

Calcula si aprueba o no (nota ≥ 60).

Asigna una letra de calificación:

Guarda todo en un diccionario anidado.

Al final, muestra:

Los datos completos de cada estudiante

El promedio general del grupo

Cuántos aprobaron y reprobaron

"""
def clasificar_nota(nota):
    if nota >= 9:
        return "S"
    elif nota >= 8:
        return "E"
    elif nota >= 7:
        return "R"
    elif nota >= 6:
        return "B"
    else:
        return "I"

estudiantes = {}

while True:
    nombre = input("Ingrese el  nombre del estudiante, o el numero 1 para salir: ").strip()
    if nombre.lower() == "1":
        break
    
    try:
        nota =int(input(f"Ingrese lanota del estudiante {nombre}: "))

        if nota < 0  or nota >10:
            print ("la nota debe estar entre 0 y 10. intente  de nuevo")
            continue
    except ValueError:
        print("La nota debe ser un numero")
        continue
    letra = clasificar_nota(nota)
    estado = ""
    if nota >= 6:
        estado = "Aprobado"
    else:
        estado = "Reprobado"


#nombre es  la clave del diccionario "estudiantes" y el valor es un subdiccionarios  con las claves,nota,letra,estado y sus valores

    estudiantes [nombre] ={  
        "nota": nota,
        "letra": letra,
        "estado": estado
    }


print("\n Resultados Finales:")
suma = 0
estudiantesAprobados = 0
estudiantesReprobados = 0

for nombre, datos in estudiantes.items():
    print(f"{nombre}  Nota: {datos['nota']} ({datos['letra']}) - {datos['estado']}")
    suma += datos["nota"]
    if datos["estado"] == "Aprobado":
        estudiantesAprobados  += 1
    else:
        estudiantesReprobados += 1

total = len(estudiantes)
if total > 0:
    promedio = suma / total
    print(f"\nPromedio general del grupo: {promedio:.2f}")
    print(f"Total de estudiantes: {total}")
    print(f"Aprobados: {estudiantesAprobados}")
    print(f"Reprobados: {estudiantesReprobados}")
else:
    print("No se ingresaron estudiantes.")
    