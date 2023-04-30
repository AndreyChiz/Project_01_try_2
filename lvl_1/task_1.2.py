# Задача 1.2.
import datetime
import random


# Пункт A.
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
from functools import reduce


def sum_time_from_list(songs_list: list[list[str, float]]) -> None:
    '''
    У трёх случайных элементов списка суммировать элементы под индексом [1]

    :param songs_list: список из элементов [<название_песни>, <продолжительность>]
    :return: None
    '''
    tmp = random.sample(songs_list, 3)
    result = sum(song[1] for song in tmp)
    print(f'Три песни звучат {round(result, 2)} минут')


sum_time_from_list(my_favorite_songs)

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}


def sum_time_from_dict(songs_dict: {str: float}, func) -> None:
    '''
    Если бы это был не учебный проект, то я бы так не сделал, (чёрт его знает потом эту функцию func где искать)
    У трёх случайных элементов словаря суммировать элементы под индексом [1]

    :param songs_dict:
    :param func:
    :return:
    '''
    tmp = [(k, v) for k, v in songs_dict.items()]
    func(tmp)


sum_time_from_dict(my_favorite_songs_dict, sum_time_from_list)

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

import json
import urllib.request

def format_duration(duration):
    '''
    формат времени песни в списке

    :param duration:
    :return:
    '''
    minutes = duration // 60
    seconds = duration % 60
    return float(f"{minutes}.{seconds:02}")

def get_song_list(url):
    with urllib.request.urlopen(url) as response:
        json_data = response.read().decode()
        data = json.loads(json_data)
        song_list = []
        for track in data['tracks']['data']:
            song_list.append([track['title'], format_duration(track['duration'])])
        return song_list


url = 'https://api.deezer.com/chart'
new_song_list = get_song_list(url)
random.shuffle(new_song_list)

my_favorite_songs+=new_song_list
sum_time_from_list(my_favorite_songs)




# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime

for song in my_favorite_songs:
    duration = song[1]
    minutes = int(duration)
    seconds = round((duration - minutes) * 60)
    time = (datetime.datetime.min + datetime.timedelta(minutes=minutes, seconds=seconds)).time()
    song[1] = time

