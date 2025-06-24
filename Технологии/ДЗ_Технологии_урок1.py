import re


def get_words(filename: str) -> list:
    with open(filename, 'r', encoding="utf-8") as f:
        words = f.read().lower()
        words = re.sub(r'[^\w\s]', '', words).split()
    return words


def get_words_dict(words: list) -> dict:
    dct = {}
    for word in words:
        dct[word] = dct.get(word, 0) + 1
    dct = dict(sorted(dct.items(), key=lambda x: x[1], reverse=True))
    return dct


file_name = 'Письмо к женщине.txt'
words_list = get_words(file_name)
print(f'Название файла - {file_name}')
print(f'Количество слов - {len(words_list)}')
words_dict = get_words_dict(words_list)
print(f'Количество уникальных слов - {len(words_dict)}')
print('Все использованные слова:')
for item in words_dict.items():
    print(*item)

