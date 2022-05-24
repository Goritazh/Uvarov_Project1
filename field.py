#

FIELD = [[''] * 3 for _ in range(3)]


# опишите функцию: что она делает?
def field():
    global FIELD
    res = ""
    for i in FIELD:
        res += str(i) + "\n"
    print(res)
    # хорошо, что начали, но пока это не очень похоже на поле для крестиков-ноликов
