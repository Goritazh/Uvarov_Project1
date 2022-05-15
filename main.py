# импорты



# глобальные переменные
FIELD = [['']*3 for _ in range(3)]
markers = ""

# функции
def field():
    global FIELD
    res = ""
    for i in FIELD:
        res += str(i) + "\n"
    print(res)

# чтение .ini файла


# запуск суперцикла
# while True:
#     command = input()
#
#     if command in ('quit', 'выход'):
#         # обработка завершения работы приложения
#         break
#
#     # ввод имени игрока


field()