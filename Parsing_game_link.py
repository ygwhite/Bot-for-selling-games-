import requests
from bs4 import BeautifulSoup as bs
from sell import selling
def max_data(url):
    r = requests.get(url)
    soup = bs(r.text, 'lxml')
    try:
        name_max_edition = [x.text for x in soup.find_all('h3',class_='psw-t-title-s psw-t-align-c psw-fill-x psw-p-t-6 psw-p-x-7')]
        sell_max_edition = []
        for sel in soup.find_all('span', class_='psw-t-title-m')[1:]:
            if sel.text == 'Included' or sel.text == 'Game Trial' or sel.text == 'Free':
                continue
            else:
                sell_max_edition.append(selling(sel.text))
        libs_sell_and_name = list(zip(sell_max_edition, name_max_edition))
        max_edition_sell_and_name = max(libs_sell_and_name)
        return max_edition_sell_and_name
    except:
        print('none')

def standart_data(url):
    r = requests.get(url)
    soup = bs(r.text, 'lxml')
    game_ps5_sell = soup.find_all('span', class_='psw-t-title-m')[0].text
    return game_ps5_sell