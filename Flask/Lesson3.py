import requests
from collections import Counter

errors_dict = {403: 'Превышение лимита запросов.',
               404: 'Неверное имя пользователя',
               500: 'Ошибка сервера.'}


def get_repos(us_name):
    url = f"https://api.github.com/users/{us_name}/repos"
    return requests.get(url)



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
        repo = get_repos(username)
        if repo.status_code != 200:
            print(f'Запрос завершен с ошибкой {repo.status_code} - {errors_dict[repo.status_code]}.')
            continue
        repos = repo.json()
        if not repos:
            print('У этого пользователю не найдено ни одного доступного репозитория')
            continue
        stat = analyze_repos(repos)
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
