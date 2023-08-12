"""
Создайте класс Матрица. Добавьте методы для:
○ вывода на печать,
○ сравнения,
○ сложения,
○ *умножения матриц
"""

# Данное решение было решено при помощи интернета.

class Matrix:
    def __init__(self, rows):
        self.rows = rows

    def __str__(self):
        matrix_str = ""
        for row in self.rows:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str

    def __eq__(self, other):
        return self.rows == other.rows

    def __add__(self, other):
        if len(self.rows) != len(other.rows) or len(self.rows[0]) != len(other.rows[0]):
            raise ValueError("Размерности матриц должны быть одинаковыми для сложения.")

        result_rows = []
        for i in range(len(self.rows)):
            result_row = [a + b for a, b in zip(self.rows[i], other.rows[i])]
            result_rows.append(result_row)

        return Matrix(result_rows)

    def __mul__(self, other):
        if len(self.rows[0]) != len(other.rows):
            raise ValueError(
                "Количество столбцов в первой матрице должно совпадать с количеством строк во второй матрице.")

        result_rows = []
        for i in range(len(self.rows)):
            result_row = []
            for j in range(len(other.rows[0])):
                element_sum = 0
                for k in range(len(self.rows[0])):
                    element_sum += self.rows[i][k] * other.rows[k][j]
                result_row.append(element_sum)
            result_rows.append(result_row)

        return Matrix(result_rows)


# Пример использования
matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print("Матрица 1:")
print(matrix1)

print("Матрица 2:")
print(matrix2)

# Сложение матриц
matrix_sum = matrix1 + matrix2
print("Сумма матриц:")
print(matrix_sum)

# Умножение матриц
matrix_mult = matrix1 * matrix2
print("Умножение матриц:")
print(matrix_mult)
