import requests
from collections import Counter

errors_dict = {403: 'Превышение лимита запросов.',
               404: 'Неверное имя пользователя',
               500: 'Ошибка сервера.'}


def get_repos(us_name):
    url = f"https://api.github.com/users/{us_name}/repos"
    return requests.get(url)



def analyze_repos(repositories):
    stats = {
        'count': len(repositories),
        'stars': 0,
        'best_repo': ('', 0),
        'languages': Counter()
        }
    for repo in repositories:
        stats['stars'] += repo['stargazers_count']
        if  repo['stargazers_count'] > stats['best_repo'][1]:
            stats['best_repo'] = (repo['name'], repo['stargazers_count'])
        stats['languages'][repo['language']] += 1
    return stats


def main():
    while True:
        username = input('Введите пользователя репозитория для получения информации.')
        repo = get_repos(username)
        if repo.status_code != 200:
            print(f'Запрос завершен с ошибкой {repo.status_code} - {errors_dict.get(repo.status_code, "Неизвестная ошибка")}.')
            continue
        repos = repo.json()
        if not repos:
            print('У этого пользователю не найдено ни одного доступного репозитория')
            continue
        stat = analyze_repos(repos)
        print(f'- Количество публичных репозиториев: {stat["count"]}\n'
              f'- Общее количество звёзд: {stat["stars"]}\n'
              f'- Топ языков программирования:')
        [print(f'{item[0]}: {item[1]} репозитори{["й", "я", "ев"][(item[1] > 1) + (item[1] > 4)]}') for item in
         stat['languages'].items()]
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
