# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.
import random


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
    '''
    Класс матрица
    '''
    def __init__(self, *, rows: int = 3, colomns: int = 3, value: int | None = None):
        '''
        Создает двумерный список размерностью rows-строк на colomns-столбцов, заполняет занчениями value
        :param rows: количество строк
        :param colomns: количество столбцов
        :param value: значение ячеек
        '''
        self.rows = rows
        self.colomns = colomns
        self.value = value
        self.data = [[value] * self.colomns for i in range(self.rows)]

    def __str__(self) -> str:
        result = ''
        for row in self.data:
            result += ' '.join([str(elem) for elem in row]) + '\n'
        return result

    def change_all_values(self, new_value: int):
        '''
        Изменяет все значения матрицы на new_value
        :param new_value:
        :return:
        '''
        self.data = [[new_value] * self.colomns for i in range(self.rows)]


    def change_element(self, *, colomn: int, row: int, value: int) -> None:
        '''
        Заменяет элемент на указанной позиции, позиция[0][0] - лево, верх
        :param colomn: номер столбца
        :param row: номер ряда
        :param value: значение
        :return:
        '''
        self.data[row][colomn] = value

    def get_measure(self) -> tuple:
        '''
        Возвращает размерность матрицы
        :return:
        '''
        return self.rows, self.colomns

    def rundomize_values(self,):
        self.data = [[random.randint(0,9) for _ in range(self.colomns)] for i in range(self.rows)]


if __name__ == '__main__':

    #   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
    #   - в каждой ячейке содержится либо число, либо None
    matrix = Matrix(rows=4, colomns=8, value=1)
    print(matrix)

    # выводить число строк и колонок
    measure = matrix.get_measure()
    print(f'Размер матрицы:\nкол-во строк - {measure[0]}\nкол-во колонок - {measure[1]}\n')

    # заменять существующие значения
    matrix.change_element(row=1, colomn=3, value=5)
    print(matrix)

    # принимать новые значения,
    matrix.change_all_values(8)
    print(matrix)

    matrix.rundomize_values()
    print(matrix)