class Car:
    def __init__(self, model, year, author, color, volume, price):
        self.model = model
        self.year = year
        self.autor = author
        self.color = color
        self.volume = volume
        self.price = price
        self.cars = {}

    def give_data(self):
        model = input('Введите модель машины для получения информации о ней: ')
        if model in self.cars:
            print("\nВот данные по вашей моделе:")
            print(*self.cars[model])
        else:
            print("К сожалению такая модель машины не найдена.")


def take_data():
    model = input("Введите модель машины: ")
    year = input("Введите год выпуска машины: ")
    author = input("Введите производителя машины: ")
    color = input("Введите цвет машины: ")
    volum = input("Введите объём двигателя: ")
    price = input("Введите цену машины: ")

    car = Car(model, year, author, color, volum, price)
    car.cars[model] = [f'Год создания: {year}\n',
                       f'Производитель: {author}\n',
                       f'Цвет машины: {color}\n',
                       f'Объём двигателя: {volum}\n',
                       f'Цена: {price}\n']

    car.give_data()


take_data()
