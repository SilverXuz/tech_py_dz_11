"""
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания (time.time)
"""

"""
Добавьте ко всем задачам с семинара строки документации и методы вывода 
информ
"""

import datetime

class MyString(str):

    def __new__(cls, current_str, author):
        instance = super().__new__(cls, current_str)
        instance.author = author
        instance.creation_time = datetime.datetime.today()
        return instance

    def __str__(self):
        return f'String: "{super().__str__()}", Author: {self.author}, Created at: {self.creation_time}'

    def get_author(self):
        return self.author

    def get_creation_time(self):
        return self.creation_time

# Создаем объект MyString
spam = MyString('чудный день', 'сурок')

# Вывод информации о строке
print(spam)

# Вывод автора и времени создания
print(f'Author: {spam.get_author()}, Creation Time: {spam.get_creation_time()}')
