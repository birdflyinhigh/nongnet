# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy_redis.spiders import RedisCrawlSpider
class NongnetSpider(CrawlSpider):
    name = 'nongnet'
    allowed_domains = ['nongnet.com']
    start_urls = ['http://www.nongnet.com']
    rules = (
        # 大分类页面url
        Rule(LinkExtractor(allow=r'classi_[0-9]+\.aspx'), follow=True),
        # 商品列表页url
        Rule(LinkExtractor(allow=r'list_.+\.aspx'), follow=True),
        # 商品url
        Rule(LinkExtractor(allow=r'http://www.nongnet.com/xinxi/[0-9]+\.aspx'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response.url)
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
