import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


# Створення об'єкту бота
bot = telebot.TeleBot('6090788351:AAGxbMW9ENAOK-LsuuS4ORoAn9gYH5iFhBo')

# Дані про спеціальності, курси та групи
groups_data = {
    '029 Інформаційна, бібліотечна та архівна справа': {
        'Курс 2': ['ІС-21'],
        'Курс 3': ['ІС-31']
    },
    '051 Економіка': {
        'Курс 1': ['І-11', 'І-12'],
        'Курс 2': ['І-21(Е-21)'],
        'Курс 3': ['Е-31 11']
    },
    '071 Облік і оподаткування': {
        'Курс 1': ['І-11', 'І-12'],
        'Курс 2': ['І-21(Б-21)']
    },
    '072 Фінанси, банківська справа та страхування': {
        'Курс 1': ['І-11', 'І-12'],
        'Курс 2': ['Ф-21'],
        'Курс 3': ['Фі-31']
    },
    '081 Право': {
        'Курс 2': ['П-21'],
        'Курс 3': ['Пі-31']
    },
    '122 Комп’ютерні науки': {
        'Курс 1': ['ІТ-11'],
        'Курс 2': ['ІТ-21', 'ІТ-22'],
        'Курс 3': ['ІТ-31', 'ІТ-32'],
        'Курс 4': ['ІТ-41']
    },
    '141 Електроенергетика, електротехніка та електромеханіка': {
        'Курс 1': ['ЕМ-11'],
        'Курс 2': ['ЕМ-21'],
        'Курс 3': ['ЕМ-31'],
        'Курс 4': ['ЕМ-41']
    },
    '192 Будівництво та цивільна інженерія': {
        'Курс 1': ['ТБ-11'],
        'Курс 2': ['Група 15', 'Група 16'],
        'Курс 3': ['ТБ-31'],
        'Курс 4': ['ТБ-41']
    },
    '274 Автомобільний транспорт': {
        'Курс 1': ['АТ-11', 'АТ-21'],
        'Курс 2': ['АТ-21', 'АТ-22', 'АТ-23/АТС', 'Аті-23'],
        'Курс 3': ['АТ-31', 'АТі-32', 'АТі-32/АТС-31'],
        'Курс 4': ['АТі-41', 'АТ-42']
    },
    '275 Транспортні технології (на автомобільному транспорті)': {
        'Курс 1': ['ТТ-11'],
        'Курс 2': ['ТТ-21', 'ТТ-22'],
        'Курс 3': ['ТТм-31', 'ТТмі-32'],
        'Курс 4': ['ТТ-41', 'ТТі-42']
    }
}

@bot.message_handler(commands=['start'])
def start_registration(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Доброго дня! Для реєстрації введіть ваше прізвище, ім'я та по батькові через пробіл:")
    bot.register_next_step_handler(message, ask_fullname)

# Функція для запитування повного імені
def ask_fullname(message):
    chat_id = message.chat.id
    fullname = message.text.split(" ")
    if len(fullname) != 3:
        bot.send_message(chat_id, "Будь ласка, введіть прізвище, ім'я та по батькові через пробіл:")
        bot.register_next_step_handler(message, ask_fullname)
        return

    user_id = message.from_user.id
    data = {'user_id': user_id, 'fullname': fullname}
    # Отримуємо дані про спеціальності з groups_data
    specialties = list(groups_data.keys())
    reply_keyboard = [specialties]
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(*[types.KeyboardButton(name) for name in reply_keyboard[0]])
    bot.send_message(chat_id, "Виберіть вашу спеціальність:", reply_markup=markup)
    bot.register_next_step_handler(message, select_specialty, data)

# Функція для обробки вибору спеціальності
def select_specialty(message, data):
    chat_id = message.chat.id
    specialty = message.text
    data['specialty'] = specialty
    # Отримуємо дані про курси для обраної спеціальності
    courses = groups_data.get(specialty, {})
    reply_keyboard = list(courses.keys())
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(*[types.KeyboardButton(name) for name in reply_keyboard])
    bot.send_message(chat_id, "Виберіть курс:", reply_markup=markup)
    bot.register_next_step_handler(message, select_course, data)

# Функція для обробки вибору курсу
def select_course(message, data):
    chat_id = message.chat.id
    course = message.text
    data['course'] = course
    # Отримуємо дані про групи для обраної спеціальності та курсу
    specialty = data['specialty']
    groups = groups_data.get(specialty, {}).get(course, [])
    reply_keyboard = [groups]
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(*[types.KeyboardButton(name) for name in reply_keyboard[0]])
    bot.send_message(chat_id, "Виберіть групу:", reply_markup=markup)
    bot.register_next_step_handler(message, select_group, data)

# Функція для обробки вибору групи
def select_group(message, data):
    chat_id = message.chat.id
    group = message.text
    data['group'] = group
    # Тут відправляємо дані студента студента на сервер
    # Виводимо повідомлення про успішну реєстрацію
    registration_data = f"Прізвище: {data['fullname'][0]}\nІм'я: {data['fullname'][1]}\nПо батькові: {data['fullname'][2]}\nСпеціальність: {data['specialty']}\nКурс: {data['course']}\nГрупа: {data['group']}"

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
