#

FIELD = [[''] * 3 for _ in range(3)]


def field():
    global FIELD
    res = ""
    for i in FIELD:
        res += str(i) + "\n"
    print(res)

