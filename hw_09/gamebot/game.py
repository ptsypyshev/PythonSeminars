from random import randint
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from string import Template
import messages as m

DEFAULT_CANDIES_COUNT = 15
DEFAULT_CANDIES_COUNT_BIG = 2021
DEFAULT_CANDIES_MAX_TAKE_NUMBER = 3
DEFAULT_CANDIES_MAX_TAKE_NUMBER_BIG = 28

STEP_CHOOSE_DIFFICULTY      = 0
STEP_CHOOSE_CANDIES_COUNT   = 1
STEP_CHOOSE_MAX_TAKE_NUMBER = 2
STEP_GET_FIRST_TURN         = 3
STEP_GAME_START             = 4
STEP_GAME_FINISHED          = 5


class Game():
    def __init__(self,
                hard_level: bool = False,
                candies_count: int = DEFAULT_CANDIES_COUNT,
                max_take_number: int = DEFAULT_CANDIES_MAX_TAKE_NUMBER) -> None:
        self.hard_level = hard_level
        self.candies_count = candies_count
        self.max_take_number = max_take_number
        self.current_step = STEP_CHOOSE_DIFFICULTY


def game_choose_difficulty(message, bot, game):
    '''Сохраняет выбранный уровень сложности в хранилище "state_storage"'''
    hard_level = True if message.text == m.GAME_CLEVER_BOT_MSG else False
    game.hard_level=hard_level

    markup = get_markup_btns(DEFAULT_CANDIES_COUNT, DEFAULT_CANDIES_COUNT_BIG)
    bot.send_message(message.chat.id, m.GAME_CHOOSE_CANDIES_COUNT_MSG, reply_markup=markup)

    bot.register_next_step_handler(message, game_choose_count, bot, game)


def game_choose_count(message, bot, game):
    '''Сохраняет общее количество конфет в "state_storage"'''
    try:
        candies_count = int(message.text)
    except ValueError:
        candies_count = DEFAULT_CANDIES_COUNT
        bot.send_message(message.chat.id, m.VALUE_ERROR_MSG)
    
    game.candies_count=candies_count
    markup = get_markup_btns(DEFAULT_CANDIES_MAX_TAKE_NUMBER, DEFAULT_CANDIES_MAX_TAKE_NUMBER_BIG)
    bot.send_message(message.chat.id, m.GAME_CHOOSE_MAX_TAKE_NUMBER_MSG, reply_markup=markup)
    bot.register_next_step_handler(message, game_choose_max_take, bot, game)
    

def game_choose_max_take(message, bot, game):
    '''Сохраняет максимальное количество конфет, забираемых за один ход, в "state_storage"'''
    try:
        max_take_number = int(message.text)
    except ValueError:
        max_take_number = DEFAULT_CANDIES_MAX_TAKE_NUMBER
        bot.send_message(message.chat.id, m.VALUE_ERROR_MSG)    

    game.max_take_number=max_take_number
    game_start(message, bot, game)


def game_start(message, bot, game):
    '''Запускает игру'''
    if game.max_take_number < 10:
        buttons = [str(i) for i in range(1, game.max_take_number + 1)]
        markup = get_markup_btns(*buttons)
    else:
        markup = ReplyKeyboardRemove()
    
    # msg = f'На столе {game.candies_count} конфет\nМожно взять не более {game.max_take_number}'
    msg = Template(m.GAME_STEP_MESSAGE).substitute(
        candies_count=game.candies_count,
        max_take_number=game.max_take_number
    )
    bot.send_message(message.chat.id, msg, reply_markup=markup)
    bot.register_next_step_handler(message, check_win, bot, game)


def check_win(message, bot, game):
    '''Проверяет победителя'''
    markup = ReplyKeyboardRemove()
    try:
        user_takes = int(message.text)
        if user_takes > min(game.max_take_number, game.candies_count):
            bot.send_message(message.chat.id, m.MAX_TAKE_ERROR_MSG)
            bot.register_next_step_handler(message, check_win, bot, game)
            return
        if user_takes <= 0:
            bot.send_message(message.chat.id, m.MIN_TAKE_ERROR_MSG)
            bot.register_next_step_handler(message, check_win, bot, game)
            return
    except ValueError:
        bot.send_message(message.chat.id, m.VALUE_ERROR_TRY_AGAIN_MSG)
        bot.register_next_step_handler(message, check_win, bot, game)
        return
    
    game.candies_count -= user_takes
    
    if game.candies_count:
        bot_takes = take_candies(game)
        game.candies_count -= bot_takes
        bot.send_message(message.chat.id, f'{m.BOT_TAKES_MSG} {bot_takes}')
        if game.candies_count:
            game_start(message, bot, game)
            return
        bot.send_message(message.chat.id, m.YOU_LOSE_MSG, reply_markup=markup)
        return
    else:
        bot.send_message(message.chat.id, m.YOU_WIN_MSG, reply_markup=markup)


def take_candies(game: Game) -> int:
    '''Реализует ход бота в умном/глупом режиме'''
    res = 0
    if game.hard_level:
        res = game.candies_count % (game.max_take_number + 1)
    return res if res else randint(1, min(game.candies_count, game.max_take_number))


def get_markup_btns(*buttons: str) -> ReplyKeyboardMarkup:
    '''Формирует объект ReplyKeyboardMarkup - добавляет кнопки из полученных аргументов'''
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup_buttons = []
    for btn in buttons:
        markup_buttons.append(KeyboardButton(btn))
    markup.add(*markup_buttons)
    return markup