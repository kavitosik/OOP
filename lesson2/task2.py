class Book:
    def __init__(self, name, year, izdatel, genre, author, price):
        self.name = name
        self.year = year
        self.izdatel = izdatel
        self.genre = genre
        self.author = author
        self.price = price


def start():
    books_info = {}
    request = input('Что вы хотите сделать?(ввести данные/получить данные/'
                    'редактировать данные/остановить):\n')
    while request.lower() != 'остановить':
        if request == 'ввести данные':
            name = input('Введите название: ')
            year = input('Введите год издания: ')
            izdatel = input('Введите издателя: ')
            genre = input('Введите жанр: ')
            author = input('Введите автора: ')
            price = input('Введите цену: ')
            book = Book(name, year, izdatel, genre, author, price)
            books_info[name] = [f'Название: {name}\n',
                                f'Год: {year}\n',
                                f'Издатель: {izdatel}\n',
                                f'Жанр: {genre}\n',
                                f'Автор: {author}\n',
                                f'Цена: {price}\n',]
        if request == 'получить данные':
            name = input('Введите название искомой книги: ')
            print('Вот данные по вашей книге:\n')
            print(books_info[name])
