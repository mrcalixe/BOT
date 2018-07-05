from bs4 import BeautifulSoup
import requests
import urllib.request

base_url = 'http://www.livescore.com/worldcup/'




def get_data_url(url=base_url):
    r = urllib.request.urlopen(url)
    soup = BeautifulSoup(r.read(), 'html.parser')
    return soup

def get_fst_match():
    soup = get_data_url()
    for link in soup.find_all('div'):
        if link.get('class') == ["md"] and link.get('data-type') == 'match':
            print("Found")
            match_id = link.get('data-id')
            match_url = 'http://www.livescore.com/worldcup/match/?match='+match_id
            return match_url

    return None

def get_match_info(match_url):
    home = ""
    away = ""
    score = ""
    soup = get_data_url(match_url)
    for link in soup.find_all('div'):
        if link.get('class') == ['ply', 'tright'] and link.get('data-type') == ['home-team']:
            home = link.contents
        if link.get('class') == ['ply'] and link.get('data-type') == ['away-team']:
            away = link.contents
        if link.get('class') == ['sco']:
            for st in link.stripped_strings:
                score = ''.join(repr(st))
    return home,away, score


print(get_data_url())