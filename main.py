# импорты
from players import *
from help import show_help, show_message


show_message('Крестики-нолики')

# чтение .ini файла
if read_ini():
    show_help()

# запуск суперцикла
while True:
    # смотрите в файл с архитектурой
    # что происходит, когда мы только заходим в суперцикл?
    command = input('> ')

    if command in ('quit', 'выход'):
        # обработка завершения работы приложения
        break
    elif command in ('new', 'yes'):
        if not PLAYER:
            player_name()
            # мы узнали имя игрока: что делаем дальше?


            # где-то тут должно быть начало новой партии
