def validar_estado(valor_inicial: str, idx: int) -> int:
    """Pide y valida el estado del interruptor idx (0 o 1)."""
    entrada = valor_inicial
    while True:
        try:
            v = int(entrada)
            if v in (0, 1):
                return v
            else:
                raise ValueError
        except ValueError:
            print("Ingrese una opción válida (0=CERRADO, 1=ABIERTO)")
            entrada = input(f"Estado del interruptor {idx}: ")


print("----- Estado de los interruptores -----\nABIERTO = 1 \nCERRADO = 0")
print("---------------------------------------")
estados = []
for i in range(1, 4):
    valor = input(f"Estado del interruptor {i}: ")
    estado = validar_estado(valor, i)
    estados.append(estado)

print("---------------------------------------")
if sum(estados) >= 2:
    print("El equipo funcionará")
else:
    print("El equipo no funcionará")