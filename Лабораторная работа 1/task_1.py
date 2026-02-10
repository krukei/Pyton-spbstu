import doctest

# TODO Написать 3 класса с документацией и аннотацией типов

class Taxi:

    def __init__(self, place_of_arrival: str, place_of_departure: str):
        """
        Создание и подготовка к работе объекта "Такси"

        :param place_of_arrival: Место прибытия
        :param place_of_departure: Место отправления

        Примеры:
        >>> taxi = Taxi("Улица Пушкина, дом 6","Улица Чайковского, дом 23")  # инициализация экземпляра класса
        """
        if not isinstance(place_of_arrival, str):
            raise TypeError("Место прибытия должено быть типа str")
        self.place_of_arrival = place_of_arrival

        if not isinstance(place_of_departure, str):
            raise TypeError("Место прибытия должено быть типа str")
        self.place_of_departure = place_of_departure

    def change_the_place_of_arrival(self, new_place_of_arrival: str) -> None:
        """
        Изменение места прибытия.
        :param new_place_of_arrival: Новое место прибытия

        :raise: TypeError: Если новый адрес не строка, то вызываем ошибку
        :return: Адрес отправления и адрес прибытия

        Примеры:
        >>> taxi = Taxi("Улица Пушкина, дом 6","Улица Чайковского, дом 23")
        >>> taxi.change_the_place_of_arrival("Улица Пушкина, дом 13")
        """
        if not isinstance(new_place_of_arrival, (str)):
            raise TypeError("Новое место прибытия должено быть типа str")
        ...

    def change_the_place_of_departure(self, new_place_of_departure: str) -> None:
        """
        Изменение места отправления.
        :param new_place_of_departure: Новое место отправления

        :raise: TypeError: Если новый адрес не строка, то вызываем ошибку
        :return: Адрес отправления и адрес прибытия
        Примеры:
        >>> taxi = Taxi("Улица Пушкина, дом 6","Улица Чайковского, дом 23")
        >>> taxi.change_the_place_of_departure("Улица Чайковского, дом 13")
        """
        if not isinstance(new_place_of_departure, (str)):
            raise TypeError("Новое место отправления должено быть типа str")
        ...

class TheaterTicket:

    def __init__(self, time: str, row_number: int, place_number: int):
        """
        Создание и подготовка к работе объекта "Билет в театр"

        :param time: Время представления
        :param row_number: Номер ряда
        :param place_number: Номер места

        Примеры:
        >>> ticket = TheaterTicket("15:30", 4, 15)
        """
        if not isinstance(row_number, int):
            raise TypeError("Номер ряда должен быть типа int")
        self.row_number = row_number

        if not isinstance(place_number, int):
            raise TypeError("Номер места должен быть типа int")
        self.place_number = place_number

        self.time = time

    def change_place(self, new_row: int, new_place: int) -> None:
        """
        Изменение места
        :param new_row: Новый ряд
        :param new_place: Новое место

        :raise: TypeError: Если новое место не int, то вызываем ошибку
        :return: Время представления, номер места

        Примеры:
        >>> ticket = TheaterTicket("15:30", 4, 15)
        >>> ticket.change_place(5, 15)
        """

        if not isinstance(new_row, int):
            raise TypeError("Номер ряда должен быть типа int")
        if not isinstance(new_place, int):
            raise TypeError("Номер места должен быть типа int")
        self.row_number = new_row
        self.place_number = new_place

    def change_time(self, new_time: str) -> None:
        """
        Изменение времени
        :param new_time: Новое время

        :return: Время представления, номер места
        Примеры:
        >>> ticket = TheaterTicket("15:30", 4, 15)
        >>> ticket.change_time("17:30")
        """
        ...

    def personalized_ticket(self, name: str) -> None:
        """
        Создание именного билета
        :param name: Имя

        :return: Время представления, номер места, имя зрителя
        Примеры:
        >>> ticket = TheaterTicket("15:30", 4, 15)
        >>> ticket.personalized_ticket("Иван Петрович")
        """
        ...

class BankAccount:
    def __init__(self, name: str, number: int, balance: float = 0.0):
        """
        Создание и подготовка к работе объекта "Банковский счет"

        :param name: Имя владельца счета
        :param number: Номер счета
        :param balance: Баланс

        Примеры:
        >>> account = BankAccount("Иван Петрович", 2003569, 500.0)
        """
        if not isinstance(name, str):
            raise TypeError("Имя счета должно быть типа str")
        self.name = name

        if not isinstance(number, int):
            raise TypeError("Номер счета должен быть типа int")
        self.number = number

        if not isinstance(balance, (int, float)):
            raise TypeError("Баланс должен быть типа int или float")
        self.balance = balance

    def contribution(self, money: float) -> None:
        """
        Внесение денег на счет.

        :param money: Сумма для внесения
        :raise ValueError: Если сумма меньше нуля

        Примеры:
        >>> account = BankAccount("Иван Петрович", 2003569, 500.0)
        >>> account.contribution(4000)
        """
        if not isinstance(money, (int, float)):
            raise TypeError("Сумма должен быть типа int или float")
        if money < 0:
            raise ValueError("Баланс должен быть больше нуля")
        self.balance += money

    def withdrawing(self, money: float) -> None:
        """
        Снятие денег со счета.

        :param money: Сумма для снятия
        :raise ValueError: Если сумма меньше нуля

        Примеры:
        >>> account = BankAccount("Иван Петрович", 2003569, 500.0)
        >>> account.withdrawing(400)
                """
        if not isinstance(money, (int, float)):
            raise TypeError("Сумма должен быть типа int или float")
        if money < 0:
            raise ValueError("Баланс должен быть больше нуля")
        if money > self.balance:
            raise ValueError("На счете недостаточно средств")
        self.balance -= money

if __name__ == "__main__":
    doctest.testmod()       # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
