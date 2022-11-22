import requests
from bs4 import BeautifulSoup
import lxml
from fake_useragent import UserAgent

def createHeader():
    ua = UserAgent()
    fake_ua = {'user-agent': ua.random}
    return fake_ua

def yandexSearch():
    url = 'https://yandex.ru/search/?text='
    return url

def getYandexSearch():
    user_input = input('Введите запрос : ')
    url = yandexSearch() + user_input
    header = createHeader()
    response = requests.get(url=url, headers=header)
    response.encoding = 'utf-8'
    return response

def googleSearch():
    pass

def main():
    response = getYandexSearch()
    soap = BeautifulSoup(response.text, 'lxml')
    arr = soap.find('u1', class_='serp-list serp-list_left_yes')
    print(arr)


if __name__ == '__main__':
    main()