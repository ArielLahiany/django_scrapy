# Scrapy modules.
from scrapy import Spider

# marionette modules
from django_scrapy.crawler.items import QuoteItem


class QuoteSpider(Spider):
    """
    QuoteSpider:
    """

    name = "quote"
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response, **kwargs):
        """

        :param response:
        :param kwargs:
        :return:
        """

        item = QuoteItem()

        item["quote"] = response.css("div.quote span.text::text").extract_first()
        item["author"] = response.css("small.author::text").extract_first()

        yield item
