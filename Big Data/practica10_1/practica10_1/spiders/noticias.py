import scrapy
from datetime import datetime

class NoticiasSpider(scrapy.Spider):
    name = 'noticias'
    allowed_domains = ['lavozdeasturias.es']
    start_urls = ['https://www.lavozdeasturias.es/actualidad']

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'noticias_2024.csv',
        'FEED_EXPORT_ENCODING': 'utf-8',
        'FEED_EXPORTERS': {
            'csv': 'scrapy.exporters.CsvItemExporter',
        },
        'FEED_EXPORT_PARAMS': {
            'delimiter': ';'  # Change ';' to the delimiter you want to use
        }
    }

    def parse(self, response):
        for noticia in response.css('.a-min-content'):
            enlace_noticia = noticia.css('a::attr(href)').get()
            if enlace_noticia:
                yield response.follow(enlace_noticia, self.parse_noticia)

        siguiente_pagina = response.css('a.btn-primary::attr(href)').get()
        if siguiente_pagina:
            yield response.follow(siguiente_pagina, self.parse)

    def parse_noticia(self, response):
        fecha_texto = response.css('span.sz-t-xs strong::text').get()
        if fecha_texto:
            try:
                meses_es_a_en = {
                    'ene': 'Jan', 'feb': 'Feb', 'mar': 'Mar', 'abr': 'Apr',
                    'may': 'May', 'jun': 'Jun', 'jul': 'Jul', 'ago': 'Aug',
                    'sep': 'Sep', 'oct': 'Oct', 'nov': 'Nov', 'dic': 'Dec'
                }

                for es, en in meses_es_a_en.items():
                    if es in fecha_texto:
                        fecha_texto = fecha_texto.replace(es, en)
                        break

                fecha = datetime.strptime(fecha_texto, '%d %b %Y')
                if fecha.year == 2024:
                    autor_texto = response.css('span.author.sz-t-xxs.t-bld.upper a::text').get()
                    autor = autor_texto.strip() if autor_texto else 'Autor no encontrado'

                    categoria_texto = response.css('a.mg-l::text').get()
                    categoria = categoria_texto.strip() if categoria_texto else 'Categoría no encontrada'
                    texto = response.xpath('//p[@class="first-paragraph txt"]//text()').getall()
                    texto = ' '.join(texto).strip()

                    yield {
                        'titulo': response.css('h1.headline::text').get().strip(),
                        'subtitulo': response.css('h3.subtitle::text').get().strip(),
                        'autor': autor,
                        'texto': texto,
                        'url': response.url,
                        'fecha': fecha_texto.strip(),
                        'categoria': categoria,
                    }
                else:
                    self.logger.info(f"Deteniendo el proceso debido a una noticia de {fecha.year}")
                    raise scrapy.exceptions.CloseSpider(reason='Noticia de año anterior a 2024')
            except ValueError as e:
                self.logger.error(f"Error parsing date from string '{fecha_texto}': {e}")
        else:
            self.logger.error(f"No date found in response: {response.url}")
