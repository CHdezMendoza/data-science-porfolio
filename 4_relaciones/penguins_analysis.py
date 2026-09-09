import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar datos
df = pd.read_csv('penguins.csv')

# Exploración básica
print("=== Primeras filas ===")
print(df.head())
print("\n=== Información ===")
print(df.info())
print("\n=== Nulos por columna ===")
print(df.isnull().sum())

# Limpieza: eliminar filas con nulos en variables numéricas
df = df.dropna(subset=['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])

# Seleccionar columnas numéricas
numericas = df.select_dtypes(include=[np.number])
correlaciones = numericas.corr()

print("\n=== Correlaciones entre variables numéricas ===")
print(correlaciones)

# Mapa de calor
plt.figure(figsize=(8,6))
plt.imshow(correlaciones, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar(label='Correlación')
plt.xticks(range(len(correlaciones.columns)), correlaciones.columns, rotation=45)
plt.yticks(range(len(correlaciones.columns)), correlaciones.columns)
plt.title('Mapa de calor de correlaciones')
plt.tight_layout()
plt.savefig('mapa_calor_correlaciones.png', dpi=150, bbox_inches='tight')
plt.show()

# Scatter plot: flipper length vs body mass coloreado por especie
plt.figure(figsize=(8,6))
for especie, grupo in df.groupby('species'):
    plt.scatter(grupo['flipper_length_mm'], grupo['body_mass_g'],
                label=especie, alpha=0.7)
plt.title('Relación entre largo de aleta y masa corporal por especie')
plt.xlabel('Largo de aleta (mm)')
plt.ylabel('Masa corporal (g)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('scatter_flipper_vs_body_mass.png', dpi=150, bbox_inches='tight')
plt.show()

# Boxplots de body mass por especie
plt.figure(figsize=(8,6))
df.boxplot(column='body_mass_g', by='species', ax=plt.gca())
plt.title('Distribución de masa corporal por especie')
plt.suptitle('')
plt.xlabel('Especie')
plt.ylabel('Masa corporal (g)')
plt.tight_layout()
plt.savefig('boxplots_body_mass.png', dpi=150, bbox_inches='tight')
plt.show()

# Comparar medias por especie
print("\n=== Media de variables por especie ===")
print(df.groupby('species')[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']].mean())

