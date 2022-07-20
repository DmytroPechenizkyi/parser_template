import requests
from bs4 import BeautifulSoup


def parse_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/99.0.4844.82 Safari/537.36'
    }
    request = requests.get(url, headers=headers)
    soup = BeautifulSoup(request.content, 'lxml')
    return soup



