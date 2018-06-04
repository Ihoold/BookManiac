import os
import re

data_path = '../Ksiazki'
list_file_name = 'spis.csv'
new_list_file_name = 'features_1.csv'

if __name__ == '__main__':
    os.chdir(data_path)
    with open(list_file_name) as book_list:
        with open(new_list_file_name, 'w') as new_list:
            for line in book_list:
                match = re.match(r',?,?\'?\"?(?P<name>.*) - (?P<authors>.*) ?\((?P<number>[0-9]*)\)\)?\'?\"?,?,?',
                                 line, re.UNICODE)
                if match:
                    new_list.write(' '.join([match.group('number'), ';', match.group('name').replace(';', ''), ';',
                                             match.group('authors').replace(';', ''), '\n']))
                else:
                    print(line.strip('\n'))
