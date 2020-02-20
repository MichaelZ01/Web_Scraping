import requests
from bs4 import BeautifulSoup



if __name__ == '__main__':
    
    url = "https://store.steampowered.com/"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    final_price =soup.find_all('div', class_ ="discount_final_price")
    original_price =soup.find_all('div', class_ ="discount_original_price")
    item_name =soup.find_all('div', class_ ="tab_item_name")

    print(original_price)
    print(final_price)
    print(item_name)