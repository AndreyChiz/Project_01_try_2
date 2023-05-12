# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - проявите фантазию :)

class Matrix:
    def __init__(self, rows: int = 3, colomn: int = 3, value: int | None = None):
        self.rows = rows
        self.colomns = colomn
        self.value = value
        self.data = [[value] * self.colomns for i in range(rows)]

    def __str__(self):
        result = ''
        for row in self.data:
            result += ' '.join([str(elem) for elem in row]) + '\n'
        return result

    def add_element(self, *, x_coord: int, y_coord: int, value: int) -> None:

        self.data[self.rows - y_coord][self.colomns - (self.colomns - x_coord) - 1] = value

    def get_measure(self) -> tuple:
        '''
        Возвращает размерность матрицы
        :return:
        '''
        return self.rows, self.colomns


matrix = Matrix(4, 8, 1)
matrix.add_element(y_coord=1, x_coord=3, value=5)

print(matrix)
print(matrix.get_measure())
