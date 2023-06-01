import scrapy
from myproject.items import MyprojectItem
from scrapy.crawler import CrawlerProcess

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://www.tuhocweb.com/gioi-thieu-va-cai-dat-composer-don-gian-cho-nguoi-moi-bat-dau-110.html']

    def parse(self, response):
        # Extract blog posts
        blog_posts = response.css('div.content')

        for post in blog_posts:
            # Extract blog title
            title = post.css('h1::text').get()

            # Extract blog content
            content = post.css('#div-ct').get()

            # Extract source
            source = post.css('.blog-source').get()
            print(title)
            # Create a dictionary to store the extracted data
            item = MyprojectItem()
            item['title'] = title
            item['content'] = content
            item['source'] = source
            yield item
class MySpider2(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://azdigi.com/blog/linux-server/webserver/them-website-vao-lamp-stack-tren-ubuntu-22-04/']

    def parse(self, response):
        # Extract blog posts
        blog_posts = response.css('div.blog')

        for post in blog_posts:
            # Extract blog title
            title = post.css('h1::text').get()

            # Extract blog content
            content = post.css('#div-blog').get()

            # Extract source
            source = post.css('.source').get()
            print(title)
            # Create a dictionary to store the extracted data
            item = MyprojectItem()
            item['title'] = title
            item['content'] = content
            item['source'] = source
            yield item
# Create a list of spider instances
spiders = [MySpider, MySpider2]

# Create a CrawlerProcess and pass the spider instances
process = CrawlerProcess()
for spider in spiders:
    process.crawl(spider)
process.start()