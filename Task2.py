"""
Создайте класс Архив, который хранит пару свойств. Например, число и строку.
При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются
в пару списков-архивов, которые также являются свойствами экземпляра.
"""

"""
Добавьте ко всем задачам с семинара строки документации и методы вывода 
информации на печать.
"""

class Arhiv:
    """Класс Архив для хранения данных"""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.list_arhiv = []

        cls._instance.list_arhiv.append(args)

        return cls._instance

    def __init__(self, text: str, number: int):
        """Инициализация объекта Arhiv"""
        self.text = text
        self.number = number

    def __str__(self):
        return f'Текущий текст строки: {self.text}, Число строки: {self.number}'

    def __repr__(self):
        return f'Arhiv(text={self.text!r}, number={self.number!r})'

    def user_representation(self):
        return f'Текущее содержимое: {self.text}'

    def programmer_representation(self):
        return f'Объект Arhiv(text={self.text!r}, number={self.number!r})'

# Создаем экземпляры класса
archive1 = Arhiv("Hello", 42)
archive2 = Arhiv("World", 77)

# Используем методы представления для пользователя и программиста
print(archive1.user_representation())  # Выводит: Текущее содержимое: Hello
print(repr(archive2))  # Выводит: Arhiv(text='World', number=77)

# Документация класса и методов
print(Arhiv.__doc__)  # Выводит: Класс Архив для хранения данных
print(Arhiv.__init__.__doc__)  # Выводит: Инициализация объекта Arhiv
