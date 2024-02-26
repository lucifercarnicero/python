import scrapy
from dateutil.parser import parse

class NoticiasSpider(scrapy.Spider):
    name = 'noticias'
    allowed_domains = ['lavozdeasturias.es']
    start_urls = ['https://www.lavozdeasturias.es/actualidad/2']

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'noticias_2024.csv'
    }

    def parse(self, response):
        # Asumiendo que cada noticia está en un contenedor específico
       for noticia in response.css('.a-min-content'):
        enlace_noticia = noticia.css('a::attr(href)').get()
        if enlace_noticia:
            yield response.follow(enlace_noticia, self.parse_noticia)

        # Paginación (ajustar el selector según sea necesario)
        siguiente_pagina = response.css('a.btn-primary::attr(href)').get()
        if siguiente_pagina:
            yield response.follow(siguiente_pagina, self.parse)

    def parse_noticia(self, response):
        # Extraer la fecha y verificar si es de 2024
        fecha_texto = response.css('div.date::text').get()
        fecha = parse(fecha_texto, fuzzy=True)

        if fecha and fecha.year == 2024:
            yield {
                'titulo': response.css('h1.headline::text').get().strip(),
                'subtitulo': response.css('h3.subtitle::text').get().strip(),
                'autor': response.css('div.author-name::text').get().strip(),
                'texto': ' '.join(response.css('div.article-text p::text, div.article-text p em::text').getall()),
                'url': response.url,
                'fecha': fecha_texto.strip(),
                'categoria': response.css('h2.detalle_cliche_actualidad::text').get().strip(),
            }
