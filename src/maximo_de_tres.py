# Desarrollar un programa que solicite tres números al usuario,
# posteriormente el programa debe indicar cual de los tres números es
# el mayor.

valores = []
for i in range(3):
    entrada = input(f"Ingrese el número {i + 1}: ")
    while True:
        try:
            num = float(entrada)
            valores.append(num)
            break
        except ValueError:
            print("Entrada inválida. Ingrese un número (entero o decimal).")
            entrada = input(f"Ingrese el número {i + 1}: ")

mx = max(valores)
conteo_mx = sum(1 for v in valores if v == mx)

if conteo_mx > 1:
    print(f"El número máximo es {mx} (hay {conteo_mx} valores iguales al máximo).")
else:
    print(f"El número más alto es: {mx}")