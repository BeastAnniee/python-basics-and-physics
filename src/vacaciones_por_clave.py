def clave_1(a):
    if a == 1:
        return 6
    elif 2 <= a <= 6:
        return 14
    elif a >= 7:
        return 20


def clave_2(a):
    if a == 1:
        return 7
    elif 2 <= a <= 6:
        return 15
    elif a >= 7:
        return 22


def clave_3(a):
    if a == 1:
        return 10
    elif 2 <= a <= 6:
        return 20
    elif a >= 7:
        return 30


claves = {
    1: clave_1,
    2: clave_2,
    3: clave_3,
}

# Bucle interactivo con validaciones robustas
ent = input("1 - Entrar al programa \n2 - Salir \n---> ")
while True:
    try:
        ent = int(ent)
        break
    except ValueError:
        print("¡¡Ingrese una opcion valida!!")
        ent = input("1 - Entrar al programa \n2 - Salir \n---> ")

while ent == 1:
    print("----- CALCULO DE VACACIONES -----")
    name = input("Ingrese el nombre del empleado: ")

    # Leer clave de departamento como entero válido
    clave_in = input("Ingrese la clave del departamento (1-3): ")
    while True:
        try:
            clave = int(clave_in)
            if clave in claves:
                break
            else:
                raise ValueError
        except ValueError:
            print("¡¡Ingrese una opcion valida!!")
            clave_in = input("Ingrese la clave del departamento (1-3): ")

    # Leer antigüedad como entero no negativo
    antig_in = input("Ingrese la antigüedad del empleado (en años): ")
    while True:
        try:
            antiguedad = int(antig_in)
            if antiguedad >= 0:
                break
            else:
                raise ValueError
        except ValueError:
            print("¡¡Ingrese una opcion valida!!")
            antig_in = input("Ingrese la antigüedad del empleado (en años): ")

    print("-------------------------------")
    print("EMPLEADO: ", name)
    print("DIAS DE DESCANSO: ", claves[clave](antiguedad))
    print("-------------------------------")

    # Preguntar si desea continuar
    ent_in = input("1 - Seguir \n2 - Salir \n---> ")
    while True:
        try:
            ent = int(ent_in)
            if ent in [1, 2]:
                break
            else:
                raise ValueError
        except ValueError:
            print("¡¡Ingrese una opcion valida!!")
            ent_in = input("1 - Seguir \n2 - Salir \n---> ")