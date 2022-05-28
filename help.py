from shutil import get_terminal_size as gts
from math import floor, ceil

COMMANDS = {'quit': ('quit', 'выход'),
            'help': ('help', 'помощь', 'h', '?'),
            'scores': ('scores', 'таблица'),
            'new': ('new', 'новая', 'yes', 'да', 'y', 'д'),
            '': (),
            }

MESSAGES = ('хотите начать новую партию? > ',
            'введите имя игрока > ',
            'введите имя второго игрока > ',
            'выберите режим игры:\n  1 - с ботом\n  2 - с человеком\n> ',
            'выберите уровень сложности:\n  1 - лёгкий\n  2 - трудный\n> ',
            'вы хотите ходить первым? > ',
            'вы хотите загрузить сохранённую партию? > ',
            )

ANSWERS = (None,
           None,
           None,
           ('1', 'бот', 'б', '2', 'человек', 'ч'),
           ('1', 'лёгкий', 'л', '2', 'трудный', 'т'),
           ('yes', 'да', 'y', 'д'),
           ('yes', 'да', 'y', 'д'),
           )

h = f'''Правила игры:

Список команд:
{' '.join(COMMANDS['quit'])}
{' '.join(COMMANDS['help'])}
{' '.join(COMMANDS['scores'])}
{' '.join(COMMANDS['new'])}
'''


# вывод правил игры и списка команд
def show_help():
    print(h)


# вывод сообщения в рамке
def show_message(text):
    width = gts()[0] - 1
    h_width = (width - len(text) - 2) / 2
    m = f"""{'#' * width}
{'#' + ' ' * (width - 2) + '#'}
{'#' + ' ' * ceil(h_width) + text.upper() + ' ' * floor(h_width) + '#'}
{'#' + ' ' * (width - 2) + '#'}
{'#' * width}"""
    print(m, end='\n\n')
