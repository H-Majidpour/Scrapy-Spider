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


        with open("project result/v1.1/Books.txt", 'a+') as Fin:

            for i in range(0, len(title_list)):
                Fin.write(str(i) + " : " + title_list[i] + "\n")
            Fin.close()