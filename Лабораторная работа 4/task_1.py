class Gadget:
    """ Базовый класс гаджета.
        Определяет общие атрибуты и методы для всех гаджетов."""

    def __init__(self, name: str, model: str, body_material: str):
        """
        Инициализация базового класса для гаджета.
        :param name: Название типа устройства
        :param model: Модель устройства
        :param body_material: Материал корпуса
        """
        self._name = name
        self._model = model
        self._body_material = body_material


    def __str__(self) -> str:
        return f"Название {self.name}. Модель {self.model}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, model={self.model!r}, body_material={self.body_material!r})"

    @property
    def name(self) -> str:
        """Геттер для названия устройства с маскировкой для безопасности"""
        return self._name

    @property
    def model(self) -> str:
        """Геттер для модели устройства с маскировкой для безопасности"""
        return self._model

    @property
    def body_material(self):
        """Геттер для материала корпуса"""
        return self._body_material

    def material(self) -> str:
        return self._body_material

    def update_model(self, new_model: str) -> None:
        """
        Обновление модели устройства
        :param new_model: Новая модель
        """
        ...



class Smartphone(Gadget):
    def __init__(self, name: str, model: str, body_material: str, screen_diagonal: float, memory_capacity: float):
        """
        Дочерний класс гаджетов для смарфона

        :param screen_diagonal: Диагональ экрана
        :param memory_capacity: Объем памяти
        """
        super().__init__(name, model, body_material)
        self.screen_diagonal = screen_diagonal
        self.memory_capacity = memory_capacity

    @property
    def screen_diagonal(self) -> float:
        """Геттер для диагонали экрана"""
        return self._screen_diagonal

    @screen_diagonal.setter
    def screen_diagonal(self, new_screen_diagonal) -> None:
        """
        Сеттер для диагонали экрана
        :param new_screen_diagonal: Новая диагональ экрана
        :raise ValueError: Если диагональ экрана меньше нуля
        :raise TypeError: Если диагональ экрана неправильного типа

        """
        if not isinstance(new_screen_diagonal, (float, int)):
            raise TypeError("Диагональ экрана должна быть типа float или int")
        if new_screen_diagonal < 0:
            raise ValueError("Диагональ экрана должна быть больше нуля")
        self._screen_diagonal = new_screen_diagonal

    @property
    def memory_capacity(self):
        """Геттер для объема памяти"""
        return self._memory_capacity

    @memory_capacity.setter
    def memory_capacity(self, new_memory_capacity):
        """
        Сеттер для объема памяти
        :param new_memory_capacity: Новый объем памяти
        :raise ValueError: Если объем памяти меньше нуля
        :raise TypeError: Если объем памяти неправильного типа

                """
        if not isinstance(new_memory_capacity, (int, float)):
            raise TypeError("Объем памяти должн быть типа float или int")
        if new_memory_capacity < 0:
            raise ValueError("Объем памяти должн быть больше нуля")
        self._memory_capacity = new_memory_capacity

    def download_app(self, application_size: float) -> None:
        """
        Установка приложения на смартфон
        :param application_size: Размер приложения
        :raise ValueError: Если размер приложения меньше нуля или на устройстве недостаточно памяти
        :raise TypeError: Если объем памяти неправильного типа
        """
        if not isinstance(application_size, (int, float)):
            raise TypeError("Объем приложения должн быть типа float или int")
        if application_size < 0:
            raise ValueError("Объем приложения должн быть больше нуля")
        if application_size >  self.memory_capacity:
            raise ValueError("Не хватает памяти")
        self.memory_capacity -= application_size

    def update_model(self, new_model: str) -> None:
        """
        Перегруженный метод обновление модели смартфона

        Причина перегрузки: Способ обновления модели смартфона отличается от других гаджетов
        :param new_model: Новая модель
        """
        ...

    def __repr__(self) -> str:
        """
        Перегруженный магический метод для технического представления смартфона
        """
        return f"{self.__class__.__name__}(name={self.name!r}, model={self.model!r}, body_material={self.body_material!r}, screen_diagonal={self.screen_diagonal!r}, memory_capacity={self.memory_capacity!r})"


class Watch(Gadget):
    def __init__(self, name: str, model: str, body_material: str, date_and_time: str):
        """
        Дочерний класс гаджетов для часов

        :param date_and_time: Дата и время
        """
        super().__init__(name, model, body_material)
        if not isinstance(date_and_time, str):
            raise TypeError("Дата должна быть типа str")
        self.date_and_time = date_and_time

    def change_date_and_time(self, new_date_and_time: str) -> None:
        """
        Изменение даты и времени на устройстве
        :param new_date_and_time: Новая дата и время
        :raise TypeError: Если новая дата и время неправильного типа
        """
        if not isinstance(new_date_and_time, str):
            raise TypeError("Дата должна быть типа str")
        self.date_and_time = new_date_and_time

    def update_model(self, new_model: str) -> None:
        """
        Перегруженый метод обновление модели часов

        Причина перегрузки: Способ обновления модели часов отличается от других гаджетов
        :param new_model: Новая модель
        """
        ...

    def __repr__(self) -> str:
        """
        Перегруженный магический метод для технического представления часов
        """
        return f"{self.__class__.__name__}(name={self.name!r}, model={self.model!r}, body_material={self.body_material!r}, date_and_time={self.date_and_time!r})"


if __name__ == "__main__":
    # Write your solution here

    # Создаем экземпляры классов
    iphone = Smartphone("Iphone", "16 Pro", "Titanium alloy", 6.3, 128)
    watch = Watch("Xiaomi Redmi Watch", "5 Lite", "Plastic (NCVM)", "01.01.1960")

    # Тестируем методы
    iphone.download_app(3.5)
    # iphone.download_app(130) -> ValueError: Не хватает памяти
    watch.change_date_and_time("16.03.2026")

    iphone.update_model("17 Pro")
    watch.update_model("5.2.144")
    pass