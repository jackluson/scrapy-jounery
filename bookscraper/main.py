'''
Desc:
File: /main.py
Project: bookscraper
File Created: Monday, 13th November 2023 8:25:45 pm
Author: luxuemin2108@gmail.com
-----
Copyright (c) 2023 Camel Lu
'''
from scrapy.crawler import CrawlerProcess
from bookscraper.spiders.bookspider import BookspiderSpider

if __name__ == '__main__':
  process = CrawlerProcess()
  process.crawl(BookspiderSpider)
  process.start()
