import requests
from bs4 import BeautifulSoup
import csv
import os
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module='bs4')


def extract_image_url(item):
    # Intenta encontrar la URL de la imagen en el elemento enclosure
    image_url = item.find('enclosure')['url'] if item.find('enclosure') else None
    
    # Si no se encuentra la URL de la imagen en enclosure, busca en el contenido de la descripción
    if not image_url and item.description:
        description_soup = BeautifulSoup(item.description.text, 'html.parser')
        img_tag = description_soup.find('img')
        if img_tag and 'src' in img_tag.attrs:
            image_url = img_tag['src']

    return image_url

def extract_rss_feed(feed_url, writer, start_id, source):
    response = requests.get(feed_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('item')

    for item in items:
        title = item.title.text if item.title else 'No Title'
        link = item.link.text if item.link else 'No Link'
        pubDate = item.pubDate.text if item.pubDate else 'No Publication Date'
        description = item.description.text if item.description else 'No Description'
        categories = [category.text for category in item.find_all('category')] if item.find_all('category') else ['No Categories']
        
        # Extraer la URL de la imagen
        image_url = extract_image_url(item)

        writer.writerow({
            'Id': start_id,
            'Title': title,
            'URL': link,
            'Date': pubDate,
            'Description': description,
            'Categories': categories,
            'Image URL': image_url,
            'Source': source
        })

        if image_url:
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                with open(os.path.join('Imagenes', f'image_{start_id}.jpg'), 'wb') as f:
                    f.write(image_response.content)

        start_id += 1

    return start_id

if not os.path.exists('Imagenes'):
    os.makedirs('Imagenes')

with open('noticias.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Id', 'Title', 'URL', 'Date', 'Description', 'Categories', 'Image URL', 'Source']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    start_id = 1
    el_pais_rss = 'https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/section/ultimas-noticias/portada'
    start_id = extract_rss_feed(el_pais_rss, writer, start_id, 'El País')

    el_mundo_rss = 'https://e00-elmundo.uecdn.es/elmundo/rss/portada.xml'
    extract_rss_feed(el_mundo_rss, writer, start_id, 'El Mundo')
