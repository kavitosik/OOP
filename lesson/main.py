from loguru import logger
from parser import Parser


def main():
    # https://www.52shuku.vip/yanqing/am/h2QX.html
    logger.add('file.log',
               format='{time:YYYY-MM-DD at HH:mm:} | {level} | {message}',
               rotation='3 days',
               backtrace=True,
               diagnose=True)

    title = input("Введите название новелы:")
    url = input("Введите ссылку:")
    pars = Parser(title, url)
    pars.get_novel()


if __name__ == '__main__':
    main()
