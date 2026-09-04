import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar datos
df = pd.read_csv('titanic.csv')

# 2. Exploración básica
print("=== Primeras 5 filas ===")
print(df.head())
print("\n=== Información del DataFrame ===")
print(df.info())
print("\n=== Estadísticas descriptivas ===")
print(df.describe())

# 3. Valores nulos
print("\n=== Nulos por columna ===")
print(df.isnull().sum())

# Tratar nulos:
# - Edad: rellenar con la mediana
df['Age'] = df['Age'].fillna(df['Age'].median())
# - Embarcado: rellenar con la moda
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
# - Cabina: eliminar columna por demasiados nulos
df.drop('Cabin', axis=1, inplace=True)

# Verificar que ya no hay nulos
print("\n=== Nulos después de limpieza ===")
print(df.isnull().sum())

# 4. Crear columnas nuevas
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
df['IsAlone'] = (df['FamilySize'] == 1).astype(int)

# 5. Visualizaciones

# 5.1 Supervivencia por sexo
plt.figure(figsize=(8,5))
df.groupby('Sex')['Survived'].mean().plot(kind='bar', color=['pink','lightblue'], edgecolor='black')
plt.title('Tasa de supervivencia por sexo')
plt.ylabel('Proporción de sobrevivientes')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('supervivencia_por_sexo.png', dpi=150, bbox_inches='tight')
plt.show()

# 5.2 Supervivencia por clase
plt.figure(figsize=(8,5))
df.groupby('Pclass')['Survived'].mean().plot(kind='bar', color='lightgreen', edgecolor='black')
plt.title('Tasa de supervivencia por clase')
plt.ylabel('Proporción de sobrevivientes')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('supervivencia_por_clase.png', dpi=150, bbox_inches='tight')
plt.show()

# 5.3 Distribución de edad por supervivencia (histograma separado)
plt.figure(figsize=(10,5))
sobrevivientes = df[df['Survived']==1]['Age']
no_sobrevivientes = df[df['Survived']==0]['Age']
plt.hist(sobrevivientes, bins=20, alpha=0.6, label='Sobrevivientes', color='green')
plt.hist(no_sobrevivientes, bins=20, alpha=0.6, label='No sobrevivientes', color='red')
plt.title('Distribución de edad por supervivencia')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.legend()
plt.tight_layout()
plt.savefig('distribucion_edad_supervivencia.png', dpi=150, bbox_inches='tight')
plt.show()

# 5.4 Relación edad-tarifa con color por supervivencia
plt.figure(figsize=(8,6))
for sobrev, grupo in df.groupby('Survived'):
    etiqueta = 'Sobrevivientes' if sobrev == 1 else 'No sobrevivientes'
    plt.scatter(grupo['Age'], grupo['Fare'], label=etiqueta, alpha=0.5)
plt.title('Edad vs Tarifa según supervivencia')
plt.xlabel('Edad')
plt.ylabel('Tarifa')
plt.legend()
plt.tight_layout()
plt.savefig('edad_vs_tarifa_supervivencia.png', dpi=150, bbox_inches='tight')
plt.show()

# 6. Agrupación por sexo y clase
print("\n=== Tasa de supervivencia por sexo y clase ===")
print(df.groupby(['Sex', 'Pclass'])['Survived'].mean())

