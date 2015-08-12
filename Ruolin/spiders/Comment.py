# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from Ruolin.items import RuolinItem

import re

class CommentSpider(CrawlSpider):
    name = 'Comment'
    allowed_domains = ['wealink.com']
    start_urls = ['http://www.wealink.com/gongsi/']

    rules = (
        Rule(LinkExtractor(allow=r'gongsi/([\d\w]+)\_s/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        companies = response.xpath("//ul[@class='zw-list']/li")
        for company in companies:
            i = RuolinItem()
            i['name'] = company.xpath('div/div/h4/a/text()').extract()[0]
            i['addr'] = company.xpath("div/div/h4/span[@class='clr-999']/text()").extract()[0]
            comment_expert = company.xpath("div/div[@class='right-ctrl right-ctrl2']")
            i['comment_num'] = comment_expert.xpath("p/a[@rel='nofollow']/text()").extract()[0]
            star_on = comment_expert.xpath("p/i[@class='star-off']/i[@class='star-on']/@style").extract()[0]
            i['average_point'] = self.convertRate(star_on)
            yield i

    def convertRate(self, rate):
        return int(re.match(r'width:(\d+)%', rate).group(1)) * 5 / 100

