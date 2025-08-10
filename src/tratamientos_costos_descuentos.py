#Clientes mayores a 60 años 25% de descuento
#Clientes menores de 25 años 15% de descuento

# Tipos de tratamiento y su costo
# 1 : 2800
# 2 : 1950
# 3 : 2500
# 4 : 1150
# Tratamiento es una variable de tipo entero que representa el tipo de tratamiento
# Edad es una variable de tipo entero que represent la edad del cliente
# Dia es una variable de tipo entero que expresa el numero de dias
#Costo de internacion
#Ganancias del Día

# Declaración y configuración
costos_tratamientos = {1: 2800, 2: 1950, 3: 2500, 4: 1150}
total_ganancias = 0.0

# Inicio del programa
op_in = input("Ingrese: 1 para entrar al programa, 2 para salir: ")
while True:
    try:
        opcion = int(op_in)
        break
    except ValueError:
        print("Error: seleccione 1 o 2.")
        op_in = input("Ingrese: 1 para entrar al programa, 2 para salir: ")

while opcion == 1:
    # Leer tratamiento
    t_in = input("Ingrese el tipo de tratamiento del cliente (1-4): ")
    while True:
        try:
            tratamiento = int(t_in)
            if tratamiento in costos_tratamientos:
                break;
            else:
                raise ValueError
        except ValueError:
            print("Error al ingresar los datos. Debe ser 1, 2, 3 o 4.")
            t_in = input("Ingrese el tipo de tratamiento del cliente (1-4): ")

    # Leer edad
    e_in = input("Ingrese la edad del cliente: ")
    while True:
        try:
            edad = int(e_in)
            if edad >= 0:
                break
            else:
                raise ValueError
        except ValueError:
            print("Error al ingresar los datos. Ingrese una edad válida (entero no negativo).")
            e_in = input("Ingrese la edad del cliente: ")

    # Calcular costo con posibles descuentos
    cost = float(costos_tratamientos[tratamiento])
    if edad > 60:
        cost *= 0.75  # 25% de descuento
    elif edad < 25:
        cost *= 0.85  # 15% de descuento

    total_ganancias += cost
    print(f"El costo de internación del paciente es: {cost}")

    # Continuar o salir
    op_in = input("Ingrese: 1 para registrar otro paciente, 2 para salir: ")
    while True:
        try:
            opcion = int(op_in)
            if opcion in (1, 2):
                break
            else:
                raise ValueError
        except ValueError:
            print("Error: seleccione 1 o 2.")
            op_in = input("Ingrese: 1 para registrar otro paciente, 2 para salir: ")

print("El total de ganancias del día es: ", total_ganancias)