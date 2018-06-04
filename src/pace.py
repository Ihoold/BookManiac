import os
from math import floor
from os import path

from lib import file_to_sentences


data_path = 'Ksiazki'
list_file_name = 'features_2.csv'
new_list_file_name = 'features_3.csv'

if __name__ == '__main__':
    os.chdir(data_path)
    with open(list_file_name) as old_list:
        with open(new_list_file_name, 'w') as new_list:
            i = 0
            for line in old_list:
                if i % 100 == 0:
                    print(i)
                i += 1

                avg_words = []
                book_id = [x.strip() for x in line.strip().split(';')][0]
                print(path.join(data_path, book_id+ '.txt'))
                try:
                    for sentence in file_to_sentences(path.join(data_path, book_id + '.txt')):
                        avg_words.append(len(sentence.split()))
                except FileNotFoundError:
                    continue

                length = len(avg_words)
                if length < 100:
                    continue

                paces = [sum(avg_words) / len(avg_words)]
                for i in range(0, 100, 10):
                    pos_start = floor(length * i / 100)
                    pos_end = floor(length * (i + 10) / 100)
                    paces.append(sum(avg_words[pos_start:pos_end]) / (pos_end - pos_start))

                new_list.write(line.strip() + ' ; ' + ' ; '.join([str(round(x, 5)) for x in paces]) + '\n')