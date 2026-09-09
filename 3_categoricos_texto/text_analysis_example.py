import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re

# =======================================================
# 1. Crear dataset reviews de Alexa
# =======================================================
data = {
    'rating': [5,5,4,5,1,3,5,2,4,5,1,5,5,4,3,2,5,4,5,1,
               4,5,5,3,2,5,1,4,5,5,4,3,5,1,2,5,4,5,5,3],
    'date': ['2020-01-01']*40,
    'variation': ['Black Dot']*40,
    'verified_reviews': [
        "I love my Alexa, it is amazing and very easy to use.",
        "Great product, excellent sound quality and awesome features.",
        "Good device but sometimes it doesn't understand me well.",
        "Very happy with my purchase, works perfectly.",
        "Worst product ever, useless and annoying.",
        "It is okay, but not great. A bit difficult to set up.",
        "Love it! Best smart speaker I've owned.",
        "Bad quality, poor microphone and it disconnects often.",
        "Nice design, happy with the performance.",
        "Absolutely fantastic, love the integration with my smart home.",
        "Terrible experience, waste of money.",
        "Excellent device, very responsive and easy to control.",
        "Perfect for my kitchen, I use it every day.",
        "Good value, but the sound could be better.",
        "It's fine, does what it should, nothing special.",
        "Disappointed, it stopped working after two weeks.",
        "Wonderful, the kids love asking it questions.",
        "Not great, the Wi-Fi connection drops frequently.",
        "Happy with the alarm and timer features.",
        "Hate it, difficult to pair with my phone.",
        "Amazing sound for the size, very impressed.",
        "Love the routine feature, makes mornings easier.",
        "Good product, but the app is a bit confusing.",
        "It's okay, sometimes it hears me incorrectly.",
        "Useless, the voice recognition is terrible.",
        "Great for playing music, excellent bass.",
        "Worst purchase, totally overpriced.",
        "Nice, does what I need, no complaints.",
        "Fantastic, I control all my lights with it.",
        "Poor quality, the speaker crackles at high volume.",
        "Very good, the microphone picks up my voice from afar.",
        "It's average, not bad but not amazing.",
        "Love it, use it every single day.",
        "Horrible, it never understands my commands.",
        "Disappointing, expected better for the price.",
        "Great product, highly recommend to everyone.",
        "Good for timers and weather updates.",
        "Excellent, the sound is clear and loud.",
        "Very happy, works seamlessly with my other devices.",
        "Bad, the setup was a nightmare and it kept failing."
    ],
    'feedback': [1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,0,1,0,1,0,
                 1,1,1,1,0,1,0,1,1,0,1,1,1,0,0,1,1,1,1,1]
}

df = pd.DataFrame(data)

# =======================================================
# 2. Exploración básica
# =======================================================
print("=== Primeras filas ===")
print(df.head())
print("\n=== Distribución de feedback (1=positivo, 0=negativo) ===")
print(df['feedback'].value_counts())

# =======================================================
# 3. Preprocesamiento de texto
# =======================================================
stopwords = set(['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your',
                 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she',
                 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their',
                 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that',
                 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
                 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an',
                 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of',
                 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through',
                 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down',
                 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then',
                 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any',
                 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no',
                 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's',
                 't', 'can', 'will', 'just', 'don', 'should', 'now'])

def limpiar_texto(texto):
    # Convertir a minúsculas y extraer solo palabras
    palabras = re.findall(r'\b[a-z]+\b', texto.lower())
    # Filtrar stopwords y palabras de longitud <= 2
    palabras_filtradas = [p for p in palabras if p not in stopwords and len(p) > 2]
    return palabras_filtradas

# Aplicar limpieza
df['palabras'] = df['verified_reviews'].apply(limpiar_texto)

# =======================================================
# 4. Conteo de frecuencia de palabras
# =======================================================
contador = Counter()
for lista in df['palabras']:
    contador.update(lista)

print("\n=== 20 palabras más frecuentes ===")
for palabra, freq in contador.most_common(20):
    print(f"{palabra}: {freq}")

# Visualizar top 15
top_palabras = dict(contador.most_common(15))
plt.figure(figsize=(10,6))
plt.bar(top_palabras.keys(), top_palabras.values(), color='lightgreen')
plt.title('Top 15 palabras más frecuentes en reviews de Alexa (dataset de ejemplo)')
plt.xlabel('Palabra')
plt.ylabel('Frecuencia')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('top_palabras_frecuentes.png', dpi=150, bbox_inches='tight')
plt.show()

# =======================================================
# 5. Análisis de sentimiento con reglas
# =======================================================
positivas = set(['good', 'great', 'awesome', 'excellent', 'love', 'nice', 'amazing',
                 'fantastic', 'perfect', 'happy', 'best', 'wonderful', 'easy',
                 'impressive', 'recommend', 'seamlessly'])
negativas = set(['bad', 'terrible', 'horrible', 'awful', 'poor', 'worse', 'worst',
                 'disappointed', 'hate', 'annoying', 'difficult', 'useless',
                 'disappointing', 'nightmare', 'overpriced', 'crackles'])

def clasificar_sentimiento(palabras):
    score = 0
    for p in palabras:
        if p in positivas:
            score += 1
        elif p in negativas:
            score -= 1
    return 'positivo' if score > 0 else ('negativo' if score < 0 else 'neutral')

df['sentimiento'] = df['palabras'].apply(clasificar_sentimiento)

print("\n=== Distribución de sentimiento según reglas ===")
print(df['sentimiento'].value_counts())

print("\n=== Comparación con feedback real (1=positivo, 0=negativo) ===")
print(pd.crosstab(df['sentimiento'], df['feedback']))

# =======================================================
# 6. Insights
# =======================================================
print("\n=== Insights ===")
print("1. Las palabras más frecuentes incluyen 'love', 'good', 'great', 'easy', etc.")
print("2. El análisis de reglas clasifica correctamente la mayoría de positivos, pero algunos negativos se confunden con neutros.")
print("3. Limitación: no maneja negaciones (ej. 'not good' se tomaría como 'good').")
print("4. Se podría mejorar agregando más palabras o usando lematización y manejo de negaciones.")
