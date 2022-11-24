import requests
from bs4 import BeautifulSoup
import html.parser
from fake_useragent import UserAgent


def create_header():
    ua = UserAgent()
    fake_ua = {'user-agent': ua.random}
    return fake_ua


def yandex_search():
    url = 'https://yandex.ru/search/?text='
    return url


def get_yandex_search():
    user_input = input('Введите запрос : ')
    url = yandex_search() + user_input
    header = create_header()
    response = requests.get(url=url, headers=header)
    response.encoding = 'utf-8'
    return response


def google_search():
    pass


def main():
    response = get_yandex_search()
    soup = BeautifulSoup(response.content, 'html.parser')
    with open('yandex_search_out.html', 'w', encoding='utf-8') as search_file:
        search_file.write(str(soup.prettify()))
    

if __name__ == '__main__':
    main()
