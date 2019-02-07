import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst
from python_04.items import ProductoItem


def truncar_text(texto):
    return texto[:50]

class DetalleProducto(scrapy.Spider):
    name = 'input_processor'
    start_urls = [
        'file:///C:/Users/rprado/AppData/Local/Temp/tmp3f_61gj3.html'
    ]
    def parse(self, response):
        resultados_busqueda = response.css('ul.s-result-list > li')
        for producto in resultados_busqueda:
            producto_loader = ItemLoader(item=ProductoItem(), selector=producto)

            producto_loader.default_input_processor = MapCompose(truncar_text)
            producto_loader.default_output_processor = TakeFirst()

            titulo = producto_loader.add_css('titulo', '.s-access-title::text')
            precio = producto_loader.add_css('precio', '.sx-price-whole::text')
            link = producto_loader.add_css('link', 'a.s-access-detail-page::attr(href)')
            yield producto_loader.load_item()
