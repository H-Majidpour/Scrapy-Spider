import scrapy

class InitSpider(scrapy.Spider):
    name = "book_crawler"

    def start_requests(self):

        # Add the first five pages of the site to the list for requests
        url_list = []
        for i in range(2, 6):
            url_list.append("https://books.toscrape.com/catalogue/page-"+ str(i)+ ".html")


        urls =[]
        urls.append("https://books.toscrape.com/")
        for i in range(0, len(url_list)):
            urls.append(url_list[i])

        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)



        
    def parse(self, response):
        title_list = response.xpath("//article[@class = 'product_pod']/h3/a/text()").extract()
        price_list = response.xpath("//p[@class = 'price_color']/text()").extract()

        convert_list = dict(zip(title_list , price_list))
        book_list = list(convert_list.items())



        with open("project result/v1.2/Books.txt", 'a+') as Fin:

            for i, j in book_list:
                Fin.write( i + " >>> Price : " + j + "\n")
            Fin.close()