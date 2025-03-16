import requests
from loguru import logger
from bs4 import BeautifulSoup
from novel import Novel


class Parser:
    def __init__(self, title, url):
        self.title = title
        self.url = url
        self.chapters = {}
        self.chapter = 1

    def get_novel(self):
        page = self.get_webpage(self.url)
        chapters_list = page.find('ul', class_='list clearfix')
        elements = chapters_list.find_all('a')
        links = []
        for element in elements:
            href = element.get('href')
            if href:
                links.append(href)

        logger.info(f"Все ссылки на главы новеллы {self.title} собранны")

        for link in links:
            chapter_page = self.get_webpage(link)
            text = chapter_page.find('div', class_='book_con fix')
            self.chapters.update({str(self.chapter): link + text.text})

        logger.info(f"Все тексты новеллы {self.title} собранны")

        novel = Novel(self.title)
        novel.write_novel_to_bd(self.chapters)

    def get_webpage(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            logger.info(f"Страница по адресу {url} доступна")
            return BeautifulSoup(response.text, 'html.parser')
        else:
            logger.error(f"Сервер вернул {response.status_code} статус")
