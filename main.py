from parse import parse_page
import json
import re

URL = 'https://www.gov.pl/web/poland-businessharbour-en/itspecialist'
# in this file we create a logic to parse a web page


def get_json(url):
    soup = parse_page(url)
    json_dict = {}
    titles = soup.find_all('summary')
    for i in range(len(titles)):
        organization_dict = {}
        block = titles[i].find_next()
        content = block.find_all('p')
        for element in content:
            if re.search(r'www:|WWW:', element.text):
                url = element.find('a').get('href')
                organization_dict.update({'url': url})
            else:
                email = element.text
                exception_list = ['e-mail: ', 'Mail: ', 'Contact: ', 'e-mail:\xa0']
                for exception in exception_list:
                    email = email.replace(exception, '')
                    organization_dict.update({'e-mail': email})
        json_dict.update({titles[i].text.replace('\xa0', ' '): organization_dict})
    with open('info.json', 'w', encoding='utf-8') as file:
        json.dump(json_dict, file, indent=4, ensure_ascii=False)


get_json(URL)
