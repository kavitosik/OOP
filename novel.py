import json
from loguru import logger


class Novel:
    def __init__(self, title):
        self.title = title
        self.chapters = {}

    def write_novel_to_bd(self, chapters):
        self.chapters = chapters
        with open(f"{self.title}.json", 'w', encoding='UTF-8') as json_file:
            json.dump(self.chapters, json_file,
                      ensure_ascii=False)
        logger.info(f"Главы новеллы записаны в файл {self.title}.json")
