# импорты
from players import *
from help import COMMANDS, MESSAGES, show_help, show_message


# вывод названия игры/приветствия
show_message('Крестики-нолики')

# чтение .ini файла
if read_ini():
    show_help()

# запуск суперцикла
while True:
    # запрос начала новой партии
    command = input(MESSAGES[0].lower())

    # выход из программы
    if command in COMMANDS['quit']:
        # обработка завершения работы приложения
        break
    # показать справку
    elif command in COMMANDS['help']:
        show_help()
    # показать таблицу результатов
    elif command in COMMANDS['scores']:
        pass
    # начало новой партии
    elif command in COMMANDS['new']:
        # есть ли текущий игрок
        if not PLAYER:
            # запрос имени игрока
            player_name()
        # запрос режима игры
        if game_mode():
            # продолжаем сохранённую партию
            pass
        else:
            # начинаем новую партию
            pass
