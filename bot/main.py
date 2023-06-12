import json

import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from dotenv import load_dotenv

import BOT_API

load_dotenv()

# Створення об'єкту бота
bot = telebot.TeleBot(os.environ.get("TELEGRAM_TOKEN"))

@bot.message_handler(commands=['start'])
def start_registration(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Доброго дня! Для реєстрації введіть ваше Ім'я:")
    bot.register_next_step_handler(message, ask_name)

def ask_name(message):
    '''Функція для запитування імені'''
    chat_id = message.chat.id
    first_name = message.text.strip()
    user_id = message.from_user.id
    username = message.from_user.username
    data = {'social_id': user_id, 'chat_id': chat_id, 'first_name': first_name, 'username': username}
    bot.send_message(chat_id, "Тепер введіть ваше прізвище:")
    bot.register_next_step_handler(message, ask_surname, data)

def ask_surname(message, data):
    '''Функція для запитування прізвища'''
    chat_id = message.chat.id
    last_name = message.text.strip()
    data['last_name'] = last_name
    json_string = json.dumps(BOT_API.get_specialty())
    specialty_data = json.loads(json_string)
    specialty = [item['name'] for item in specialty_data]
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(*[types.KeyboardButton(name) for name in specialty])
    bot.send_message(chat_id, "Виберіть вашу спеціальність:", reply_markup=markup)
    bot.register_next_step_handler(message, select_specialty, data)

def select_specialty(message, data):
    '''Функція для обробки вибору спеціальності і вибору курсу'''
    chat_id = message.chat.id
    specialty = message.text
    data['specialty'] = specialty
    # Отримуємо дані про курси для обраної спеціальності
    # Зчитуємо дані з JSON
    json_string = json.dumps(BOT_API.get_group())
    courses_data = json.loads(json_string)
    # Фільтруємо курси за вибраною спеціальністю
    courses = [course["course_num"] for course in courses_data if course["specialty"] == specialty]
    courses.sort(key=int)
    # Створюємо клавіатуру з кнопками курсів
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(*[types.KeyboardButton(course) for course in courses])
    bot.send_message(chat_id, "Виберіть курс:", reply_markup=markup)
    bot.register_next_step_handler(message, select_course, data, specialty)

def select_course(message, data, specialty):
    '''Функція для обробки вибору вибору курсу та вибір групи'''
    chat_id = message.chat.id
    course = int(message.text)
    # Зчитуємо дані з JSON
    json_string = json.dumps(BOT_API.get_group())
    courses_data = json.loads(json_string)
    # Фільтруємо Групи за вибраною спеціальністю та курсом
    groups = [group["name"] for group in courses_data if
              group["specialty"] == specialty and group["course_num"] == course]
    # Створюємо клавіатуру з кнопками груп
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(*[types.KeyboardButton(group) for group in groups])
    bot.send_message(chat_id, "Виберіть групу:", reply_markup=markup)
    bot.register_next_step_handler(message, select_group, data)

def select_group(message, data):
    '''Функція для обробки вибору вибору групи та реєстрація користувача на сервері'''
    chat_id = message.chat.id
    group = message.text
    data['group'] = group
    # Тут відправляємо дані студента на сервер
    BOT_API.post_user(data)
    # Виводимо повідомлення про успішну реєстрацію
    registration_data = f"Прізвище: {data['first_name']}\nІм'я: {data['last_name']}\nСпеціальність: {data['specialty']}\nГрупа: {data['group']}"

    keyboard = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton("Розклад", callback_data="action1")
    button2 = InlineKeyboardButton("Практика та працевлаштування", url="http://ncntu.com.ua/index.php/partnerstvo")
    button3 = InlineKeyboardButton("Ресурси та матеріали", url="https://sites.google.com/view/bibliotekancntu/%D0%B3"
                                                               "%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0-%D1%81%D1%82%D0"
                                                               "%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0")
    button4 = InlineKeyboardButton("Важливі контакти", callback_data="contact")
    keyboard.add(button1, button2, button3, button4)

    bot.send_message(chat_id, f"Ви успішно зареєстровані!\n\n{registration_data}", reply_markup=keyboard)



def contact(chat_id):
    keyboard = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton("Студенту", callback_data="cont_stud")
    button2 = InlineKeyboardButton("Випускнику", callback_data="cont_vupus")
    button3 = InlineKeyboardButton("Якість освіти", callback_data="cont_osvi")
    button4 = InlineKeyboardButton("Бібліотека", callback_data="cont_biblioteka")
    keyboard.add(button1, button2, button3, button4)

    bot.send_message(chat_id, "Контакти:", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    chat_id = call.message.chat.id
    if call.data == "action1":
        bot.send_message(chat_id, "Розклад")
    elif call.data == "contact":
        contact(chat_id)
    elif call.data == "cont_stud":
        bot.send_message(chat_id, "Контактна інформація:\n+380347520322\nПредставники коледжу:\n+380668009048 (Грицюк "
                                  "Христина Ігорівна)\n+380688683302 (Семенюк Христина Русланівна)")
    elif call.data == "cont_vupus":
        bot.send_message(chat_id, "Підрозділ сприяння працевлаштування випускників\n+380688683302")
    elif call.data == "cont_osvi":
        bot.send_message(chat_id, "Навчально-методична лабораторія\n+380347520322")
    elif call.data == "cont_biblioteka":
        bot.send_message(chat_id, "Електронна бібліотека\n+380685333241")


bot.polling()
