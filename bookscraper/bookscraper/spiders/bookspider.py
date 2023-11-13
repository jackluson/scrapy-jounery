import scrapy
from bookscraper.items import BookItem
from urllib.parse import urlencode


# def get_proxy_url(url):
#     payload = {'api_key': API_KEY, 'url': url}
#     proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
#     return proxy_url

class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    # allowed_domains = ["books.toscrape.com", "proxy.scrapeops.io"]
    start_urls = ["https://books.toscrape.com", "http://books.toscrape.com?page=2"]
    
    custom_settings = {
        'FEEDS': {
            'booksdata.json': {'format': 'json', 'overwrite': True},
            'booksdata.csv': {'format': 'csv'},
        }
    }

    def parse(self, response):
        print('here in', response.url)
        books = response.css("article.product_pod")
        start = 0
        end = 2
        if 'page' in response.url:
            start = 2
            end = 4
        print("start", start, 'end', end, 'len', len(books))
        for book in books[start:end]:
            # title = book.xpath("./h3/a/@title").extract_first()
            # price = book.css("p.price_color::text").extract_first()
            # url = book.css("h3 a::attr(href)").extract_first()
            # yield {"title": title, "price": price, 'url': url}
            relative_url = book.css('h3 a::attr(href)').get()
            absolute_url = response.urljoin(relative_url)
            yield scrapy.Request(absolute_url, callback=self.parse_book)
            
        next_page = response.css("ul.pager li.next a::attr(href)").get()
        if next_page and None:
            next_page = response.urljoin(next_page)
            # yield response.follow(next_page, callback=self.parse)
            yield scrapy.Request(next_page, callback=self.parse)
    def parse_book(self, response):
        table_rows = response.css('table tr')
        book_item = BookItem()
        book_item['url'] = response.url
        book_item['title'] = response.css('.product_main h1::text').get()
        book_item['upc'] = table_rows[0].css('td::text').get()
        book_item['product_type'] = table_rows[1].css('td::text').get()
        book_item['price_excl_tax'] = table_rows[2].css("td ::text").get()
        book_item['price_incl_tax'] = table_rows[3].css("td ::text").get()
        book_item['tax'] = table_rows[4].css("td ::text").get()
        book_item['availability'] = table_rows[5].css("td ::text").get()
        book_item['num_reviews'] = table_rows[6].css("td ::text").get()
        book_item['stars'] = response.css("p.star-rating").attrib['class']
        book_item['category'] = response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get()
        book_item['description'] = response.xpath("//div[@id='product_description']/following-sibling::p/text()").get()
        book_item['price'] = response.css('p.price_color ::text').get()
        yield book_item
