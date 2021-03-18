# __author__Соловьева Дарья Викторовна
# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |
#
# | 3 5 8 3 |
# | 8 3 7 1 |
class Matrix:
    def __init__(self, lst_listes):
        self.lst_listes = lst_listes

    def __str__(self):
        matrix = str()
        for matrix_item in self.lst_listes:
            matrix_item_str = str()
            for item in matrix_item:
                matrix_item_str += f" {item} "
            matrix += f"|{matrix_item_str}| \n"
        return matrix


matrix1 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
print(matrix1)

matrix2 = Matrix([[5, 6], [7, 8], [9, 0]])
print(matrix2)

matrix3 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
print(matrix3)
