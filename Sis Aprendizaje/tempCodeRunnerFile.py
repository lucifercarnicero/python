import requests
from bs4 import BeautifulSoup
from sentiment_analysis_spanish import sentiment_analysis

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

# Ejemplo de uso con la URL proporcionada
enlace_noticia = 'https://www.lne.es/asturias/2023/11/27/kamikaze-hizo-trayecto-enorme-velocidad-95133181.html'
texto_noticia = obtener_texto_enlace(enlace_noticia)
sentimiento = analizar_sentimientos(texto_noticia)

print(f'Sentimiento: {sentimiento}')
