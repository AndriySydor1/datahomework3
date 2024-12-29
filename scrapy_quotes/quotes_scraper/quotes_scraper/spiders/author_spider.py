import scrapy


class AuthorsSpider(scrapy.Spider):
    name = "authors"
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        # Знаходимо посилання на сторінки авторів
        author_links = response.css("div.quote span a::attr(href)").getall()
        for link in author_links:
            # Відвідуємо сторінки авторів для збору інформації
            yield response.follow(link, self.parse_author)

        # Переходимо на наступну сторінку цитат
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_author(self, response):
        # Збираємо інформацію про автора
        yield {
            "fullname": response.css("h3.author-title::text").get().strip(),
            "born_date": response.css("span.author-born-date::text").get(),
            "born_location": response.css("span.author-born-location::text").get(),
            "description": response.css("div.author-description::text").get().strip(),
        }
        