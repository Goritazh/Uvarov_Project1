# импорты
from players import *
from help import show_help, show_message


show_message('Крестики-нолики')
# чтение .ini файла
# if read_ini():
#     show_help()

# запуск суперцикла
while True:
    command = input('> ')

    if command in ('quit', 'выход'):
        # обработка завершения работы приложения
        break
    elif command in ('new', 'yes'):
        if not PLAYER:
            player_name()

        # начало новой партии

