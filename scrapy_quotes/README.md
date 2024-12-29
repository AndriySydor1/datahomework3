# Scrapy Quotes

## Опис

Цей проєкт виконує скрапінг сайту [Quotes to Scrape](http://quotes.toscrape.com), отримуючи:

1. Цитати разом із тегами.
2. Інформацію про авторів цитат.

## Інструкція з запуску

### Підготовка

1. Перейдіть до папки `scrapy_quotes/quotes_scraper`:
   cd scrapy_quotes/quotes_scraper
2. Створіть папку data для збереження результатів (якщо вона ще не існує):
   mkdir data

### Запуск павуків

1. Зібрати цитати:
   scrapy crawl quotes -o data/quotes.json
2. Зібрати авторів:
   scrapy crawl authors -o data/authors.json

## Збережені файли

data/quotes.json — інформація про цитати.
data/authors.json — інформація про авторів.

## Залежності

Python 3.10+
Scrapy
