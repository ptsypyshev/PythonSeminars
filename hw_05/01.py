# Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# *** b) Подумайте как наделить бота ""интеллектом""
from random import randint
from time import sleep


def get_first_turn():
    print('Жеребьевка началась', end=' ', flush=True)
    for _ in range(3):
        sleep(0.5)
        print('.', end=' ', flush=True)

    bot_turn = randint(0, 1)
    if bot_turn:
        print('  =>   Бот ходит первым')
    else:
        print('  =>   Игрок ходит первым')

    return bot_turn


def take_candies(game_level=0):
    res = 0
    if game_level:
        res = candies_count % (max_take_number + 1)
    return res if res else randint(1, min(candies_count, max_take_number))


if __name__ == '__main__':
    # Original init settings
    candies_count = 2021
    max_take_number = 28

    # Simple init settings
    # candies_count = 15
    # max_take_number = 3

    # Set game level
    # game_level = 1
    try:
        game_level = int(input('Введите уровень сложности (0 или 1): '))
    except ValueError:
        print('Неправильный ввод, уровень сложности будет простым')
        game_level = 0

    bot_turn = get_first_turn()

    while candies_count > 0:
        print(f'Осталось {candies_count} конфет')
        if bot_turn:
            bot_takes = take_candies(game_level)
            candies_count -= bot_takes
            print(f'Бот забрал {bot_takes} конфет(ы/у)')
        else:
            # Comment next lines to automatic human random choice answer
            human_takes = 0
            while not 0 < human_takes <= max_take_number:
                limit = min(candies_count, max_take_number)
                msg = f'Сколько конфет берёте (от 1 до {limit}): '
                try:
                    human_takes = int(input(msg))
                except ValueError:
                    print('Неправильный ввод. Введите число')

            # Uncomment next lines to automatic human random choice answer
            # human_takes = take_candies()
            # print(f'Игрок забрал {human_takes} конфет')

            candies_count -= human_takes

        bot_turn = not bot_turn

    print('Игрок победил!') if bot_turn else print('Бот победил!')
