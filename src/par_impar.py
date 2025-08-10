# 1. Desarrollar un programa que solicite un número entero desde teclado
# y determinar si dicho número es par o impar.

# Solicitar un entero de forma robusta
entrada = input("Ingrese un número entero: ")
while True:
    try:
        x = int(entrada)
        break
    except ValueError:
        print("El valor ingresado no es un entero válido.")
        entrada = input("Ingrese un número entero: ")

if x % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")