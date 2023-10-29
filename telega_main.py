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
        btn2 = types.KeyboardButton('Группа 1')
        btn3 = types.KeyboardButton('Группа 2')
        markup.add(btn2)
        markup.add(btn3)
        bot.send_message(message.chat.id, 'Выберите группу', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Неизвестная Команда")

        bot.register_next_step_handler(message, on_click)
selected_group = {}
@bot.message_handler(func = lambda message: message.text == 'Группа 1' or message.text == 'Группа 2')


def group(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Группа 1':
        selected_group[message.chat.id] = 'Группа 1'
        btn4 = types.KeyboardButton('Adil')
        btn5 = types.KeyboardButton('Kuka')
        btn_back = types.KeyboardButton('Nazad')
        markup.add(btn4,btn5)
        markup.add(btn_back)
        bot.send_message(message.chat.id, 'Выберите Ученика', reply_markup=markup)
    elif message.text == 'Группа 2':
        selected_group[message.chat.id] = 'Группа 2'
        btn6 = types.KeyboardButton('Nurik')
        btn7 = types.KeyboardButton('Nurken')
        btn_back = types.KeyboardButton('Nazad')
        markup.add(btn6, btn7)
        markup.add(btn_back)
        bot.send_message(message.chat.id, 'Выберите Ученика', reply_markup=markup)
    else:
        bot.send_message(message.chat.id,'Неизвестная Команда')

    @bot.message_handler(func=lambda message: message.text == 'Nazad')
    def go_back(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn2 = types.KeyboardButton('Группа 1')
        btn3 = types.KeyboardButton('Группа 2')
        markup.add(btn2)
        markup.add(btn3)
        bot.send_message(message.chat.id, 'Выберите Группу', reply_markup= markup)

@bot.message_handler(func=lambda message: message.text == 'Adil' or message.text == 'Kuka' or message.text == 'Nurik' or message.text == 'Nurken')

def student(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Adil'  or message.text == 'Kuka' or message.text == 'Nurik' or message.text == 'Nurken':
        btn8 = types.KeyboardButton('Домашка')
        btn9 = types.KeyboardButton('Классная Работа')
        btn11 = types.KeyboardButton('Назад')
        markup.add(btn8,btn9)
        markup.add(btn11)
        bot.send_message(message.chat.id,"Выберите Действие",reply_markup=markup)
    else:
        bot.send_message(message.chat.id,'Неверная команда,повторите попытку')

        bot.register_next_step_handler(message, student)


@bot.message_handler(func=lambda message: message.text == 'Назад')
def go_back(message):
    group = selected_group.get(message.chat.id)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if group == 'Группа 1':
        btn4 = types.KeyboardButton('Adil')
        btn5 = types.KeyboardButton('Kuka')
        btn_back = types.KeyboardButton('Nazad')
        markup.add(btn4, btn5)
        markup.add(btn_back)
        bot.send_message(message.chat.id, 'Выберите Ученика', reply_markup=markup)
    elif group == 'Группа 2':
        btn6 = types.KeyboardButton('Nurik')
        btn7 = types.KeyboardButton('Nurken')
        btn_back = types.KeyboardButton('Nazad')
        markup.add(btn6, btn7)
        markup.add(btn_back)
        bot.send_message(message.chat.id, 'Выберите Ученика', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text=='Домашка')
def ask_theme(message):
    bot.send_message(message.chat.id, 'Напишите тему')
    bot.register_next_step_handler(message, save_homework_topic)

def save_homework_topic(message):
    connection = sqlite3.connect('C:\\Users\\user\\IdeaProjects\\projectX\\database')
    cursor = connection.cursor()
    student_id = 1
    homework_theme = message.text
    cursor.execute("UPDATE students SET homework_theme = ? WHERE student_id = 1", (homework_theme,))
    connection.commit()
    bot.send_message(message.chat.id,f'Тема сохранена: {homework_theme}')

@bot.message_handler(func=lambda message: message.text == 'Далее')
def ask_ex_count(message):
    bot.send_message(message.chat.id, 'Какие задачи были выполнены?')
    bot.register_next_step_handler(message, save_homework_ex_count)

def save_homework_ex_count(message):
    connection = sqlite3.connect('C:\\Users\\user\\IdeaProjects\\projectX\\database')
    cursor = connection.cursor()
    student_id = 1
    homework = message.text
    cursor.execute("UPDATE students SET homework = ? WHERE student_id = 1" ,(homework,))
    connection.commit()
    bot.send_message(message.chat.id, 'Задачи сохранены')

@bot.message_handler(func=lambda message: message.text == 'Назад')
def go_back(message):
    group = selected_group.get(message.chat.id)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if group == 'Группа 1':
        btn4 = types.KeyboardButton('Adil')
        btn5 = types.KeyboardButton('Kuka')
        btn_back = types.KeyboardButton('Nazad')
        markup.add(btn4, btn5)
        markup.add(btn_back)
        bot.send_message(message.chat.id, 'Выберите Ученика', reply_markup=markup)
    elif group == 'Группа 2':
        btn6 = types.KeyboardButton('Nurik')
        btn7 = types.KeyboardButton('Nurken')
        btn_back = types.KeyboardButton('Nazad')
        markup.add(btn6, btn7)
        markup.add(btn_back)
        bot.send_message(message.chat.id, 'Выберите Ученика', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text=='Классная Работа')
def ask_theme(message):
    bot.send_message(message.chat.id, 'Напишите тему')
    bot.register_next_step_handler(message, save_classwork_topic)

def save_classwork_topic(message):
    connection = sqlite3.connect('C:\\Users\\user\\IdeaProjects\\projectX\\database')
    cursor = connection.cursor()
    student_id = 1
    classwork_theme = message.text
    cursor.execute("UPDATE students SET classwork_theme = ? WHERE student_id = 1", (classwork_theme,))
    connection.commit()
    bot.send_message(message.chat.id,f'Тема сохранена: {classwork_theme}')
@bot.message_handler(func=lambda message: message.text == 'Далее')
def ask_ex_count(message):
    bot.send_message(message.chat.id, 'Какие задачи были выполнены?')
    bot.register_next_step_handler(message, save_classwork_ex_count)

def save_classwork_ex_count(message):
    connection = sqlite3.connect('C:\\Users\\user\\IdeaProjects\\projectX\\database')
    cursor = connection.cursor()
    student_id = 1
    classwork = message.text
    cursor.execute("UPDATE students SET classwork = ? WHERE student_id = 1" ,(classwork,))
    connection.commit()
    bot.send_message(message.chat.id, 'Задачи сохранены')


@bot.message_handler(func=lambda message: message.text == 'Назад')
def go_back(message):
    group = selected_group.get(message.chat.id)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if group == 'Группа 1':
        btn4 = types.KeyboardButton('Adil')
        btn5 = types.KeyboardButton('Kuka')
        btn_back = types.KeyboardButton('Nazad')
        markup.add(btn4, btn5)
        markup.add(btn_back)
        bot.send_message(message.chat.id, 'Выберите Ученика', reply_markup=markup)
    elif group == 'Группа 2':
        btn6 = types.KeyboardButton('Nurik')
        btn7 = types.KeyboardButton('Nurken')
        btn_back = types.KeyboardButton('Nazad')
        markup.add(btn6, btn7)
        markup.add(btn_back)
        bot.send_message(message.chat.id, 'Выберите Ученика', reply_markup=markup)


@bot.message_handler(commands=['students'])
def students(message):
    connection = sqlite3.connect('C:\\Users\\user\\IdeaProjects\\projectX\\database')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    connection.close()
    message_text = ''
    for student in students:
        message_text += f'{student[1]} - {student[2]} - {student[3]} - {student[4]} - {student[6]} - {student[7]}\n'
    bot.send_message(message.chat.id, message_text)


bot.polling(none_stop=True)
