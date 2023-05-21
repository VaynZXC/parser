import requests
import lxml.html
import bs4
from bs4 import BeautifulSoup


def main():
    base = 'https://stackoverflow.com/questions'
    html = requests.get(base).content
    soup = BeautifulSoup(html, 'lxml')
    div = soup.find('div', id='questions')
    a = div.find_all('a', class_='s-link')

    n = 1

    for _ in a:
        print(str(n) + ' вопрос: ' + base + _.get('href'))
        n += 1


if __name__ == "__main__":
    main()
