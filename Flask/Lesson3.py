import requests
from collections import Counter

errors_dict = {403: 'Превышение лимита запросов.',
               404: 'Неверное имя пользователя',
               500: 'Ошибка сервера.'}


def get_repos(rep):
    rep_list = []
    for i in rep:
        rep_list.append(i['name'])
    return rep_list


def analyze_repos(rep):
    dct = {}
    lst = []
    for i in rep:
        dct['count'] = dct.get('count', 0) + 1
        dct['stars'] = dct.get('stars', 0) + i['stargazers_count']
        if dct.get('best_rep', ['', 0])[1] < i['stargazers_count']:
            dct['best_rep'] = [i['name'], i['stargazers_count']]
        lst.append(i['language'])
    dct['list_language'] = Counter(lst)
    return dct


def main():
    while True:
        username = input('Введите пользователя репозитория для получения информации.')
        url = f"https://api.github.com/users/{username}/repos"
        response = requests.get(url)
        if response.status_code != 200:
            print(f'Запрос завершен с ошибкой {response.status_code} - {errors_dict[response.status_code]}.')
        else:
            repo = response.json()
            print(f'Список доступных репозиториев пользователя {username}: {get_repos(repo)}')
            stat = analyze_repos(repo)
            print(f'- Количество публичных репозиториев: {stat["count"]}\n'
                  f'- Общее количество звёзд: {stat["stars"]}\n'
                  f'- Топ языков программирования:')
            [print(f'{i[0]}: {i[1]} репозитори{["й", "я", "ев"][(i[1] > 1) + (i[1] > 4)]}') for i in
             stat['list_language'].items()]
        if input('Хотите продолжить? Все кроме "да" прервет сессию.').lower() != 'да':
            break


main()

access_key = 'mi76aFMdgvml'
ogrn = '1027700132195'

response = requests.get(
    f'https://api.datanewton.ru/v1/counterparty?key={access_key}&filters=OWNER_BLOCK%2CADDRESS_BLOCK&ogrn={ogrn}')

resp = response.json()
print(f'Компания: {resp["company"]["company_names"]["short_name"]}\n'
      f'Адресс: {resp["company"]["address"]["line_address"]}\n'
      f'Статус предприятия: {resp["company"]["status"]["status_egr"]}\n'
      f'Список учередителей: {resp["company"]["owners"]}\n'
      f'''Уставной капитал: {f'{float(resp["company"]["charter_capital"]): ,.0f}'.replace(",", " ")} рублей.''')