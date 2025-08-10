def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir entre 0"


def potencia(a, b):
    return a ** b


def div_entera(a, b):
    return a // b


def modulo(a, b):
    return a % b


operaciones = {
    1: suma,
    2: resta,
    3: multiplicacion,
    4: division,
    5: potencia,
    6: div_entera,
    7: modulo,
}
ent_in = input("1 - Entrar a la calculadora \n2 - Salir \n---> ")
while True:
    try:
        ent = int(ent_in)
        break
    except ValueError:
        print("Seleccione una opción válida")
        ent_in = input("1 - Entrar a la calculadora \n2 - Salir \n---> ")

while ent == 1:
    print(""" ------- CALCULADORA BASICA ------- 
    OPERACIONES DISPONIBLES:
    1. SUMA
    2. RESTA
    3. MULTIPLICACIÓN 
    4. DIVISIÓN
    5. POTENCIA
    6. DIVISION ENTERA
    7. MÓDULO
 ----------------------------------""")
    op_in = input("Ingrese la operación deseada (1-7): ")
    while True:
        try:
            op = int(op_in)
            if op in operaciones:
                break
            else:
                raise ValueError
        except ValueError:
            print("Seleccione una opción válida (1-7)")
            op_in = input("Ingrese la operación deseada (1-7): ")
    print("----------------------------------")
    x_in = input("Ingrese el primer número: ")
    while True:
        try:
            x = float(x_in)
            break
        except ValueError:
            print("Valor inválido. Ingrese un número válido.")
            x_in = input("Ingrese el primer número: ")

    y_in = input("Ingrese el segundo número: ")
    while True:
        try:
            y = float(y_in)
            break
        except ValueError:
            print("Valor inválido. Ingrese un número válido.")
            y_in = input("Ingrese el segundo número: ")
    print("----------------------------------")
    print("RESULTADO: ", operaciones[op](x, y))
    print("----------------------------------")
    ent_in = input("1 - Seguir calculando \n2 - Salir \n---> ")
    while True:
        try:
            ent = int(ent_in)
            if ent in [1, 2]:
                break
            else:
                raise ValueError
        except ValueError:
            print("Seleccione una opción válida")
            ent_in = input("1 - Seguir calculando \n2 - Salir \n---> ")