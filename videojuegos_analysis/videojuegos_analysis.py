import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar datos
df = pd.read_csv('vgsales.csv')

# 2. Exploración básica
print("=== Primeras 5 filas ===")
print(df.head())
print("\n=== Información ===")
print(df.info())
print("\n=== Estadísticas ===")
print(df.describe())

# 3. Limpiar columna Year
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
df = df.dropna(subset=['Year'])
df['Year'] = df['Year'].astype(int)

# 4. Crear columna de ventas totales por región
df['Total_Region_Sales'] = df['NA_Sales'] + df['EU_Sales'] + df['JP_Sales'] + df['Other_Sales']
# Verificar que coincide con Global_Sales
print("\n=== Diferencias entre Total_Region_Sales y Global_Sales ===")
print((df['Total_Region_Sales'] - df['Global_Sales']).abs().max())

# 5. Análisis por plataforma: top 10 por ventas globales
top_plataformas = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head(10)
print("\n=== Top 10 plataformas por ventas globales ===")
print(top_plataformas)

plt.figure(figsize=(10,6))
top_plataformas.plot(kind='barh', color='skyblue', edgecolor='black')
plt.title('Top 10 plataformas por ventas globales (millones)')
plt.xlabel('Ventas globales (millones)')
plt.ylabel('Plataforma')
plt.gca().invert_yaxis()  # para que la mayor quede arriba
plt.tight_layout()
plt.savefig('top_plataformas.png', dpi=150, bbox_inches='tight')
plt.show()

# 6. Análisis por género
ventas_por_genero = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)
print("\n=== Ventas globales por género ===")
print(ventas_por_genero)

plt.figure(figsize=(10,6))
ventas_por_genero.plot(kind='bar', color='lightgreen', edgecolor='black')
plt.title('Ventas globales por género')
plt.xlabel('Género')
plt.ylabel('Ventas globales (millones)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('ventas_por_genero.png', dpi=150, bbox_inches='tight')
plt.show()

# 7. Evolución temporal de ventas globales
ventas_por_anio = df.groupby('Year')['Global_Sales'].sum()
print("\n=== Ventas globales por año (primeros 10) ===")
print(ventas_por_anio.head(10))

plt.figure(figsize=(10,6))
ventas_por_anio.plot(kind='line', marker='o', color='coral')
plt.title('Evolución de ventas globales por año')
plt.xlabel('Año')
plt.ylabel('Ventas globales (millones)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('evolucion_ventas.png', dpi=150, bbox_inches='tight')
plt.show()

# 8. Top publishers por ventas totales
top_publishers = df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).head(10)
print("\n=== Top 10 publishers por ventas globales ===")
print(top_publishers)

# 9. Insights
print("\n=== Insights ===")
print("1. El genero de action, sports y shooter son los mas vendidos")
print("2. Las plataformas PS2, X360 y PS3 son las que tienen mas ventas, seguidas muy de cerca por Wii y DS")
print("3. A partir del año 2010 se nota una caida constante en las ventas globales, lo que puede deberse a la saturación del mercado o al cambio en los hábitos de consumo hacia juegos móviles y digitales.")


