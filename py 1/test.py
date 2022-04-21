import telebot
from telebot import types
import random


bot = telebot.TeleBot("5169612952:AAFz9SxWzxCaCgQ2B0m4cAGrYz_RljpxX14")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»
    if message.text == "Привет":
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Привет")
    elif message.text == "/start":
        keyboard = types.InlineKeyboardMarkup()
        key_hello = types.InlineKeyboardButton(text='Приветствие', callback_data='hello')
        keyboard.add(key_hello)
        bot.send_message(message.from_user.id, text='Выбери команду', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, "Введите /start")
    
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "hello": 
        bot.send_message(call.message.chat.id, "Привет. Рад твоему сообщению)")
    
    
    

bot.polling(none_stop=True, interval=0)