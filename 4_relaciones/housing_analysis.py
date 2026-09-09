import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar datos
df = pd.read_csv('housing.csv')

# Exploración básica
print("=== Primeras filas ===")
print(df.head())
print("\n=== Información ===")
print(df.info())
print("\n=== Nulos por columna ===")
print(df.isnull().sum())

# Limpieza: rellenar nulos en total_bedrooms con la mediana
df['total_bedrooms'] = df['total_bedrooms'].fillna(df['total_bedrooms'].median())

# Crear columnas adicionales (ratios)
df['rooms_per_household'] = df['total_rooms'] / df['households']
df['bedrooms_per_room'] = df['total_bedrooms'] / df['total_rooms']
df['population_per_household'] = df['population'] / df['households']

# Seleccionar columnas numéricas para correlación
numericas = df.select_dtypes(include=[np.number])
correlaciones = numericas.corr()

print("\n=== Correlación con median_house_value (ordenado) ===")
print(correlaciones['median_house_value'].sort_values(ascending=False))

# Mapa de calor con matplotlib (sin seaborn)
plt.figure(figsize=(12,10))
plt.imshow(correlaciones, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar(label='Coeficiente de correlación')
plt.xticks(range(len(correlaciones.columns)), correlaciones.columns, rotation=90)
plt.yticks(range(len(correlaciones.columns)), correlaciones.columns)
plt.title('Mapa de calor de correlaciones')
plt.tight_layout()
plt.savefig('mapa_calor_correlaciones.png', dpi=150, bbox_inches='tight')
plt.show()

# Scatter plot: median_income vs median_house_value
plt.figure(figsize=(8,6))
plt.scatter(df['median_income'], df['median_house_value'], alpha=0.5)
plt.title('Relación entre ingreso mediano y valor de la vivienda')
plt.xlabel('Ingreso mediano (en decenas de miles)')
plt.ylabel('Valor mediano de la vivienda (USD)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('scatter_income_vs_value.png', dpi=150, bbox_inches='tight')
plt.show()

# Scatter plot: latitud y longitud coloreado por valor (opcional)
plt.figure(figsize=(10,6))
sc = plt.scatter(df['longitude'], df['latitude'], c=df['median_house_value'],
                 cmap='viridis', alpha=0.6)
plt.colorbar(sc, label='Valor mediano')
plt.title('Distribución geográfica de precios')
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.tight_layout()
plt.savefig('scatter_geografico_valor.png', dpi=150, bbox_inches='tight')
plt.show()

