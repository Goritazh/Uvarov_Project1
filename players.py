# Модуль заботы с данными игроков

from configparser import ConfigParser

import help
import field

SCORES = {}

PLAYER = tuple()

SAVES = {}


# читать из файла статистику игроков и их сохранения
def read_ini():
    global SCORES, SAVES
    config = ConfigParser()
    if config.read('data.ini', encoding='utf-8'):
        # статистика побед
        SCORES = {name.title(): [int(n) for n in score.split(',')]
                  for name, score in config['Scores'].items()}
        # сохранение партии превращаем в матрицу поля
        SAVES = {tuple(name.split(';')):
                     [[' ' if c == '-' else c for c in field[i:i + 3]]
                      for i in range(0, 9, 3)]
                 for name, field in config['Saves'].items()}
        # первый запуск программы
        return True if config['General']['first'] == 'yes' else False
    else:
        raise FileNotFoundError


# сохранить в файл статистику игроков и их сохранения
def save_ini():
    config = ConfigParser()
    # записываем статистику побед игроков
    config['Scores'] = {name: ','.join(str(n) for n in score)
                        for name, score in SCORES.items()}
    # из матрицы поля формируем строку для хранения в конфигурационном файле
    config['Saves'] = {';'.join(name):
                           ''.join(['-' if c == ' ' else c for r in field for c in r])
                       for name, field in SAVES.items()}
    # если сохраняем данные, значит следующий запуск будет уже не первым
    config['General']['first'] = 'no'
    with open('data.ini', 'w', encoding='utf-8') as config_file:
        config.write(config_file)


# запрос имени пользователя, добавить бота, изменить очередность хода
def player_name(bot='', *, change_order=False):
    global PLAYER
    # если имя игрока еще не вводилось
    if len(PLAYER) == 0:
        PLAYER = (input(help.MESSAGES[1]).lower())
    # ввод второго имени (человек или бот)
    elif len(PLAYER) == 1:
        # необходимо передать строку 'ai1' или 'ai2'
        if bot:
            # добавит бота с уровнем сложности
            PLAYER = (PLAYER[0], bot)
        else:
            # добавит имя второго игрока
            PLAYER = (PLAYER[0], input(help.MESSAGES[2]).lower())
    # для выбора символа поменять местами элементы кортежа
    # первый играет крестиком и ходит первым
    if change_order:
        PLAYER = (PLAYER[1], PLAYER[0])


# выбор режима игры
def game_mode():
    global PLAYER
    # запрашиваем у игрока режим игры
    while True:
        gm = input(help.MESSAGES[3]).lower()
        if gm in help.ANSWERS[3]:
            break
    # если одиночная
    if gm in help.ANSWERS[3][:3]:
        # есть ли сохранение для одиночной игры
        if save := field.check_saves():
            # восстановление уровня сложности и очерёдности хода из сохранённой партии
            PLAYER = save
            return True
        # запрашиваем у игрока уровень сложности
        while True:
            dl = input(help.MESSAGES[4]).lower()
            if dl in help.ANSWERS[4]:
                break
        # добавляем имя бота к PLAYER
        if dl in help.ANSWERS[4][:3]:
            dl = 'ai1'
        else:
            dl = 'ai2'
        player_name(dl)
    # если парная
    else:
        player_name()
        if save := field.check_saves(single=False):
            # восстановление уровня сложности и очерёдности хода из сохранённой партии
            PLAYER = save
            return True
    # выбор очерёдности хода
    if not (input(help.MESSAGES[5]).lower() in help.ANSWERS[5]):
        player_name(change_order=True)


# вывод таблицы результатов
def show_stats():
    pass
