from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup as bs

URL = "https://store.steampowered.com/search/results?force_infinite=1&maxprice=free&supportedlang=english&specials=1"
SPECIAL_GAME = []


@dataclass
class Game:
    url: str
    title: str
    img_url: str
    description: str


def special_offer():
    data = requests.get(URL)
    soup = bs(data.content, 'html5lib')

    table = soup.find("div", attrs={'id': 'search_resultsRows'})

    for row in table.findAll('a', attrs={'class': 'search_result_row'}): # type: ignore
        game_page = requests.get(row['href'])
        page_data = bs(game_page.content, 'html5lib')
        metas = page_data.find("meta", attrs={'name': 'Description'})
        
        SPECIAL_GAME.append(Game(
            row['href'],
            row.span.text,
            row.img['src'],
            metas['content'] # type: ignore
        ))

    return SPECIAL_GAME
