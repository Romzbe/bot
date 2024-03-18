
def start():
    print("---------------------------------------")
    print("  Приветствуем вас ")
    print("  в игре крестики нолики")
    print("---------------------------------------")
    print("  Запаситесь чаем и печеньками")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")

start()


def show():
    print()
    print(" |  | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(game):
        roh = f" | {i} | {' | '.join(row)} | "
        print(roh)
        print("  --------------- ")
    print()


def ask():
    while True:
        cords = input("     Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if game[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(game[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False


game = [[" "] * 3 for i in range(3) ]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = ask()

    if count % 2 == 1:
        game[x][y] = "X"
    else:
        game[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Ничья!")
        break


