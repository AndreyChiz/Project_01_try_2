# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"
def remove_exclamation_marks(s: str) -> str:
    """
    Удалить все символы '!' из строки
    :param s: строка
    :return:
    """
    return s.replace('!', '')


print(remove_exclamation_marks('!hallo! !world!'))


# Пункт B.
# Удалите восклицательный знак из конца строки.
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    """
       Удалить все символы '!' c конца строки
       :param s:
       :return:
       """
    return s.rstrip('!')
print(remove_last_em('!hallo!!!!'))

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    return [i for i in s.split() if i.count('!') != 1]

print(*remove_word_with_one_em("Hi! !Hi! Hi!"))