import scrapy
from ..items import PostalCodesItem


class PostalCodesSpider(scrapy.Spider):
    name = 'postal_codes'
    start_urls = ['https://worldpostalcode.com/india/madhya-pradesh/jabalpur/']

    def parse(self, response):
        container_div_tags = response.css('.container')
        items = PostalCodesItem()

        for container in container_div_tags:
            place = container.css('.place::text').extract_first()
            code = container.css('.code').css('span::text').extract_first()

            items['place'] = place
            items['postCode'] = code
            yield items
