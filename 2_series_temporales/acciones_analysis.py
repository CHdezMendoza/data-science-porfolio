import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Descargar datos históricos de Apple y Tesla (últimos 3 años)
tickers = ['AAPL', 'TSLA']
data = yf.download(tickers, period='3y', interval='1d')['Close']

# data es un DataFrame con columnas AAPL y TSLA
# Eliminar filas con nulos
data.dropna(inplace=True)

# Calcular retornos diarios
retornos = data.pct_change().dropna()

# Mostrar últimos precios
print("=== Últimos 10 días de precios de cierre ===")
print(data.tail(10))

print("\n=== Rendimiento promedio diario (%) ===")
print(retornos.mean() * 100)

print("\n=== Volatilidad (desviación estándar diaria) ===")
print(retornos.std())

# Graficar precios normalizados (base 100 al inicio)
normalizado = data / data.iloc[0] * 100
plt.figure(figsize=(12,6))
plt.plot(normalizado.index, normalizado['AAPL'], label='Apple', color='blue')
plt.plot(normalizado.index, normalizado['TSLA'], label='Tesla', color='red')
plt.title('Precios de cierre normalizados (base 100)')
plt.xlabel('Fecha')
plt.ylabel('Precio normalizado')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('precios_normalizados.png', dpi=150, bbox_inches='tight')
plt.show()

# Histogramas de retornos
plt.figure(figsize=(12,5))
plt.subplot(1, 2, 1)
retornos['AAPL'].hist(bins=50, alpha=0.7, color='blue')
plt.title('Retornos diarios Apple')
plt.xlabel('Retorno')
plt.ylabel('Frecuencia')

plt.subplot(1, 2, 2)
retornos['TSLA'].hist(bins=50, alpha=0.7, color='red')
plt.title('Retornos diarios Tesla')
plt.xlabel('Retorno')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.savefig('histogramas_retornos.png', dpi=150, bbox_inches='tight')
plt.show()
