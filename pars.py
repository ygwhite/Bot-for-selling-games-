import requests
from bs4 import BeautifulSoup as bs

ps_list_game = []
ps_link_game = []
ps_image_game = []

for page in range(1, 20):
    url = f'https://store.playstation.com/en-tr/pages/browse/{page}'
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    for ps_game in soup.find_all('li', class_='psw-l-w-1/2@mobile-s psw-l-w-1/2@mobile-l psw-l-w-1/6@tablet-l psw-l-w-1/4@tablet-s psw-l-w-1/6@laptop psw-l-w-1/8@desktop psw-l-w-1/8@max'):
        ps_list_game.append(ps_game.text)
    for link in soup.find_all('a', class_='psw-link psw-content-link'):
        ps_link_game.append('https://store.playstation.com' + link.get('href'))
    for image in soup.find_all('img',class_='psw-blur psw-top-left psw-l-fit-cover'):
        image_link = image.get('src')
        image_s_link = image_link.replace('?w=54&thumb=true', ' ')
        ps_image_game.append(image_s_link)
def flatten(xss):
    return [x for xs in xss for x in xs]

libs = dict(zip(ps_list_game, ps_link_game))
libs_image = dict(zip(ps_list_game, ps_image_game))



