# Python modules
import os

# Django modules.
from django.core.management.base import BaseCommand

# Scrapy modules.
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# Marionette modules.
from django_scrapy.crawler.spiders.quote import QuoteSpider


class Command(BaseCommand):
    help = "Crawler run command."

    def handle(self, *args, **options):
        """

        :param args:
        :param options:
        :return:
        """

        process = CrawlerProcess(get_project_settings())
        process.crawl(QuoteSpider)
        process.start()
