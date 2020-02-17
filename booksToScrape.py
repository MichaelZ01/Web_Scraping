# A program that scrapes the scraping practice website http://books.toscrape.com

# 

# Import requests and beautiful soup to scrape and interact with html from site
import requests
from bs4 import BeautifulSoup



if __name__ == '__main__':
    
    url = "http://books.toscrape.com/catalogue/category/books_1/index.html"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    #results = soup.find(class='messages')

    print(soup.prettify())