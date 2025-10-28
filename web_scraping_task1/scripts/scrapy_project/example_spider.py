
# Minimal Scrapy spider example (place this inside a scrapy project's spiders/ directory).
import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'example'
    start_urls = ['https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population']

    def parse(self, response):
        # This is a minimal example to show where to extract data
        for row in response.css('table.wikitable tr')[1:]:
            yield {
                'country': row.css('td:nth-child(2) ::text').get(),
                'population': row.css('td:nth-child(3) ::text').get()
            }
