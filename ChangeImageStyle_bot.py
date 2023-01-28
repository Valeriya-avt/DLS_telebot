import telebot
import numpy as np
import subprocess
from telebot import types
import threading
import pictures_processing

from datetime import datetime 

db_photos = {}
with open("creds/ChangeImageStyle_bot.txt", "r") as f:
    change_image_style_creds = f.read().strip()
bot = telebot.TeleBot(change_image_style_creds)

def start_keyboard():
    buttons = [
        types.InlineKeyboardButton(text="Перенести стиль", callback_data="button_style")
        
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def log(text):
    time_stamp = datetime.now().strftime("%Y.%m.%d-%H:%M:%S")
    print(time_stamp + " " + text)


class User:
    def __init__(self, user_id):
        self.id = user_id
        self.style_img = 0
        self.type_algo = None

    def restart(self, algo=None):
        self.style_img = 0
        self.type_algo = algo


greeting_string = "Привет! Я бот, который может переносить стиль с одного изображения на другое:)"

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    start = "/start"
    user_id = message.from_user.id
    user_name = message.from_user.username
    answer_for_no = "Для того, чтобы перенести стиль с одного изображения на другое, нажмите "
    question = str(message.text)

    log_text = "User ({0}): {1}".format(user_name, question)
    log(log_text)

    db_photos[message.from_user.id] = User(message.from_user.id)

    if (message.text == start):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton("Перенести стиль")
        markup.add(btn)
        bot.send_message(user_id, text=greeting_string, reply_markup=markup)

    elif (message.text == "Перенести стиль"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(user_id, text="Отправь мне картинку, с которой нужно взять стиль", reply_markup=markup)
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton("Перенести стиль")
        markup.add(btn)
        bot.send_message(user_id, text=greeting_string, reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton("Перенести стиль")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn, back)
        bot.send_message(user_id, "Неверный ввод. Выберите необходимую опцию", reply_markup=markup)


@bot.message_handler(content_types=['photo'])
def get_photo_messages(message):
    user_id = message.from_user.id
    user_name = message.from_user.username

    photo = message.photo[-1]
    tele_file = bot.get_file(photo.file_id)
    image = bot.download_file(tele_file.file_path)

    user = db_photos[user_id]

    if user.style_img == 0:
        user.style_img = image
        bot.send_message(user_id, "Отправь картинку, на которую надо перенести стиль")
    else:
        bot.send_message(user_id, "Почти готово...")
        log("Process")

        pictures_processing.style_transfer(message, user.style_img, image)

def on_shutdown(dp):
    log("Выключен")
    bot.close()
    bot.wait_closed()

bot.polling(none_stop=True, interval=0)
