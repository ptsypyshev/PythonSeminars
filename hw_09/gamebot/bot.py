import telebot
from remove_words import remove_words
from random import randint
import game as g
import os
import messages as m


START_CMD = 'start'
WORDS_CMD = 'words'
GAME_CMD = 'game'
FAST_GAME_CMD = 'fastgame'
COMMANDS = [START_CMD, WORDS_CMD, GAME_CMD, FAST_GAME_CMD]


def get_token(path: str = 'TOKEN.env') -> str:
    '''Функция получает токен Телеграм-бота из переменной окружения или из файла'''
    bot_token_env = os.environ.get('TG_TOKEN', None)
    if bot_token_env:
        return bot_token_env

    try:
        with open(path, 'r') as f:
            token = f.read().rstrip()
    except Exception as e:
        bot.reply_to(e)
    return token


# Инициализация бота
bot = telebot.TeleBot(get_token())
state_storage = {}


@bot.message_handler(commands=COMMANDS)
def init(message):
    '''Обработка команд'''
    if message.text.lstrip('/') == START_CMD:
        bot.send_message(message.chat.id, m.START_MESSAGE)
    elif message.text.lstrip('/') == WORDS_CMD:
        bot.send_message(message.chat.id, m.WORDS_MESSAGE)
        bot.register_next_step_handler(message, remove_words, bot)
    elif message.text.lstrip('/') == FAST_GAME_CMD:
        bot.send_message(message.chat.id, m.GAME_START_MESSAGE)
        game = g.Game(
            hard_level=True,
            candies_count=g.DEFAULT_CANDIES_COUNT,
            max_take_number=g.DEFAULT_CANDIES_MAX_TAKE_NUMBER
            )
        state_storage[message.chat.id] = game
        g.game_start(message, bot, game)
    else:
        bot.send_message(message.chat.id, m.GAME_START_MESSAGE)
        game = g.Game()
        state_storage[message.chat.id] = game

        markup = g.get_markup_btns(m.GAME_STUPID_BOT_MSG, m.GAME_CLEVER_BOT_MSG)
        bot.send_message(message.chat.id, m.GAME_CHOOSE_DIFFICULTY_MSG, reply_markup=markup)

        bot.register_next_step_handler(message, g.game_choose_difficulty, bot, game)


@bot.message_handler(content_types=['text'])
def echo(message):
    '''Выводит подсказку, если не запущена ни одна команда'''
    bot.send_message(message.chat.id, m.START_MESSAGE)


def start_bot():
    '''Запуск бота'''
    bot.polling(none_stop=True, interval=0)
