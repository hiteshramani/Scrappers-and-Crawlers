# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor


class ExampleSpider(CrawlSpider):
    name = "wisdomgeek"
    allowed_domains = ["wisdomgeek.com"]
    start_urls = ["http://www.wisdomgeek.com/"]
    rules = [Rule(SgmlLinkExtractor(), callback='parse_item', follow=True)]

    def parse_item(self,response):
        self.log('A response from %s just arrived!' % response.url)
