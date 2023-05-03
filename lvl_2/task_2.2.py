# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.
import math

months = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь', 7: 'июль', 8: 'август',
          9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'
          }
quarter_name = {1: 'первого', 2: 'второго', 3: 'третьего', 4: 'четвёртого'}

def quarter_month(month_number: int)-> str:
    """
    Возвращает номер квартал по номеру месяца

    :param month_number: номер месяца
    :return: str
    """
    return (f'месяц {month_number} ({months[month_number]})'
          f' является частью {quarter_name[math.ceil(month_number / 3)]} квартала.'
          )


print(quarter_month(int(input('Введите номер месяца: '))))


# class Task:
#     months = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь', 7: 'июль', 8: 'август',
#               9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'
#               }
#     quarter_name = {1: 'первого', 2: 'второго', 3: 'третьего', 4: 'четвертого'}
#     month_number: int
#
#     def __call__(self):
#         try:
#             self._solution()
#         except KeyError:
#             print('Такого месяца нет!')
#         except ValueError:
#             print('Неверный формат номера месяца')
#
#     def _solution(self):
#         self.month_number: int = int(input('Введите номер месяца: '))
#         print(f'месяц {self.month_number} ({self.months[self.month_number]})'
#               f' является частью {self._month_quarter()} квартала.'
#               )
#
#     def _month_quarter(self):
#         quarter_number = math.ceil(self.month_number / 3)
#         return self.quarter_name[quarter_number]
#
#
# if __name__ == '__main__':
#     task = Task()
#     task()
