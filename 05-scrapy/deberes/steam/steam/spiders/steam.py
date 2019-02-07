import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst
from steam.items import SteamItem

class DetalleJuego(scrapy.Spider):
    name = 'steam_processor'
    start_urls = [
        'file:///C:/Users/rprado/AppData/Local/Temp/tmprey8zr0v.html'
    ]

    def parse(self, response):
        resultados_busqueda = response.css('#NewReleasesRows > a')
        for juego in resultados_busqueda:
            juego_loader = ItemLoader(item=SteamItem(), selector=juego)
            juego_loader.default_output_processor = TakeFirst()
            juego_loader.add_css('name', '.tab_item_content > .tab_item_name::text')
            juego_loader.add_css('discount', '.tab_item_discount > .discount_pct::text')
            juego_loader.add_css('final_price', '.tab_item_discount > .discount_prices > .discount_final_price::text')
            juego_loader.add_css('original_price', '.tab_item_discount > .discount_prices > .discount_original_price::text')
            # juego_loader.add_css('tags', '.tab_item_content > .tab_item_details > .tab_item_top_tags > span::text')
            tags = juego_loader.selector.css('.tab_item_content > .tab_item_details > .tab_item_top_tags > span::text').extract()
            print(tags)
            juego_loader.add_value('tags', tags)
            yield juego_loader.load_item()