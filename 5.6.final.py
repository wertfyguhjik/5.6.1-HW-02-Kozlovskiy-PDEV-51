# игра крестики-нолики
# автор - Козловский Юрий, PDEV-51
# идею немного подсмотрел в записи вебинара по разбору задачи.

print("///////////////////////////////////")
print("")
print("Приветствую в игре крестики-нолики!")
print("Представьтесь, пожалуйста.")
print("")
username1 = input("первый игрок: ")
username2 = input("второй игрок: ")
print("")
print(f"Отлично! {username1} - ты играешь за X, {username2} - ты играешь за O")
print("")
print("Правила:")
print("Имеется поле 3х3, игроки по очереди ставят свой знак в свободную клетку.")
print("Для этого надо ввести в консоли её координаты, от 1 до 3 по каждой оси, без пробелов.")
print("Сначала идёт строка, потом столбец. Например, первая ячейка - это 11, вторая - 12 и тд.")
print("Побеждает тот, кто полностью заполнит строку, столбец или диагональ.")
print("")
print("Приятной игры!")
print("")

# создаём начальную матрицу

rows = 4
cols = 4

matrix = [[" ", 1, 2, 3],
          [1, "-", "-", "-"],
          [2, "-", "-", "-"],
          [3, "-", "-", "-"]]

# задаём условия выигрыша для X - строка, столбец или диагональ
def win_condition_X():
    if (
        (matrix[1][1] == "X" and matrix[1][2] == "X" and matrix[1][3] == "X") or
        (matrix[2][1] == "X" and matrix[2][2] == "X" and matrix[2][3] == "X") or
        (matrix[3][1] == "X" and matrix[3][2] == "X" and matrix[3][3] == "X") or
        (matrix[1][1] == "X" and matrix[2][1] == "X" and matrix[3][1] == "X") or
        (matrix[1][2] == "X" and matrix[2][2] == "X" and matrix[2][3] == "X") or
        (matrix[1][3] == "X" and matrix[2][3] == "X" and matrix[3][3] == "X") or
        (matrix[1][1] == "X" and matrix[2][2] == "X" and matrix[3][3] == "X") or
        (matrix[3][1] == "X" and matrix[2][2] == "X" and matrix[1][3] == "X")
            ):
            print("")
            print(f"Выиграл крестик! Победа за {username1}!")
            return True
    return False

# и такие же условия для O
# (наверно, есть более лаконичный способ это сделать...)
def win_condition_O():
    if (
        (matrix[1][1] == "O" and matrix[1][2] == "O" and matrix[1][3] == "O") or
        (matrix[2][1] == "O" and matrix[2][2] == "O" and matrix[2][3] == "O") or
        (matrix[3][1] == "O" and matrix[3][2] == "O" and matrix[3][3] == "O") or
        (matrix[1][1] == "O" and matrix[2][1] == "O" and matrix[3][1] == "O") or
        (matrix[1][2] == "O" and matrix[2][2] == "O" and matrix[2][3] == "O") or
        (matrix[1][3] == "O" and matrix[2][3] == "O" and matrix[3][3] == "O") or
        (matrix[1][1] == "O" and matrix[2][2] == "O" and matrix[3][3] == "O") or
        (matrix[3][1] == "O" and matrix[2][2] == "O" and matrix[1][3] == "O")
            ):
            print("")
            print(f"Выиграл нолик! Победа за {username2}!")
            return True
    return False

# создаём алогритм самой игры
def game():

    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end=" ")
        print()                                                             # выводим на консоль поле в подобающем формате

    while True:
        while True:
            print("")
            coordX = list(input(f"{username1}, введите координаты X: "))    # запрашиваем у пользователя координаты X
            print("")

            a, b = int(coordX[0]), int(coordX[1])                           # преверащаем ввод в переменные

            if matrix[a][b] == "-":                                         # проверям, что клетка пустая
                matrix[a][b] = "X"                                          # Вносим X в матрицу по введённым координатам
                break
            else:
                print("Неправильная клетка! Повторите ввод.")               # если клетка занята, повторяем ввод координат

        for i in range(rows):                                               # выводим поле с новым X
            for j in range(cols):
                print(matrix[i][j], end=" ")
            print()

        if win_condition_X():                                               # проверяем, выиграл ли X
            break

        matrix_merged = [i for j in matrix for i in j]                      # создаём из матрицы список для проверки на ничью
        if "-" not in matrix_merged:                                        # после хода X, т.к. он ходит последний
            print("")                                                       # если все клетки заняты (нет "-"), выводим сообщение
            print("Ничья!")                                                 # способ подсмотрел в интернете
            break

        while True:
            print("")
            coordO = list(input(f"{username2},введите координаты O: "))     # запрашиваем у пользователя координаты O
            print("")

            c, d = int(coordO[0]), int(coordO[1])                           # преверащаем ввод в переменные

            if matrix[c][d] == "-":                                         # проверям, что клетка пустая
                matrix[c][d] = "O"                                          # Вносим O в матрицу по введённым координатам
                break
            else:
                print("Неправильная клетка! Повторите ввод.")               # если клетка занята, повторяем ввод координат

        for i in range(rows):                                               # выводим поле с новым O
            for j in range(cols):
                print(matrix[i][j], end=" ")
            print()

        if win_condition_O():                                               # проверяем, выиграл ли O
            break

# запускаем игру
game()

# Под конец перестала работать последняя проверка выигрыша! Потратил N часов чтобы понять, почему, но без успеха.
# Если оставить одно любое условие, оно выполняется, но второе всегда игнорируется.
# Пробовал объединить условия в одной функции, но результат был тот же.
# Потом проверка магическим образом снова стала работать. Не понимаю. Программирование это весело.


