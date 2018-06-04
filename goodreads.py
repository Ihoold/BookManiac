import time
from xml.etree import ElementTree

import requests
import os


search_url = 'https://www.goodreads.com/search/index.xml'
data_path = 'Ksiazki'
list_file_name = 'features_1.csv'
new_list_file_name = 'features_2.csv'

if __name__ == '__main__':
    os.chdir(data_path)
    with open(list_file_name) as old_list:
        with open(new_list_file_name, 'w') as new_list:
            i = 0
            for line in old_list:
                if i % 100 == 0:
                    print(i)
                i += 1
                id, title, authors = [x.strip() for x in line.strip().split(';')]
                params = {'key': 'exuNbWaEgnJX1RcU1xHjg', 'q': '{} {}'.format(title, ' '.join(authors.split(',')))}
                time.sleep(0.5)
                page = requests.get(search_url, params)
                tree = ElementTree.fromstring(page.content)
                try:
                    work = tree[1][6][0]
                    if str(work[2].text) == '0':
                        continue
                    new_list.write(' ; '.join([id, title, authors, work[0].text, str(work[2].text), str(int(round(float(work[7].text) * 100)))]) + '\n')
                except IndexError:
                    continue
