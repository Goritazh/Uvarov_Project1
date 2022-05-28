# модуль работы с полем игры

import players
import help

FIELD = [[''] * 3 for _ in range(3)]
MARKERS = ('X', 'O')


# отображение поля игры
def show_field():
    global FIELD
    res = ""
    for i in FIELD:
        res += str(i) + "\n"
    print(res)


# проверка наличия сохранённой партии
def check_saves(*, single=True):
    global FIELD
    # для парной игры
    s = set(players.PLAYER)
    # для одиночной игры
    if single:
        s |= {'ai1', 'ai2'}
    for save in players.SAVES:
        if set(save).issubset(s):
            # хочет ли игрок загрузить найденную партию
            load = input(help.MESSAGES[6]).lower()
            if load in help.ANSWERS[6]:
                FIELD = players.SAVES[save]
                return save
    return False


# функция проверки на победу или ничью
def check_win_or_tie():
    pass


def game():
    pass
