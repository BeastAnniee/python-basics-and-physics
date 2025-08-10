import matplotlib.pyplot as plt

# Datos 
datos = [
    30, 60, 70, 80, 90, 90, 90, 100, 110, 110, 120, 120, 123, 130, 135,
    140, 150, 150, 170, 175, 180, 180, 210, 210, 225, 270, 300, 400, 420, 840
]

# Límites de los intervalos
rango = 135  # Rango
max_valor = max(datos)
bins = list(range(0, max_valor + rango, rango))  # Bordes de las barras

# Crear el histograma
plt.hist(datos, bins=bins, edgecolor='black', color='skyblue', alpha=0.7)

# Configurar el gráfico
plt.title('Histograma de Minutos de Música Escuchados')
plt.xlabel('Minutos')
plt.ylabel('Frecuencia')
plt.xticks(bins)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar el histograma
plt.show()