import telebot
from extensions import *

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def helping(message: telebot.types.Message):
    text = 'Для начала работы введите команду боту в формате: \n <название валюты> \
<название валюты в которую надо перевести>\
<количество переводимой валюты>\nЧтобы увидеть список доступных валю введите: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values', ])
def values(message: telebot.types.Message):
    text = 'Доступны валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        value = message.text.split(' ')

        if len(value) != 3:
            raise ConvertionException('Задано неверное количество параметров.')

        quote, base, amount = value
        total_base = ValuteConvert.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
