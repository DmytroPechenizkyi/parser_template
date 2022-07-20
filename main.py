from parse import parse_page
import csv

URL = 'https://rozetka.com.ua/notebooks/c80004/'
# in this file we create a logic to parse a web page


def get_list(url):
    count = 1
    info_list = []
    soup = parse_page(url)
    laptops = soup.find_all('div', class_='goods-tile__inner')
    for laptop in laptops:
        name = laptop.find('span', class_='goods-tile__title').get_text()[9:]
        info_link = laptop.find('a', class_='goods-tile__heading ng-star-inserted').get('href')
        get_price = laptop.find('span', class_='goods-tile__price-value').get_text()
        garbage = get_price[-5:-6:-1]
        price = get_price.replace(garbage, ' ')
        page_soup = parse_page(info_link)
        characteristics_list = page_soup.find('dl', 'characteristics-full__list')
        key_list = characteristics_list.find_all('span')
        value_list = characteristics_list.find_all('li')
        info_list.append({'Имя': name, 'Цена': price, 'Детальная информация': info_link,
                          key_list[0].text: value_list[0].text, key_list[1].text: value_list[1].text,
                          key_list[2].text: value_list[2].text, key_list[3].text: value_list[3].text,
                          key_list[6].text: value_list[6].text})
    for element in info_list:
        print(count, ':')
        for item in element.items():
            print(item)
        print('\n')
        count += 1
    with open('info_list.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        for element in info_list:
            writer.writerow(f'{count}:')
            for item in element.items():
                writer.writerow(item)
            writer.writerow('\n\n')
            count += 1


get_list(URL)
