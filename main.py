import requests
from bs4 import BeautifulSoup
import html.parser
from fake_useragent import UserAgent
import webbrowser as wb

def create_header():
    ua = UserAgent()
    fake_ua = {'user-agent': ua.random}
    return fake_ua


def yandex_search():
    url = 'https://yandex.ru/search/?text='
    return url

def google_search():
    url = "https://search.sapti.me/search?q="
    return url


def get_yandex_search():    # ? reworked function
    user_input = input('Введите запрос : ')
    url = yandex_search() + user_input
    header = create_header()
    response = requests.get(url=url, headers=header)
    response.encoding = 'utf-8'
    return response


def get_google_search():    # ? reworked function
    user_input = input('Введите запрос : ')
    url = google_search() + user_input
    # wb.open(url)
    header = create_header()
    response = requests.get(url=url, headers=header)
    response.encoding = 'utf-8'
    return response


def main():
    response = get_google_search()
    soup = BeautifulSoup(response.content, 'html.parser')
    searching_result = set([x['href'] for x in soup.find('div', id='urls').find_all('a')])
    with open('google_search_out.html', 'w', encoding='utf-8') as search_file:
        search_file.write(str(soup.prettify()))
    print(searching_result)


if __name__ == '__main__':
    main()
