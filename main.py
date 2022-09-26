import requests
from parse import parse_page
from threading import Thread
from lxml import html

URL = 'https://amf.ua/kresla/konferenckresla/'
# in this file we create a logic to parse a web page


def get_info(chair):
    info_dict = {}
    name = chair.find('span', class_='title').get_text()
    price = chair.find('strong').get_text()
    info_dict.update({'имя': name, 'цена': price})
    print(info_dict)
    return info_dict


def get_all_chairs():
    threads = []
    soup = parse_page(URL)
    chairs = soup.find_all('div', class_='product-block')
    for chair in chairs:
        t = Thread(target=get_info, args=(chair,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()


# def get_all_chairs():
#     soup = parse_page(URL)
#     chairs = soup.find_all('div', class_='product-block')
#     for chair in chairs:
#         get_info(chair)


get_all_chairs()

