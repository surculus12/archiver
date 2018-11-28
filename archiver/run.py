import scrapy
import config


class Archiver(scrapy.Spider):
    name = 'archiver'
    http_user = config.user
    http_pass = config.password
    start_urls = [config.host + config.uri]

    def parse(self, response):
        for file_ in response.css("li.gallerybox"):
            break  # TODO: Re-enable for downloading all files + filter
            yield scrapy.Request(url=config.host + file_.css("a::attr(href)").extract_first(),
                                 callback=self.save_pdf)
        next_page = response.css("a.mw-nextlink::attr(href)").extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page))

    def save_pdf(self, response):
        # TODO: Write + tagging
        path = response.url.split('File:')[1]
        print("Saving", path)

if __name__ == '__main__':
    from scrapy.crawler import CrawlerProcess
    process = CrawlerProcess({'USER_AGENT': config.user_agent})
    process.crawl(Archiver)
    process.start()
