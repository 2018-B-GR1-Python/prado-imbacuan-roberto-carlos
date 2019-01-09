import scrapy

nombre_archivo = 'book_titles.txt'

class MiPrimerSpider(scrapy.Spider):
    name = 'introduccion_spider'

    def start_requests(self):
        urls = [
            'http://books.toscrape.com/catalogue/page-1.html',
            'http://books.toscrape.com/catalogue/page-2.html',
            'http://books.toscrape.com/catalogue/page-3.html',
            'http://books.toscrape.com/catalogue/page-4.html',
            'http://books.toscrape.com/catalogue/page-5.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # // *[ @ id = "default"] / div / div / div / div / section / div[2] / ol / li[1] / article / h3 / a
        # print(response.xpath("//*[@id='default']/div/div/div/div/section/div[2]/ol/li/article/h3/a/text()").extract())
        # print(response.css('.product_pod > h3 > a::text').extract())
        print('\n')
        titles = response.xpath("//article/h3/a/text()").extract()
        print(len(titles))

        prices = response.css('.product_pod > .product_price > .price_color::text').extract()
        print(len(prices))


        # //*[@id="default"]/div/div/div/div/section/div[2]/ol/li[1]/article/div[2]/p[2]/i
        # //*[@id="default"]/div/div/div/div/section/div[2]/ol/li[1]/article/div[2]/p[2]
        stock = response.xpath("//article/div[@class='product_price']/p[@class='instock availability']/text()").extract()

        stock.remove('\n    ')
        print(stock)

        f = open("data.txt", "a+")
        count = 0
        for index, title in enumerate(titles):
            if "In" not in stock[index]:
                stock[index] = True
            else:
                stock[index] = False

            f.write(f"{titles[index]}, {prices[index]}, {stock[index]}\n")
        f.close()
