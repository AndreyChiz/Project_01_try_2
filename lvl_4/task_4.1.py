# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)
import sqlite3

PUTH = 'teatchers.db'
student_list = [(201, 'Иван', 1),
                (202, 'Петр', 2),
                (203, 'Анастасия', 3),
                (204, 'Игорь', 4),
                ]

try:
    connection_ = sqlite3.connect(PUTH)
    cursor_ = connection_.cursor()
    cursor_.execute(
        '''CREATE TABLE IF NOT EXISTS Students (
        Student_Id INTEGER,
        Student_Name TEXT,
        School_Id INTEGER PRIMARY KEY
        )'''
    )

    # Наполните таблицу следующими данными:

    # 201, Иван, 1
    # 202, Петр, 2
    # 203, Анастасия, 3
    # 204, Игорь, 4
    for item in student_list:
        cursor_.execute('INSERT INTO  Students  (Student_Id, Student_Name, School_Id) VALUES (?, ?, ?)',
                        (item[0], item[1], item[2]))

        connection_.commit()

except sqlite3.Error as e:
    connection_.rollback()
    print("Ошибка: таблица с таким названием существует")
finally:
    connection_.close()


# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:


def student_info(student_id: int, path) -> tuple:
    '''
    Возвращает кортеж с данными студента с указанным ID
    :param student_id: ID студента
    :return: (<ID Студента>,<Имя студента>,<ID школы>,<Название школы>)
    '''

    try:
        connection_ = sqlite3.connect(PUTH)
        cursor_ = connection_.cursor()
        query = '''
            SELECT Students.Student_Id, Students.Student_Name, School.School_Id, School.School_Name
            FROM Students
            INNER JOIN School ON Students.school_id = School.school_id
            WHERE Students.Student_Id = ?;
            '''
        cursor_.execute(query, (student_id,))
        data = cursor_.fetchone()
        if data:
            return data
        else:
            return ('Отсутствует',) * 4
    except sqlite3.Error as e:
        print("Ошибка выполнения запроса:", e)
    finally:
        connection_.close()


if __name__ == '__main__':
    student_data = student_info(int(input("Введите ID студента: ")), PUTH)
    print("ID студента: {}\nИмя студента: {}\nID школы: {}\nНазвание школы: {}"
          .format(*student_data))
