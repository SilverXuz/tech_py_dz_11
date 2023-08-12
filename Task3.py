"""
📌 Дорабатываем класс прямоугольник из прошлого семинара.
📌 Добавьте возможность сложения и вычитания.
📌 При этом должен создаваться новый экземпляр
прямоугольника.
📌 Складываем и вычитаем периметры, а не длинну и ширину.
📌 При вычитании не допускайте отрицательных значений.
"""

"""
Задание №6
Доработайте прошлую задачу.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения
"""

"""
Добавьте ко всем задачам с семинара строки документации и методы вывода 
информации на печать.
"""

class Rectangle:
    """Класс для представления прямоугольника."""

    def __init__(self, height: int, width=None):
        """Инициализация экземпляра прямоугольника."""
        self.height = height
        if width:
            self.width = width
        else:
            self.width = height

    def get_perimeter(self):
        """Вычисление периметра прямоугольника."""
        return 2 * (self.height + self.width)

    def get_area(self):
        """Вычисление площади прямоугольника."""
        return self.width * self.height

    def __add__(self, other):
        """Сложение прямоугольников по периметру."""
        perimetr = self.get_perimeter() + other.get_perimeter()
        side_a = perimetr // 6
        side_b = (perimetr - side_a * 2) // 2
        return Rectangle(side_a, side_b)

    def __sub__(self, other):
        """Вычитание прямоугольников по периметру."""
        perimetr = abs(self.get_perimeter() - other.get_perimeter())
        side_a = perimetr // 6
        side_b = (perimetr - side_a * 2) // 2
        return Rectangle(side_a, side_b)

    def __eq__(self, other):
        """Сравнение прямоугольников на равенство площади."""
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        """Сравнение прямоугольников на неравенство площади."""
        return self.get_area() != other.get_area()

    def __lt__(self, other):
        """Сравнение прямоугольников по площади (меньше)."""
        return self.get_area() < other.get_area()

    def __le__(self, other):
        """Сравнение прямоугольников по площади (меньше или равно)."""
        return self.get_area() <= other.get_area()

    def __gt__(self, other):
        """Сравнение прямоугольников по площади (больше)."""
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        """Сравнение прямоугольников по площади (больше или равно)."""
        return self.get_area() >= other.get_area()

    def __str__(self):
        """Строковое представление прямоугольника."""
        return f'Rectangle(height={self.height}, width={self.width})'

    def __repr__(self):
        """Представление прямоугольника в виде строки."""
        return self.__str__()

spam = Rectangle(1, 9)
eggs = Rectangle(7)

add_reg = spam + eggs
sub_reg = spam - eggs

print(f'{sub_reg.width = }, {sub_reg.height =}')
print(f'{add_reg.width = }, {add_reg.height =}')
print()
print(spam)
print(eggs)
print()
print(repr(spam))
print(repr(eggs))
