import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# =======================================================
# 1. Cargar datos
# =======================================================
df = pd.read_csv('covid_confirmed.csv')

# Exploración básica
print("=== Dimensiones del dataset ===")
print(df.shape)
print("\n=== Primeras 5 filas (primeras 8 columnas) ===")
print(df.iloc[:5, :8])
print("\n=== Columnas de fechas (últimas 5) ===")
print(df.columns[-5:])

# =======================================================
# 2. Agrupar por país (sumando provincias)
# =======================================================
# Seleccionar solo columnas de fechas (todas menos las 4 primeras)
fechas_columnas = df.columns[4:]
df_paises = df.groupby('Country/Region')[fechas_columnas].sum()

# Transponer: fechas como filas, países como columnas
df_paises = df_paises.transpose()

# Convertir índice a datetime
df_paises.index = pd.to_datetime(df_paises.index)

# Ordenar por fecha
df_paises = df_paises.sort_index()

# =======================================================
# 3. Seleccionar países de interés
# =======================================================
paises_interes = ['Mexico', 'US', 'Brazil', 'Spain', 'Italy', 'Germany', 'India', 'Japan']
# Algunos nombres pueden tener variantes; asegurarse de que existan
paises_presentes = [p for p in paises_interes if p in df_paises.columns]
print(f"\nPaíses seleccionados: {paises_presentes}")

df_sel = df_paises[paises_presentes]

# =======================================================
# 4. Visualizar evolución de casos confirmados
# =======================================================
plt.figure(figsize=(12,8))
for pais in paises_presentes:
    plt.plot(df_sel.index, df_sel[pais], label=pais, linewidth=2)

plt.title('Casos confirmados de COVID-19 por país (escala logarítmica)')
plt.xlabel('Fecha')
plt.ylabel('Casos confirmados (log)')
plt.yscale('log')  # escala log para comparar mejor
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('casos_confirmados_paises.png', dpi=150)
plt.show()

# =======================================================
# 5. Nuevos casos diarios y media móvil (ejemplo México)
# =======================================================
pais_ejemplo = 'Mexico'
nuevos_casos = df_sel[pais_ejemplo].diff().dropna()

# Media móvil de 7 días
media_movil = nuevos_casos.rolling(window=7).mean()

plt.figure(figsize=(12,6))
plt.plot(nuevos_casos.index, nuevos_casos.values, alpha=0.4, label='Nuevos casos diarios')
plt.plot(media_movil.index, media_movil.values, color='red', linewidth=2, label='Media móvil 7 días')
plt.title(f'Nuevos casos diarios en {pais_ejemplo}')
plt.xlabel('Fecha')
plt.ylabel('Casos nuevos')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('nuevos_casos_mexico.png', dpi=150)
plt.show()

# =======================================================
# 6. Comparar tasas de crecimiento (días para duplicarse desde 1000 casos)
# =======================================================
def dias_duplicacion(pais, umbral=1000):
    serie = df_sel[pais]
    # Día en que supera el umbral
    if serie.max() < umbral:
        return None
    inicio_idx = serie[serie >= umbral].index[0]
    inicio_val = serie.loc[inicio_idx]
    duplicado_val = inicio_val * 2
    # Día en que supera el doble
    try:
        fin_idx = serie[serie >= duplicado_val].index[0]
        dias = (fin_idx - inicio_idx).days
        return dias
    except:
        return None

print("\n=== Días para duplicar casos desde 1000 ===")
for pais in paises_presentes:
    d = dias_duplicacion(pais)
    if d:
        print(f"{pais}: {d} días")
    else:
        print(f"{pais}: no alcanzó el umbral o no se pudo calcular")

# =======================================================
# 7. Insights
# =======================================================
print("\n=== Insights ===")
print("1. La evolución en escala logarítmica muestra fases de crecimiento exponencial y aplanamiento.")
print("2. Los nuevos casos diarios presentan picos que coinciden con olas epidémicas.")
print("3. La velocidad de duplicación inicial varió entre países; los que actuaron tarde tuvieron duplicaciones más rápidas.")
print("4. La media móvil suaviza la variabilidad diaria y revela tendencias.")

