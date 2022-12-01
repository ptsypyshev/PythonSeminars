from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from calculate import parse, calc
from custom_log import Logger


BOT_TOKEN = ''
LOG_FILE = "calc.log"
START_MESSAGE = '''Здравствуйте! Этот бот поддерживает команды:
/calc - Выведет результат вычисления выражения, введенного пользователем)'''
ASK_STATEMENT = 'Введите выражение:'
A = 0


bot = Bot(token=BOT_TOKEN)
updater = Updater(token=BOT_TOKEN)
dispatcher = updater.dispatcher
logger = Logger(LOG_FILE)


def start_cmd(update, context):
    '''Выводит информацию о поддерживаемых командах'''
    context.bot.send_message(update.effective_chat.id, START_MESSAGE)


def calc_cmd(update, context):
    '''Выводит сообщение о запросе вычисляемого выражения'''
    context.bot.send_message(update.effective_chat.id, ASK_STATEMENT)
    return A


def calc_bot(update, context):
    '''Запрос и вычисление выражения'''
    input_string = update.message.text
    operations = parse(input_string)
    try:
        result = calc(operations)
        result_msg = f'{input_string} = {result}'
        log_msg = f'User {update.effective_chat.id} has requested {input_string} and gotten result = {result}'
        context.bot.send_message(update.effective_chat.id, result_msg)
        logger.log(log_msg)
    except ZeroDivisionError as e:
        e_msg = "На ноль делить нельзя!"
        log_msg = f'User {update.effective_chat.id} has requested {input_string} and gotten an error {e}'
        context.bot.send_message(update.effective_chat.id, e_msg)
        logger.log(log_msg)    
    return ConversationHandler.END


def cancel(update, context):
    '''Реакция на отмену в ConversationHandler'''
    context.bot.send_message(update.effective_chat.id, "Bye!")

def run():
    '''Запуск бота'''
    start_cmd_handler = CommandHandler('start', start_cmd)
    calc_cmd_handler = CommandHandler('calc', calc_cmd)
    calc_bot_handler = MessageHandler(Filters.text, calc_bot)
    cancel_handler = MessageHandler(Filters.text, cancel)

    conv_handler = ConversationHandler(entry_points=[calc_cmd_handler],
                                            states={A: [calc_bot_handler],
                                                    },
                                            fallbacks=[cancel_handler])

    dispatcher.add_handler(start_cmd_handler)
    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()