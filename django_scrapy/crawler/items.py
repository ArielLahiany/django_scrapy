# Scrapy modules
from scrapy import Item, Field


class QuoteItem(Item):
    """
    Quote base scraped item.
    """

    quote = Field()
    author = Field()
