import requests
from bs4 import BeautifulSoup
from sentiment_analysis_spanish import sentiment_analysis
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import FreqDist

# Función para obtener texto de un enlace
def obtener_texto_enlace(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    texto = ' '.join([p.get_text() for p in paragraphs])
    return texto

# Función para analizar sentimientos
def analizar_sentimientos(texto):
    sa = sentiment_analysis.SentimentAnalysisSpanish()
    score = sa.sentiment(texto)
    return score

# Función para resaltar palabras clave
def resaltar_palabras_clave(texto, num_palabras=5):
    palabras = word_tokenize(texto)
    palabras = [palabra.lower() for palabra in palabras if palabra.isalpha() and palabra.lower() not in stopwords.words('spanish')]
    
    freq_dist = FreqDist(palabras)
    palabras_clave = freq_dist.most_common(num_palabras)
    return [palabra for palabra, _ in palabras_clave]

# Ejemplo de uso con la URL proporcionada
enlace_noticia = 'https://www.lne.es/asturias/2023/11/27/kamikaze-hizo-trayecto-enorme-velocidad-95133181.html'
texto_noticia = obtener_texto_enlace(enlace_noticia)
sentimiento = analizar_sentimientos(texto_noticia)
palabras_clave = resaltar_palabras_clave(texto_noticia)

print(f'Texto noticia: {texto_noticia}')
print(f'Sentimiento: {sentimiento}')
print(f'Palabras clave: {palabras_clave}')
