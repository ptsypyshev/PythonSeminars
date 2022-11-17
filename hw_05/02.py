# Создайте программу для игры в ""Крестики-нолики"".

from random import randint
from time import sleep
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_board(board):
    cls()
    print('--- Игра крестики-нолики! ---')
    print('-' * 13)
    for row in board:
        print('|', end=' ')
        for col in row:
            print(col, end=' | ')
        print()
        print('-' * 13)


def get_first_turn():
    print('Жеребьевка началась', end=' ', flush=True)
    for _ in range(3):
        sleep(0.5)
        print('.', end=' ', flush=True)

    first_player = randint(0, 1)
    print(f'Первым ходит {players[first_player]}.')

    return first_player


def get_position():
    msg = f'Ходит {players[cur_player]}. Введите координаты (через пробел): '
    while True:
        try:
            pos = [int(i) - 1 for i in input(msg).split()]
            if len(pos) != 2 or not (0 <= pos[0] < 3) or not (0 <= pos[1] < 3):
                raise ValueError(f'Некорректный ввод {pos}')
            if board[pos[0]][pos[1]] != ' ':
                print('Это поле уже занято! Попробуйте другое.')
                continue
            break
        except ValueError:
            print('Некорректный ввод, попробуйте ещё раз')
    return pos


def check_win():
    lines = []
    for i in range(3):
        col_line = ''.join([board[i][j] for j in range(3)])
        row_line = ''.join([board[j][i] for j in range(3)])
        lines.extend([row_line, col_line])
    diag_line1 = ''.join([board[0][0], board[1][1], board[2][2]])
    diag_line2 = ''.join([board[0][2], board[1][1], board[2][0]])
    lines.extend([diag_line1, diag_line2])

    if 'XXX' in lines or 'OOO' in lines:
        return True
    return False


if __name__ == '__main__':
    board = [[' ' for _ in range(3)] for _ in range(3)]
    show_board(board)
    players = [input(f"Введите имя {i + 1} игрока: ") for i in range(2)]
    cur_player = get_first_turn()

    for i in range(9):
        symbol = 'O' if i % 2 else 'X'
        pos = get_position()
        board[pos[0]][pos[1]] = symbol
        show_board(board)
        if check_win():
            print(f'Выиграл {players[cur_player]}')
            break
        cur_player = not cur_player
    else:
        print('Ничья')
