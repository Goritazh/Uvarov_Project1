# модуль работы с полем игры

from shutil import get_terminal_size as gts
import players
import help

F_SIZE = 3
FIELD = [[''] * F_SIZE for _ in range(F_SIZE)]
MARKERS = ('X', 'O')


# вывод поля игры
def show_field(*, right=False, center=False):
    result = FIELD
    if center:
        result = [[f'{i},{j}' for j in range(F_SIZE)] for i in range(F_SIZE)]
    mx = max([len(cell) for row in result for cell in row])
    wd = mx * F_SIZE + F_SIZE * 3 - 1
    margin = ' ' * ((gts()[0] - 1 - wd) // 2) if center else ' ' * (
            gts()[0] - 1 - wd) if right else ' '
    rows = [
        margin + '|'.join([cell.center(mx + 2) for cell in row])
        for row in result
    ]
    print('\n' + ('\n' + margin + '—' * wd + '\n').join(rows) + '\n')


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
