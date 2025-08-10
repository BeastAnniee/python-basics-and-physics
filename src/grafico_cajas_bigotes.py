import matplotlib.pyplot as plt

# Datos ordenados
datos = [
    30, 60, 70, 80, 90, 90, 90, 100, 110, 110, 120, 120, 123, 130, 135,
    140, 150, 150, 170, 175, 180, 180, 210, 210, 225, 270, 300, 400, 420, 840
]

# Crear el diagrama de cajas y bigotes
plt.figure(figsize=(10, 6))
boxplot = plt.boxplot(datos, vert=False, patch_artist=True,
                      boxprops=dict(facecolor='skyblue', color='black'),
                      whiskerprops=dict(color='black'),
                      capprops=dict(color='black'),
                      flierprops=dict(marker='o', color='red', alpha=0.7),
                      medianprops=dict(color='darkred', linewidth=2))

# Configurar el gráfico
plt.title('Diagrama de Cajas y Bigotes: Minutos de Música Escuchados', fontsize=14)
plt.xlabel('Minutos', fontsize=12)
plt.yticks([1], ['Datos'])
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Ajustar el rango del eje X para incluir todos los valores
plt.xlim(0, 900)

# Mostrar el gráfico
plt.show()