import telebot

TOKEN = '5882278409:AAHj56DTLZOww7WSPTdOAQbhdmMRVxzDZUM'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Привет, {message.chat.username}")


@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    pass


@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')


bot.polling(none_stop=True)
