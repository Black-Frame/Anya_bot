# Привет бро если ты хочешь стать хакером или просто хочешь посмотреть фукцонал бота 
# тебе сюда t.me/blacktools_chat


# Импортируем все

import telebot

TOKEN = '' #токен
NAME = ('аня','ан','анна','анюха','анюта')

#Создаем бота
bot = telebot.TeleBot(TOKEN)

#Функция старт
@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет я Аня\nЯ самообучающийся бот ИИ\nМой создатель @Bekhsdev\nМои исходники: \n)))))')

@bot.message_handler(content_types=['text'])
def text_message(message):
    word = message.text
    ' '.split(word)
    if ')' in word:
        bot.send_message(message.chat.id, ')))')
    elif message.text == 'Аня, к ноге!':
        bot.send_message(message.chat.id, 'Слушаюсь')
    for x in NAME:
        if x in word.lower() and 'привет' not in word.lower():
            bot.send_message(message.chat.id, 'Что?')
            break

        elif x in word.lower() and 'привет' in word.lower():
            bot.send_message(message.chat.id, 'Привет)')
            break

#Зацикливаем
bot.polling(none_stop=True, interval=0, timeout=20)