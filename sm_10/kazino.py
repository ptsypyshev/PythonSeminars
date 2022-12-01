from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import randint

BOT_TOKEN = ''

bot = Bot(token=BOT_TOKEN)
updater = Updater(token=BOT_TOKEN)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'какова ваша ставка')


def bet(update, context):
    text = int(update.message.text)
    a=field()
    b=drow(a)
    sum=win(a,text)
    context.bot.send_message(update.effective_chat.id, b)
    context.bot.send_message(update.effective_chat.id, f'ваш выигрыш состовляет {sum}')

    
def field():
    list=[]
    list_new=[1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
    for i in range(12):
        chislo=randint(0,len(list_new)-1)
        list.append(list_new[chislo])
    return list


def drow(list):
    list_drow=""
    for i in range(3):
        list_drow+="--------------------\n"
        list_drow+=f'| {list[0 + i*4]} | {list[1 + i*4]} | {list[2 + i*4]} | {list[3 + i*4]} |\n'
    list_drow+="--------------------\n"
    return list_drow


def win(list,ctavka):
    pobeda=0
    win_position = ((0,1,2,3), (4,5,6,7), (8,9,10,11)) # проверяем возможные комбинации
    win_position2=((0,4,8), (1,5,9), (2,6,10), (3,7,11))
    for step in win_position:
       if list[step[0]] == list[step[1]] == list[step[2]]==list[step[3]]:
            if list[step[0]]==1:
                pobeda+=ctavka*2
            elif list[step[0]]==2:
                pobeda+=ctavka*3
            elif list[step[0]]==3:
                pobeda+=ctavka*4
            elif list[step[0]]==4:
                pobeda+=ctavka*5
    for step in win_position2:
       if list[step[0]] == list[step[1]] == list[step[2]]:
            if list[step[0]]==1:
                pobeda+=ctavka*2
            elif list[step[0]]==2:
                pobeda+=ctavka*3
            elif list[step[0]]==3:
                pobeda+=ctavka*4
            elif list[step[0]]==4:
                pobeda+=ctavka*5
    return pobeda


start_handler = CommandHandler('hello', start)
message_handler = MessageHandler(Filters.text, bet)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()