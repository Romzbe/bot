from bot import keys, TOKEN
import telebot
from extensions import APIException as A
from extensions import CriptoConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def help(mes:telebot.types.Message):
    text="Чтобы начать работу введите команду:\n имя валюты\ в какую первести\ количество валюты. \n вы можете увидеть все доступные валюты /value"
    bot.reply_to(mes,text)

    bot.send_message(mes.chat.id,"hellov")

@bot.message_handler(commands=["value"])
def value(mess:telebot.types.Message):
    text="доступные валюты"
    for i in keys:
        text="\n".join((text, i, ))
    bot.reply_to(mess, text)


@bot.message_handler(content_types=["text", ])
def convert(message:telebot.types.Message):
    try:
        value = message.text.split(" ")
        if len(value) != 3:
            raise A ("Слишком много параметров")
        q, b, a, = value
        tot = CriptoConverter.convert(q,b,a)
    except A as e:
        bot.reply_to(message, f"Ошибка пользователя\n {e}")
    except Exception as e:
        bot.reply_to(message,f"ошибка сервера\n {e}")
    else:

        text = f'Цена {a} {q} в {b} - {tot} '
        bot.send_message(message.chat.id, text)




bot.polling(non_stop=True)




