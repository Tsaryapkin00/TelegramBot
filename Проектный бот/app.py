import telebot
from extensions import *

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def helping(message: telebot.types.Message):
    text = texta
    bot.reply_to(message, text)

@bot.message_handler(commands=['description',])
def description(message: telebot.types.Message):
    txt = txt1
    bot.reply_to(message, txt)

@bot.message_handler(commands=['values', ])
def values(message: telebot.types.Message):
    text = 'Доступны валюты:'
    for key in keys.keys():
        text = '\n           '.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(commands=['dollar', ])
def dollar(message: telebot.types.Message):
    val = 'доллар рубль 1'
    value = val.split(' ')

    quote, base, amount = value

    total_base = ValuteConvert.get_price(quote, base, amount)

    text = f'Курс доллара к рублю сейчас -   {total_base}'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['euro', ])
def euro(message: telebot.types.Message):
    val = 'евро рубль 1'
    value = val.split(' ')

    quote, base, amount = value

    total_base = ValuteConvert.get_price(quote, base, amount)

    text = f'Курс евро к рублю сейчас -   {total_base}'
    bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        value = message.text.split(' ')

        if len(value) != 3:
            raise APIException('Задано неверное количество параметров.')

        quote, base, amount = value
        total_base = ValuteConvert.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} -   {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
