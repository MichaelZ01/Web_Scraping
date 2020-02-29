# A program that scrapes game prices from steam's main page

import requests
from bs4 import BeautifulSoup

def print_new_price(name, old_price, new_price):
    print(name.text + '   ' + old_price.text + '   ' + new_price.text)

def print_old_price(name, old_price):
    print(name.text + '   ' + old_price.text)


if __name__ == '__main__':
    
    url = "https://store.steampowered.com/"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    # Extract main page games
    home_page_content = soup.find('div', class_ = "home_tabs_content")
    #game_tabs = home_page_content.find('div', class_ = 'tab_content')


    # Each hyperlink represents a game
    for game in home_page_content.find_all('a'):
        #print(game.attrs)
         if 'hidden' in game.attrs['class']: #stops hidden games from showing up
            continue
         else:    
        # Extract game name and price
            game_name = game.find('div', class_ = 'tab_item_name')
            old_price = game.find('div', class_ = 'discount_original_price')
            new_price = game.find('div', class_ = 'discount_final_price')

        # If the game had an original price
            if old_price is not None:
                print_new_price(game_name, old_price, new_price)
            else:
                print_old_price(game_name, new_price)


'''
    final_price =soup.find_all('div', class_ ="discount_final_price")


    original_price =soup.find_all('div', class_ ="discount_original_price")
    item_name =soup.find_all('div', class_ ="tab_item_name")

    print(game_tabs.prettify())

    #print(original_price)
    #print(final_price)
    #print(item_name)
'''
