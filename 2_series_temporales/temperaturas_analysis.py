import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv('monthly.csv')

# Convertir la columna Year a datetime (formato 'YYYY-MM')
df['Date'] = pd.to_datetime(df['Year'])

# Opcional: filtrar por una fuente si hay más de una (por ahora asumimos solo GCAG)
# df = df[df['Source'] == 'GCAG']

# Establecer Date como índice
df.set_index('Date', inplace=True)

# Exploración básica
print("=== Primeras filas ===")
print(df.head())
print("\n=== Información ===")
print(df.info())

# Remuestrear a frecuencia anual (promedio)
anual = df['Mean'].resample('YE').mean()

# Calcular media móvil de 5 años
media_movil = anual.rolling(window=5).mean()

# Graficar
plt.figure(figsize=(12,6))
plt.plot(anual.index, anual.values, label='Temperatura media anual', color='blue', alpha=0.7)
plt.plot(anual.index, media_movil.values, label='Media móvil 5 años', color='red', linewidth=2)
plt.title('Temperatura global media anual (1850-2020)')
plt.xlabel('Año')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# Mostrar últimos años
print("\n=== Últimos 10 años (anual) ===")
print(anual.tail(10))

