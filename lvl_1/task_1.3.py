# Задача 1.3.
from dataclasses import dataclass
# Напишите скрипт, который принимает от пользователя номер месяца,
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
# Введите номер месяца: 3
# Вы ввели март. 31 дней

# Введите номер месяца: 2
# Вы ввели февраль. 28 дней

# Введите номер месяца: 15
# Такого месяца нет

from calendar import monthrange


@dataclass
class DayMonth:

    months = {
        1: 'январь',
        2: 'февраль',
        3: 'март',
        4: 'апрель',
        5: 'май',
        6: 'июнь',
        7: 'июль',
        8: 'август',
        9: 'сентябрь',
        10: 'октябрь',
        11: 'ноябрь',
        12: 'декабрь'
    }

    def days_per_months(self ) -> str:
        try:
            self.month: int = int(input('Введите номер месяца: '))
            result = (
                f"Вы ввели {self.months[self.month]}."
                f" {monthrange(2023, self.month)[1]} дней"
            )
            return result
        except KeyError:
            return 'Такого месяца нет!'
        except ValueError:
            return 'Неверный формат номера месяца'


if __name__ == '__main__':
    day_month = DayMonth()
    print(day_month.days_per_months())


