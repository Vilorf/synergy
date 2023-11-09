from random import random

# Функция рисует в консоли игровое поле
def draw_board(gameSquare):
    print(gameSquare[0] + "|" + gameSquare[1] + "|" + gameSquare[2])
    print("-+-+-")
    print(gameSquare[3] + "|" + gameSquare[4] + "|" + gameSquare[5])
    print("-+-+-")
    print(gameSquare[6] + "|" + gameSquare[7] + "|" + gameSquare[8])


# Функция запрашивает у пользователя ход
def get_player_move(user_choise, gameSquare):
    player_move = input("Сделайте свой ход, выберите клетку (от 1 до 9): ")

    if player_move.isdigit() and int(player_move) >= 1 and int(player_move) <=9:
        if gameSquare[int(player_move) - 1] != " ":
            print("Клетка уже занята значением, выберите другую")
            get_player_move(user_choise, gameSquare)
        else:
            gameSquare[int(player_move) - 1] = user_choise
    else:
        print("Неверное значение, сверьтесь с инструкцией и введите правильный номер клетки")
        get_player_move(user_choise, gameSquare)

# Функция генерирует случайное число (0-8)
def get_computer_move(user_choise, gameSquare):
    computer_move = round(random() * 8)
    
    if gameSquare[computer_move] == " ":
        if user_choise == "Х":
            gameSquare[computer_move] = "О"
        else:
            gameSquare[computer_move] = "Х"
    else:
        if " " in gameSquare:
            get_computer_move(user_choise, gameSquare)


# Проверка победителя
def check_win(users, gameSquare):
    for user in range(2):
        for i in range(3):
            if gameSquare[i] == gameSquare[i + 3] == gameSquare[i + 6] == users[user]:
                print(f"Победил игрок {users[user]}")
                return True
            elif gameSquare[i*3] == gameSquare[i*3 + 1] == gameSquare[i*3 + 2] == users[user]:
                print(f"Победил игрок {users[user]}")
                return True

        if gameSquare[0] == gameSquare[4] == gameSquare[8] == users[user]:
            print(f"Победил игрок {users[user]}")
            return True
        elif gameSquare[2] == gameSquare[4] == gameSquare[6] == users[user]:
            print(f"Победил игрок {users[user]}")
            return True

    if " " not in gameSquare:
        print("Ничья")
        return True

    return False

def main():
    gameSquare = [" "] * 9
    draw_board(gameSquare)

    users = ["Х", "О"]
    user_choise = input('Введите символ которым будете играть - Х или О (русские буквы): ')

    if user_choise in users:
        while not check_win(users, gameSquare):
            get_player_move(user_choise, gameSquare)
            get_computer_move(user_choise, gameSquare)
            draw_board(gameSquare)
        else:
            main()
    else:
        print("Неверный ввод символа")
        main()

main()