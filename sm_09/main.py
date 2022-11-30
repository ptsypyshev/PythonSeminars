from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

BOT_TOKEN = ""

bot = Bot(token=BOT_TOKEN)
updater = Updater(token=BOT_TOKEN)
dispatcher = updater.dispatcher

A = 0
B = 1

def start(updater, context):
    context.bot.send_message(updater.effective_chat.id, "Привет,\nКак дела?")
    return A

def howareyou(updater, context):
    text = updater.message.text
    if "хор" in text.lower():
        context.bot.send_message(updater.effective_chat.id, "Я рад, что у тебя всё хорошо")
    else:
        context.bot.send_message(updater.effective_chat.id, "Не переживай, всё будет хорошо")
    context.bot.send_message(updater.effective_chat.id, "Как у тебя погода?")
    return B

def weather(updater, context):
    text = updater.message.text
    if "солн" in text.lower():
        context.bot.send_message(updater.effective_chat.id, "У меня тоже солнце")
    else:
        context.bot.send_message(updater.effective_chat.id, "У природы нет плохой погоды")
    context.bot.send_message(updater.effective_chat.id, "Bye!")
    return ConversationHandler.END

def cancel(updater, context):
    context.bot.send_message(updater.effective_chat.id, "Bye!")

# def voice(updater, context):
#     context.bot.send_message(updater.effective_chat.id, "Cannot parse voice")

# def text(updater, context):
#     text = updater.message.text
#     if "прив" in text.lower():
#         context.bot.send_message(updater.effective_chat.id, "Hi")
    

if __name__ == "__main__":
    start_handler = CommandHandler("start", start)
    text_howareyou_handler = MessageHandler(Filters.text, howareyou)
    text_weather_handler = MessageHandler(Filters.text, weather)
    cancel_handler = MessageHandler(Filters.text, cancel)
    # voice_handler = MessageHandler(Filters.voice, voice)
    # text_handler = MessageHandler(Filters.text, text)

    conv_handler = ConversationHandler(entry_points=[start_handler],
                                        states={A: [text_howareyou_handler],
                                                B: [text_weather_handler]
                                                },
                                        fallbacks=[cancel_handler])

    # dispatcher.add_handler(start_handler)
    dispatcher.add_handler(conv_handler)
    # dispatcher.add_handler(text_howareyou_handler)
    # dispatcher.add_handler(text_weather_handler)
    # dispatcher.add_handler(cancel_handler)
    # dispatcher.add_handler(voice_handler)
    # dispatcher.add_handler(text_handler)
    updater.start_polling()
    updater.idle()
