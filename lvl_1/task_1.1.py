# Задача 1.1.
import array

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'


# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

def print_paly_list(songs_titles: str, *args: int) -> None:
    '''
    Вывести список песен из строки song_titles в порядке указанном в *args

    :param songs_titles:  строка со списком песен
    :param args: очередь номеров песен, номера соответствуют очередности песен
    в song_titles от 1 до len(songs_titles)
    '''
    wrap_song_dict = {k: v for k, v in enumerate(songs_titles.split(', '), 1)}
    for song in (wrap_song_dict[i] for i in args):
        print(song)


if __name__ == '__main__':
    print_paly_list(my_favorite_songs, 1, 5, 2, 4)
