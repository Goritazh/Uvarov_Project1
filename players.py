#
from configparser import ConfigParser

PLAYERS = {}
PLAYER = tuple()
SAVES = {}


def read_ini():
    global PLAYERS, SAVES
    config = ConfigParser()
    if config.read('data.ini', encoding='utf-8'):
        PLAYERS = {name.title(): [int(n) for n in score.split(',')]
                   for name, score in config['Scores'].items()}
        SAVES = {tuple(name.split(';')):
                     [[' ' if c == '-' else c for c in field[i:i + 3]]
                      for i in range(0, 9, 3)]
                 for name, field in config['Saves'].items()}
        return True if config['General']['first'] == 'yes' else False
    else:
        raise FileNotFoundError


def save_ini():
    config = ConfigParser()
    config['Scores'] = {name: ','.join(str(n) for n in score)
                        for name, score in PLAYERS.items()}
    config['Saves'] = {';'.join(name):
                           ''.join(['-' if c == ' ' else c for r in field for c in r])
                       for name, field in SAVES.items()}
    config['General']['first'] = 'no'
    with open('data.ini', 'w', encoding='utf-8') as config_file:
        config.write(config_file)


def player_name(bot=''):
    global PLAYER
    if len(PLAYER) == 0:
        PLAYER = (input().lower())
    elif len(PLAYER) == 1:
        if bot:
            PLAYER = (PLAYER[0], bot)
        else:
            PLAYER = (PLAYER[0], input().lower())
    else:
        pass

