# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class Python04Pipeline(object):
    def process_item(self, item, spider):
        return item


class ValidarMacbook(object):
    def process_item(self, item, spider):
        print(item['titulo'])
        if 'iphone' not in item['titulo'].lower():
            item['titulo'] = 'No iPhone'
            raise DropItem('No es iphone')
        return item

class ValidarPrecio(object):
    def process_item(self, item, spider):
        print('>>> ', item)
        precio = float(item['precio'].replace('$', ''))
        if (precio < 10):
            item['precio'] = 'Muy barato'
            raise DropItem('Muy barato')
        return item


class MarcarComoViable(object):
    def process_item(self, item, spider):
        if item['titulo'] != 'No iPhone' and item['precio'] != 'Muy barato':
            print("\n\n Item encontrado")
            print('Titulo', item['titulo'])
        return item