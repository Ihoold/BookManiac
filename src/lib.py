import re


def file_to_sentences(filename):
    with open('/home/ihoold/git/programming/magisterka/' + filename, encoding='ISO-8859-2') as text_file:
        prev_line = ''
        for line in text_file:
            sentences = re.split(r'[!.?]', line)
            prev_line += sentences[0]
            if len(sentences) == 1:
                # None sentence was processed.
                continue
            if prev_line != '':
                yield prev_line.strip()

            for sentence in sentences[1:-1]:
                # Sentences mid-line
                if sentence != '':
                    yield sentence.strip()

            prev_line = sentences[-1]
