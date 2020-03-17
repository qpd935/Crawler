
import scrapy
from scrapy.spiders.feed import XMLFeedSpider
class DaliySpider(scrapy.spiders.Spider):
    name = "zhd"
    allowed_domains = ['cbss.10010.com']
    start_urls = ['https://cbss.10010.com/essframe']
    
    def parse(self, response):
        file_name = 'file.html'
        with open(file_name, 'wb') as f:
            f.write(response.body)
            while True:
                pass
            