import sqlite3

import telebot
from telebot import types
from db import Database
bot = telebot.TeleBot('6562981721:AAEMBmZ3Sav5xoz5DOj9r6CDJCgsAUcGYxs')





@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    btn1 = types.KeyboardButton('Начать заполнение')
    markup.add(btn1)
    bot.send_message(message.chat.id, 'Доброго дня,готов к работе', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Начать заполнение':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn2 = types.KeyboardButton('Группа 1 ')
        btn3 = types.KeyboardButton('Группа 2 ')
        markup.add(btn2)
        markup.add(btn3)
        bot.send_message(message.chat.id, 'Выберите группу', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Неизвестная Команда")

        bot.register_next_step_handler(message, on_click)

@bot.message_handler(func = lambda message: message.text == 'Группа 1' or message.text == 'Группа 2')


def group(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Группа 1':
        btn4 = types.KeyboardButton('Adil')
        btn5 = types.KeyboardButton('Kuka')
        btn_back = types.KeyboardButton('Nazad')
        markup.add(btn4,btn5)
        markup.add(btn_back)
        bot.send_message(message.chat.id, 'Выберите Ученика', reply_markup=markup)
    elif message.text == 'Группа 2':
        btn6 = types.KeyboardButton('Nurik')
        btn7 = types.KeyboardButton('Nurken')
        btn_back = types.KeyboardButton('Nazad')
        markup.add(btn6, btn7)
        markup.add(btn_back)
    bot.send_message(message.chat.id, 'Выберите Ученика', reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text == 'Nazad')
    def go_back(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn2 = types.KeyboardButton('Группа 1')
        btn3 = types.KeyboardButton('Группа 2')
        markup.add(btn2)
        markup.add(btn3)
        bot.send_message(message.chat.id, 'Выберите Группу', reply_markup= markup)



@bot.message_handler(commands=['students'])
def students(message):
    connection = sqlite3.connect('C:\\Users\\User\\IdeaProjects\\Hakaton-main\\database')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students WHERE group_name = 1")
    students = cursor.fetchall()
    connection.close()
    message_text = ''
    for student in students:
        message_text += f'{student[1]} - {student[2]}\n'
    bot.send_message(message.chat.id, message_text)


bot.polling(none_stop=True)
